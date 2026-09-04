from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime, timedelta
import jwt
import bcrypt
from config import settings
from database import get_user_by_email, get_user_by_id, insert_user
from models import UserCreate, UserLogin, UserResponse, TokenResponse

router = APIRouter()

# Funções auxiliares para autenticação e segurança.
def hash_password(password: str) -> str:
    """Criptografa a senha."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password: str, password_hash: str) -> bool:
    """Verifica se a senha está correta."""
    return bcrypt.checkpw(password.encode(), password_hash.encode()) # Compara a senha com a criptografada no banco de dados.

def create_access_token(user_id: str) -> str:
    """Cria um JWT token para o usuário.""" # Util para manter o usuário logado e autenticar requisições.
    payload = {
        "sub": user_id, # ID do usuário.
        "exp": datetime.utcnow() + timedelta(days=7)  # Duração do token (7 dias).
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return token

def verify_token(token: str) -> str:
    """Verifica se o token é válido e retorna o ID do usuário."""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="Token inválido.") # Verifica se o token contém o ID do usuário.
        return user_id
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado.") # Verifica se o token expirou.
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido.") # Verifica se o token é inválido.

def get_current_user(authorization: str = None) -> str:
    """Pega o usuário a partir do token no header."""
    if not authorization:
        raise HTTPException(status_code=401, detail="Token não fornecido.") # Verifica se o token está preenchido.
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=401, detail="Tipo de autenticação inválido") # Verifica se o tipo de autenticação é Bearer.
        return verify_token(token) # Verifica se o token é válido e retorna o ID do usuário.
    except ValueError:
        raise HTTPException(status_code=401, detail="Formato de token inválido")

# Rotas.
@router.post("/register", response_model=TokenResponse, tags=["Auth"])
def register(user: UserCreate):
    """Criar novo usuário."""
    existing_user = get_user_by_email(user.email) # Verifica se email já existe.
    if existing_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado.")
    password_hash = hash_password(user.password) # Criptografa a senha.
    new_user = insert_user(
        email=user.email,
        password_hash=password_hash,
        name=user.name
    ) # Insere usuário no banco de dados.
    if not new_user:
        raise HTTPException(status_code=500, detail="Erro ao criar usuário.") # Verifica se o usuário foi criado com sucesso.
    access_token = create_access_token(new_user["id"]) # Cria token de acesso. 
    return {"access_token": access_token, "token_type": "bearer"} # Retorna token de acesso e tipo do token (Bearer).

@router.post("/login", response_model=TokenResponse, tags=["Auth"])
def login(user: UserLogin):
    """Fazer login."""
    db_user = get_user_by_email(user.email) # Busca usuário pelo email.
    if not db_user:
        raise HTTPException(status_code=401, detail="Email ou senha incorretos.") # Verifica se o usuário existe no banco de dados.
    if not verify_password(user.password, db_user["password_hash"]): 
        raise HTTPException(status_code=401, detail="Email ou senha incorretos.") # Verifica se a senha está correta comparando com a senha criptografada no banco de dados.
    access_token = create_access_token(db_user["id"]) # Cria o token de acesso.
    return {"access_token": access_token, "token_type": "bearer"}  #  Retorna token de acesso e tipo do token (Bearer).

@router.get("/me", response_model=UserResponse, tags=["Auth"])
def get_current_user_info(authorization: str = None):
    """Ver dados do usuário logado."""
    user_id = get_current_user(authorization) # Verifica token e pega ID do usuário.
    user = get_user_by_id(user_id) # Busca usuário no banco de dados.
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.") # Verifica se o usuário existe no banco de dados.
    return user

@router.delete("/delete-account", tags=["Auth"])
def delete_account(authorization: str = None):
    """Deletar conta do usuário."""
    user_id = get_current_user(authorization) # Verifica token e pega ID do usuário.
    
    # TODO: Implementar soft delete no banco
    # Por enquanto, retorna sucesso
    return {"mensagem": "Conta deletada com sucesso."}

@router.post("/logout", tags=["Auth"])
def logout():
    """Fazer logout (apenas informativo.)"""
    return {"mensagem": "Desconectado com sucesso."}
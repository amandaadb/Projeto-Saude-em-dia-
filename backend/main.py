from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from config import settings

# Criar a API.
app = FastAPI(
    title="API: Saúde em Dia",
    version="1.0.0"
)

# Permitir requisições do frontend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite requisições de todas as origens (frontend).
    allow_credentials=True, # Permite envio de cookies e credenciais.
    allow_methods=["*"], # Permite todos os métodos HTTP (GET, POST, PUT, DELETE, etc.).
    allow_headers=["*"], # Permite todos os cabeçalhos HTTP (Content-Type, Authorization, etc.).
)

@app.get("/") # Rota raiz da API.
def home():
    """API está online."""
    return {"mensagem": "Bem-vindo à API: Saúde em Dia! 🏥"}

@app.get("/health") # Rota de verificação de saúde da API.
def health():
    """Verifica se tá tudo ok com a API."""
    return {"status": "online"}

# Rotas.
from routes import auth
app.include_router(auth.router, prefix="/api/auth")

# Executar a API.
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )
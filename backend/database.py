from supabase import create_client, Client
from datetime import datetime
from config import settings

# Conexão com Supabase.
supabase: Client = create_client(
    settings.SUPABASE_URL, 
    settings.SUPABASE_SERVICE_KEY # Chave ADMIN.
)

def execute_query(table: str, method: str, **kwargs):
    """ xecuta uma query no Supabase."""
    try: 
        query = getattr(supabase.table(table), method)(**kwargs)
        return query
    except Exception as e:
        print(f"Erro ao executar a query: {e}")
        return None

# Usuário.
def get_user_by_email(email: str):
    """Retorna um usuário ativo pelo email."""
    result = supabase.table("users").select("*").eq("email", email).eq("fl_deleted", False).execute()
    return result.data[0] if result.data else None # Retorna primeiro resultado ou None.

def get_user_by_id(user_id: str):
    """Retorna um usuário ativo pelo ID."""
    result = supabase.table("users").select("*").eq("id", user_id).eq("fl_deleted", False).execute()
    return result.data[0] if result.data else None # Retorna primeiro resultado ou None.

def insert_user(email: str, password_hash: str, name: str = None):
    """Insere um novo usuário na tabela 'users'."""
    data = {
        "email": email,
        "password_hash": password_hash,
        "name": name
    }
    try:
        result = supabase.table("users").insert(data).execute() 
        return result.data[0] if result.data else None # Retorna o usuário criado.
    except Exception as e:
        print(f"Erro ao inserir usuário: {e}")
        return None

def update_user(user_id: str, email: str = None, name: str = None, password_hash: str = None):
    """Atualiza um usuário existente."""
    data = {}
    if email is not None:
        data["email"] = email
    if name is not None:
        data["name"] = name
    if password_hash is not None:
        data["password_hash"] = password_hash
    if not data:
        return None
    try:
        result = supabase.table("users").update(data).eq("id", user_id).eq("fl_deleted", False).execute()
        return result.data[0] if result.data else None # Retorna o usuário atualizado.
    except Exception as e:
        print(f"Erro ao atualizar usuário: {e}")
        return None

def delete_user(user_id: str):
    """Deleta usuário e todos seus dados (soft delete)."""
    try:
        result = supabase.table("users").update({  
            "fl_deleted": True,  # Flag de deleção.
            "dt_deleted": datetime.utcnow().isoformat() # Data/hora da deleção.
        }).eq("id", user_id).eq("fl_deleted", False).execute() # Deleta apenas se estiver ativo.
        return result.data[0] if result.data else None
    except Exception as e:
        print(f"Erro ao deletar usuário: {e}")
        return None

# Medicamentos.
def insert_medicine(user_id: str, name: str, dosage: str = None, description: str = None):
    """Insere um novo medicamento na tabela 'medicines'."""
    data = {
        "user_id": user_id,
        "name": name,
        "dosage": dosage,
        "description": description,
        "fl_active": True
    }
    try:
        result = supabase.table("medicines").insert(data).execute() 
        return result.data[0] if result.data else None # Retorna o medicamento criado.
    except Exception as e:
        print(f"Erro ao inserir medicamento: {e}")
        return None

def get_medicines_by_user(user_id: str):
    """Retorna todos os medicamentos de um usuário."""
    result = supabase.table("medicines").select("*").eq("user_id", user_id).eq("fl_active", True).execute()
    return result.data if result.data else [] # Retorna lista de medicamentos ou lista vazia.

def get_medicine_by_id(medicine_id: str, user_id: str):
    """ Retorna um medicamento específico pelo ID e usuário."""
    result = supabase.table("medicines").select("*").eq("id", medicine_id).eq("user_id", user_id).eq("fl_active", True).execute()
    return result.data[0] if result.data else None # Retorna o medicamento ou None.

def update_medicine(medicine_id: str, user_id: str, name: str = None, dosage: str = None, description: str = None):
    """Atualiza um medicamento existente."""
    data = {
        "name": name, 
        "dosage": dosage,
        "description": description
    }
    try:
        result = (supabase.table("medicines").update(data).eq("id", medicine_id).eq("user_id", user_id).eq("fl_active", True).execute())
        return result.data[0] if result.data else None
    except Exception as e:
        print(f"Erro ao atualizar medicamento: {e}")
        return None

def delete_medicine(medicine_id: str, user_id: str):
    """Deleta um medicamento e todos seus dados (soft delete)."""
    try:
        result = (supabase.table("medicines").update({"fl_active": False}).eq("id", medicine_id).eq("user_id", user_id).eq("fl_active", True).execute())
        return result.data[0] if result.data else None
    except Exception as e:
        print(f"Erro ao deletar medicamento: {e}")
        return None
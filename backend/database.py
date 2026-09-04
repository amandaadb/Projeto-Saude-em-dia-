from supabase import create_client, Client
from config import settings

# Conexão com Supabase.
supabase: Client = create_client(
    settings.SUPABASE_URL, 
    settings.SUPABASE_SERVICE_KEY # Chave ADMIN.
)


def execute_query(table: str, method: str, **kwargs):
    """ Executa uma query no Supabase. """
    try: 
        query = getattr(supabase.table(table), method)(**kwargs)
        return query
    except Exception as e:
        print(f"Erro ao executar a query: {e}")
        return None

def get_user_by_email(email: str):
    """ Retorna um usuário pelo email. """
    result = supabase.table("users").select("*").eq("email", email).execute()
    return result.data[0] if result.data else None # Retorna primeiro resultado ou None.

def get_user_by_id(user_id: str):
    """ Retorna um usuário pelo ID. """
    result = supabase.table("users").select("*").eq("id", user_id).execute()
    return result.data[0] if result.data else None # Retorna primeiro resultado ou None.

def insert_user(email: str, password_hash: str, name: str = None):
    """ Insere um novo usuário na tabela 'users'. """
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

def delete_user(user_id: str):
    """ Deleta usuário e todos seus dados (soft delete) """
    result = supabase.table("users").update({  
        "fl_deleted": True,  # Flag de deleção.
        "dt_deleted": "now()" # Data/hora da deleção.
    }).eq("id", user_id).execute()
    return result
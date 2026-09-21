from datetime import datetime
from supabase import create_client, Client
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
    result = supabase.table("users").select("*").eq("email", email).eq("fl_active", True).execute()
    return result.data[0] if result.data else None # Retorna primeiro resultado ou None.

def get_user_by_id(user_id: str):
    """Retorna um usuário ativo pelo ID."""
    result = supabase.table("users").select("*").eq("id", user_id).eq("fl_active", True).execute()
    return result.data[0] if result.data else None # Retorna primeiro resultado ou None.

def insert_user(name: str, email: str, phone: str, password_hash: str, dt_birth: str, blood_type: str = None, emergency_contact_name: str = None, emergency_contact_phone: str = None, allergies: str = None, chronic_conditions: str = None):
    """Insere um novo usuário na tabela 'users'."""
    data = {
        "name": name,
        "phone": phone,
        "email": email,
        "password_hash": password_hash,
        "dt_birth": dt_birth,
        "blood_type": blood_type,
        "emergency_contact_name": emergency_contact_name,
        "emergency_contact_phone": emergency_contact_phone,
        "allergies": allergies,
        "chronic_conditions": chronic_conditions
    }
    try:
        result = supabase.table("users").insert(data).execute() 
        return result.data[0] if result.data else None # Retorna o usuário criado.
    except Exception as e:
        print(f"Erro ao inserir usuário: {e}")
        return None

def update_user(user_id: str, name: str = None, phone: str = None, email: str = None, password_hash: str = None, dt_birth: str = None, blood_type: str = None, emergency_contact_name: str = None, emergency_contact_phone: str = None, allergies: str = None, chronic_conditions: str = None):
    """Atualiza um usuário existente."""
    data = {}
    if name is not None:
        data["name"] = name
    if phone is not None:
        data["phone"] = phone
    if email is not None:
        data["email"] = email
    if password_hash is not None:
        data["password_hash"] = password_hash
    if dt_birth is not None:
        data["dt_birth"] = dt_birth
    if blood_type is not None:
        data["blood_type"] = blood_type
    if emergency_contact_name is not None:
        data["emergency_contact_name"] = emergency_contact_name
    if emergency_contact_phone is not None:
        data["emergency_contact_phone"] = emergency_contact_phone
    if allergies is not None:
        data["allergies"] = allergies
    if chronic_conditions is not None:
        data["chronic_conditions"] = chronic_conditions
    if not data:
        return None
    try:
        result = supabase.table("users").update(data).eq("id", user_id).eq("fl_active", True).execute()
        return result.data[0] if result.data else None # Retorna o usuário atualizado.
    except Exception as e:
        print(f"Erro ao atualizar usuário: {e}")
        return None

def delete_user(user_id: str):
    """Deleta usuário e todos seus dados (soft delete)."""
    try:
        result = supabase.table("users").update({  
            "fl_active": False,  # Flag de deleção.
        }).eq("id", user_id).eq("fl_active", True).execute() # Deleta apenas se estiver ativo.
        return result.data[0] if result.data else None
    except Exception as e:
        print(f"Erro ao deletar usuário: {e}")
        return None

# Medicamentos.
def insert_medicine(user_id: str, name: str, dosage: str = None, quantity: int = None,usage_type: str = None,usage_instructions: str = None, stock: int = None, description: str = None):
    """Insere um novo medicamento na tabela 'medicines'."""
    data = {
        "user_id": user_id,
        "name": name,
        "dosage": dosage,
        "quantity": quantity,
        "usage_type": usage_type,
        "usage_instructions": usage_instructions,
        "stock": stock,
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

def update_medicine(medicine_id: str, user_id: str, name: str = None, dosage: str = None,quantity: int = None,usage_type: str = None,usage_instructions: str = None, stock: int = None, description: str = None):
    """Atualiza um medicamento existente."""
    data = {}

    if name is not None:
        data["name"] = name
    if dosage is not None:
        data["dosage"] = dosage
    if quantity is not None:
        data["quantity"] = quantity
    if usage_type is not None:
        data["usage_type"] = usage_type
    if usage_instructions is not None:
        data["usage_instructions"] = usage_instructions
    if stock is not None:
        data["stock"] = stock
    if description is not None:
        data["description"] = description
    if not data:
        return None
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

# Rotinas.
def insert_routine(user_id: str, medicine_id: str, time: str, days_of_week: str = "Todos"):
    """Insere uma nova rotina."""
    data = {
        "user_id": user_id,
        "medicine_id": medicine_id,
        "time": time,
        "days_of_week": days_of_week,
        "fl_active": True
    }
    try:
        result = supabase.table("routines").insert(data).execute()
        return result.data[0] if result.data else None # Retorna a rotina criada.
    except Exception as e:
        print(f"Erro ao inserir rotina: {e}")
        return None

def get_routines_by_user(user_id: str):
    """Retorna todas as rotinas ativas de um usuário."""
    result = supabase.table("routines").select("*").eq("user_id", user_id).eq("fl_active", True).execute()
    return result.data if result.data else [] # Retorna a lista de rotinas ou uma lista vazia.

def get_routine_by_id(routine_id: str, user_id: str):
    """ Retorna uma rotina específica pelo ID e usuário."""
    result = supabase.table("routines").select("*").eq("id", routine_id).eq("user_id", user_id).eq("fl_active", True).execute()
    return result.data[0] if result.data else None # Retorna a rotina ou None.

def update_routine(routine_id: str, user_id: str, time: str = None, days_of_week: str = None):
    """Atualiza uma rotina existente."""
    data = {}
    if time is not None:
        data["time"] = time
    if days_of_week is not None:
        data["days_of_week"] = days_of_week
    if not data:
        return None
    try:
        result = (supabase.table("routines").update(data).eq("id", routine_id).eq("user_id", user_id).eq("fl_active", True).execute())
        return result.data[0] if result.data else None
    except Exception as e:
        print(f"Erro ao atualizar rotina: {e}")
        return None

def delete_routine(routine_id: str, user_id: str):
    """Deleta uma rotina e todos seus dados (soft delete)."""
    try:
        result = (supabase.table("routines").update({"fl_active": False}).eq("id", routine_id).eq("user_id", user_id).eq("fl_active", True).execute())
        return result.data[0] if result.data else None
    except Exception as e:
        print(f"Erro ao deletar rotina: {e}")
        return None

# Histórico.
def insert_history(user_id: str, routine_id: str, fl_taken: bool, dt_hour: str = None):
    """Insere um registro no histórico de uma rotina."""
    data = {
        "user_id": user_id,
        "routine_id": routine_id,
        "fl_taken": fl_taken,
    }
    if dt_hour is not None:
        data["dt_hour"] = dt_hour
    try:
        result = supabase.table("history").insert(data).execute()
        return result.data[0] if result.data else None # Retorna o registro criado.
    except Exception as e:
        print(f"Erro ao inserir histórico: {e}")
        return None

def get_history_by_user(user_id: str):
    """Retorna todo o histórico de um usuário."""
    result = supabase.table("history").select("*").eq("user_id", user_id).order("dt_hour", desc=True).execute()
    return result.data if result.data else [] # Retorna a lista de históricos.

def get_history_by_id(history_id: str, user_id: str):
    """Retorna um registro específico do histórico."""
    result = supabase.table("history").select("*").eq("id", history_id).eq("user_id", user_id).execute()
    return result.data[0] if result.data else None # Retorna o registro ou None.
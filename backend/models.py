from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime, time as Time

# Usuários.
class UserCreate(BaseModel):
    """Dados para criar um novo usuário."""
    name: str # Nome (obrigatório).
    email: EmailStr # Email (obrigatório e validado).
    phone: str # Telefone (obrigatório).
    password: str # Senha (obrigatório).
    dt_birth: date # Data de nascimento (obrigatório).
    blood_type: Optional[str] = None # Tipo sanguíneo (opcional).
    emergency_contact_name: Optional[str] = None # Nome do contato de emergência (opcional).
    emergency_contact_phone: Optional[str] = None # Telefone do contato de emergência (opcional).
    allergies: Optional[str] = None # Alergias (opcional).
    chronic_conditions: Optional[str] = None # Condições crônicas (opcional).

class UserLogin(BaseModel):
    """Dados para fazer login."""
    email: EmailStr # Email (obrigatório e validado).
    password: str # Senha (obrigatório).

class UserUpdate(BaseModel):
    """Dados para atualizar o usuário."""
    name: Optional[str] = None # Nome.
    email: Optional[EmailStr] = None # Email.
    phone: Optional[str] = None # Telefone.
    password: Optional[str] = None # Senha.
    dt_birth: Optional[date] = None # Data de nascimento.
    blood_type: Optional[str] = None # Tipo sanguíneo.
    emergency_contact_name: Optional[str] = None # Nome do contato de emergência.
    emergency_contact_phone: Optional[str] = None # Telefone do contato de emergência.
    allergies: Optional[str] = None # Alergias.
    chronic_conditions: Optional[str] = None # Condições crônicas.
    
class UserResponse(BaseModel):
    """Dados retornados do usuário (sem senha)"""
    id: str # ID do usuário.
    name: str # Nome.
    email: str # Email.
    phone: str # Telefone.
    dt_birth: date # Data de nascimento.
    blood_type: Optional[str] = None # Tipo sanguíneo.
    emergency_contact_name: Optional[str] = None # Nome do contato de emergência.
    emergency_contact_phone: Optional[str] = None # Telefone do contato de emergência.
    allergies: Optional[str] = None # Alergias.
    chronic_conditions: Optional[str] = None # Condições crônicas.
    fl_active: bool # Indica se o usuário está ativo.
    dt_created: datetime # Data de criação.
    dt_updated: datetime # Data de atualização.

# Medicamentos.
class MedicineCreate(BaseModel):
    """Dados para criar um medicamento."""
    name: str # Nome (obrigatório). 
    dosage: str # Dosagem (obrigatório).
    quantity: int # Quantidade (obrigatório).
    usage_type: Optional[str] = None # Tipo de uso (opcional).
    usage_instructions: Optional[str] = None # Instruções de uso (opcional).
    stock: int = 0 # Estoque (padrão: 0).
    description: Optional[str] = None # Descrição (opcional).

class MedicineUpdate(BaseModel):
    """Dados para atualizar um medicamento."""
    name: Optional[str] = None # Nome (opcional).
    dosage: Optional[str] = None # Dosagem (opcional).
    quantity: Optional[int] = None # Quantidade (opcional).
    usage_type: Optional[str] = None # Tipo de uso (opcional).
    usage_instructions: Optional[str] = None # Instruções de uso (opcional).
    stock: Optional[int] = None # Estoque (opcional).
    description: Optional[str] = None # Descrição (opcional).

class MedicineResponse(BaseModel):
    """Medicamento retornado."""
    id: str # ID do medicamento.
    user_id: str # ID do usuário (dono do medicamento).
    name: str # Nome.
    dosage: str # Dosagem (pode ser None).
    quantity: int # Quantidade (pode ser None).
    usage_type: Optional[str] = None # Tipo de uso (pode ser None).
    usage_instructions: Optional[str] = None # Instruções de uso (pode ser None).
    stock: int # Estoque (pode ser None).
    description: Optional[str] # Descrição (pode ser None).
    fl_active: bool # Indica se o medicamento está ativo.
    dt_created: datetime # Data de criação.
    dt_updated: datetime # Data de atualização.

# Rotinas.
class RoutineCreate(BaseModel):
    """Dados para criar uma rotina."""
    medicine_id: str # ID do medicamento.
    time: Time # Horário  - Formato HH:MM.
    days_of_week: str = "Todos" # Dias da semana.

class RoutineUpdate(BaseModel):
    """Dados para atualizar uma rotina."""
    time: Optional[Time] = None # Mudar horário (opcional).
    days_of_week: Optional[str] = None # Mudar dias da semana (opcional).

class RoutineResponse(BaseModel):
    """Rotina retornada"""
    id: str # ID da rotina.
    medicine_id: str # ID do medicamento.
    user_id: str # ID do usuário (dono da rotina).
    time: Time # Horário.
    days_of_week: str # Dias da semana.
    fl_active: bool # Indica se a rotina está ativa.
    dt_created: datetime # Data de criação.
    dt_updated: datetime # Data de atualização.

# Histórico.
class HistoryCreate(BaseModel):
    """Dados para registrar se tomou medicamento."""
    routine_id: str # ID da rotina.
    fl_taken: bool  # True = tomou, False = não tomou.
    dt_hour: Optional[datetime] = None # Data e hora.

class HistoryResponse(BaseModel):
    """Histórico retornado."""
    id: str # ID do histórico.
    routine_id: str # ID da rotina.
    user_id: str # ID do usuário (dono do histórico).
    dt_hour: datetime # Data e hora.
    fl_taken: bool # Indica se o medicamento foi tomado.
    dt_created: datetime # Data de criação.

# Autenticação.
class TokenResponse(BaseModel):
    """Token retornado após login."""
    access_token: str # Token de acesso (JWT).
    token_type: str = "bearer" # Tipo do token (padrão: "bearer").
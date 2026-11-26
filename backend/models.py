from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional
from datetime import date, datetime, time as Time
from typing import Literal
import re

def normalize_days_of_week(value: str) -> str:
    """Padroniza os dias aceitos pelo agendador."""
    value = value.strip().lower()
    if value == "todos":
        return "Todos"
    days = [day.strip() for day in value.split(",")]
    valid_days = {"seg", "ter", "qua", "qui", "sex", "sab", "dom"}
    if not days or any(day not in valid_days for day in days) or len(days) != len(set(days)):
        raise ValueError("Use Todos ou dias separados por vírgula: seg,ter,qua,qui,sex,sab,dom.")
    return ",".join(days)

class ReminderPreferencesUpdate(BaseModel):
    """Canal e número para lembretes, com consentimento explícito."""
    channel: Literal["sms"]
    phone: str
    consent: Literal[True]

    @validator("phone")
    def validate_reminder_phone(cls, value):
        if not re.fullmatch(r"\+[1-9][0-9]{7,14}", value):
            raise ValueError("Use o formato internacional E.164, por exemplo +5511999999999.")
        return value

class ReminderPreferencesResponse(BaseModel):
    enabled: bool
    channel: Optional[Literal["sms", "whatsapp"]] = None
    phone: Optional[str] = None
    consent_at: Optional[datetime] = None

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
    
    @validator('phone')
    def validate_phone(cls, v):
        """Validar que telefone contém apenas números e caracteres válidos (+, -, espaço)."""
        cleaned = v.replace('+', '').replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
        if not cleaned.isdigit():
            raise ValueError('Telefone deve conter apenas números e caracteres válidos (+, -, parênteses)')
        return v

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
    quantity: int = Field(..., gt=0) # Quantidade (obrigatório e deve ser > 0).
    usage_type: Optional[str] = None # Tipo de uso (opcional).
    usage_instructions: Optional[str] = None # Instruções de uso (opcional).
    stock: int = Field(default=0, ge=0) # Estoque (padrão: 0, deve ser >= 0).
    description: Optional[str] = None # Descrição (opcional).
    stock_limit: int = Field(default=5, ge=0) # Limite de estoque para alertas (padrão: 5, deve ser >= 0).
    notification_enabled: bool = True # Habilitar notificações de baixo estoque (padrão: True).

class MedicineUpdate(BaseModel):
    """Dados para atualizar um medicamento."""
    name: Optional[str] = None # Nome (opcional).
    dosage: Optional[str] = None # Dosagem (opcional).
    quantity: Optional[int] = Field(None, gt=0) # Quantidade (opcional, deve ser > 0 se informado).
    usage_type: Optional[str] = None # Tipo de uso (opcional).
    usage_instructions: Optional[str] = None # Instruções de uso (opcional).
    stock: Optional[int] = Field(None, ge=0) # Estoque (opcional, deve ser >= 0 se informado).
    description: Optional[str] = None # Descrição (opcional).
    stock_limit: Optional[int] = Field(None, ge=0) # Limite de estoque (opcional, deve ser >= 0 se informado).
    notification_enabled: Optional[bool] = None # Habilitar/desabilitar notificações (opcional).

class MedicineResponse(BaseModel):
    """Medicamento retornado."""
    id: str # ID do medicamento.
    user_id: str # ID do usuário (dono do medicamento).
    name: str # Nome.
    dosage: str # Dosagem.
    quantity: int # Quantidade.
    usage_type: Optional[str] = None # Tipo de uso.
    usage_instructions: Optional[str] = None # Instruções de uso.
    stock: int # Estoque.
    description: Optional[str] # Descrição.
    stock_limit: int # Limite de estoque para alertas.
    notification_enabled: bool # Se notificações estão habilitadas.
    fl_active: bool # Indica se o medicamento está ativo.
    dt_created: datetime # Data de criação.
    dt_updated: datetime # Data de atualização.

# Rotinas.
class RoutineCreate(BaseModel):
    """Dados para criar uma rotina."""
    medicine_id: str # ID do medicamento.
    time: Time # Horário  - Formato HH:MM.
    days_of_week: str = "Todos" # Dias da semana.

    _normalize_days = validator("days_of_week", allow_reuse=True)(normalize_days_of_week)

class RoutineUpdate(BaseModel):
    """Dados para atualizar uma rotina."""
    time: Optional[Time] = None # Mudar horário (opcional).
    days_of_week: Optional[str] = None # Mudar dias da semana (opcional).

    @validator("days_of_week")
    def validate_days(cls, value):
        return normalize_days_of_week(value) if value is not None else value

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
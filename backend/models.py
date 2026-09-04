from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Usuários.
class UserCreate(BaseModel):
    """Dados para criar um novo usuário."""
    email: EmailStr # Email (obrigatório e validado).
    password: str # Senha (obrigatório).
    name: Optional[str] = None # Nome (opcional).

class UserLogin(BaseModel):
    """Dados para fazer login."""
    email: EmailStr # Email (obrigatório e validado).
    password: str # Senha (obrigatório).

class UserResponse(BaseModel):
    """Dados retornados do usuário (sem senha)"""
    id: str # ID do usuário.
    email: str # Email.
    name: Optional[str] # Nome.
    dt_created: datetime # Data de criação.

# Medicamentos.
class MedicineCreate(BaseModel):
    """Dados para criar um medicamento."""
    name: str # Nome (obrigatório). 
    dosage: Optional[str] = None # Dosagem (opcional).
    description: Optional[str] = None # Descrição (opcional).

class MedicineUpdate(BaseModel):
    """Dados para atualizar um medicamento."""
    name: Optional[str] = None # Nome (opcional).
    dosage: Optional[str] = None # Dosagem (opcional).
    description: Optional[str] = None # Descrição (opcional).

class MedicineResponse(BaseModel):
    """Medicamento retornado."""
    id: str # ID do medicamento.
    user_id: str # ID do usuário (dono do medicamento).
    name: str # Nome.
    dosage: Optional[str] # Dosagem (pode ser None).
    description: Optional[str] # Descrição (pode ser None).
    fl_active: bool # Indica se o medicamento está ativo.
    dt_created: datetime # Data de criação.

# Rotinas.
class RoutineCreate(BaseModel):
    """Dados para criar uma rotina."""
    medicine_id: str # ID do medicamento (obrigatório).
    time: str  # Horário (obrigatório) - Formato HH:MM.
    days_of_week: Optional[str] = None  # Dias da semana (opcional).

class RoutineUpdate(BaseModel):
    """Dados para atualizar uma rotina."""
    time: Optional[str] = None # Mudar horário (opcional).
    days_of_week: Optional[str] = None # Mudar dias da semana (opcional).

class RoutineResponse(BaseModel):
    """Rotina retornada"""
    id: str # ID da rotina.
    medicine_id: str # ID do medicamento.
    user_id: str # ID do usuário (dono da rotina).
    time: str # Horário.
    days_of_week: Optional[str] # Dias da semana.
    fl_active: bool # Indica se a rotina está ativa.
    dt_created: datetime # Data de criação.

# Histórico.
class HistoryCreate(BaseModel):
    """Dados para registrar se tomou medicamento."""
    routine_id: str # ID da rotina.
    fl_taken: bool  # True = tomou, False = não tomou.

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
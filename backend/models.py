from datetime import date, datetime, time
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


# Usuários.
class UserCreate(BaseModel):
    """Dados para criar um novo usuário."""

    name: str
    email: EmailStr
    phone: str
    password: str
    dt_birth: date
    blood_type: Optional[str] = None
    emergency_contact_name: Optional[str] = None
    emergency_contact_phone: Optional[str] = None
    allergies: Optional[str] = None
    chronic_conditions: Optional[str] = None


class UserLogin(BaseModel):
    """Dados para fazer login."""

    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    """Dados para atualizar o usuário."""

    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    password: Optional[str] = None
    dt_birth: Optional[date] = None
    blood_type: Optional[str] = None
    emergency_contact_name: Optional[str] = None
    emergency_contact_phone: Optional[str] = None
    allergies: Optional[str] = None
    chronic_conditions: Optional[str] = None


class UserResponse(BaseModel):
    """Dados públicos retornados do usuário."""

    id: str
    name: str
    email: EmailStr
    phone: str
    dt_birth: date
    blood_type: Optional[str] = None
    emergency_contact_name: Optional[str] = None
    emergency_contact_phone: Optional[str] = None
    allergies: Optional[str] = None
    chronic_conditions: Optional[str] = None
    fl_active: bool
    dt_created: datetime
    dt_updated: datetime


# Medicamentos.
class MedicineCreate(BaseModel):
    """Dados para criar um medicamento."""

    name: str
    dosage: str
    quantity: int = Field(..., ge=1)
    usage_type: Optional[str] = None
    usage_instructions: Optional[str] = None
    stock: int = Field(default=0, ge=0)
    description: Optional[str] = None


class MedicineUpdate(BaseModel):
    """Dados para atualizar um medicamento."""

    name: Optional[str] = None
    dosage: Optional[str] = None
    quantity: Optional[int] = Field(default=None, ge=1)
    usage_type: Optional[str] = None
    usage_instructions: Optional[str] = None
    stock: Optional[int] = Field(default=None, ge=0)
    description: Optional[str] = None


class MedicineResponse(BaseModel):
    """Medicamento retornado."""

    id: str
    user_id: str
    name: str
    dosage: str
    quantity: int
    usage_type: Optional[str] = None
    usage_instructions: Optional[str] = None
    stock: int
    description: Optional[str] = None
    fl_active: bool
    dt_created: datetime
    dt_updated: datetime


# Rotinas.
class RoutineCreate(BaseModel):
    """Dados para criar uma rotina."""

    medicine_id: str
    time: time
    days_of_week: Optional[str] = None


class RoutineUpdate(BaseModel):
    """Dados para atualizar uma rotina."""

    medicine_id: Optional[str] = None
    time: Optional[time] = None
    days_of_week: Optional[str] = None
    fl_active: Optional[bool] = None


class RoutineResponse(BaseModel):
    """Rotina retornada."""

    id: str
    user_id: str
    medicine_id: str
    time: time
    days_of_week: Optional[str] = None
    fl_active: bool
    dt_created: datetime
    dt_updated: datetime


# Histórico.
class HistoryCreate(BaseModel):
    """Dados para registrar se tomou medicamento."""

    routine_id: str
    fl_taken: bool


class HistoryResponse(BaseModel):
    """Histórico retornado."""

    id: str
    routine_id: str
    user_id: str
    dt_hour: datetime
    fl_taken: bool
    dt_created: datetime


# Autenticação.
class TokenResponse(BaseModel):
    """Token retornado após login."""

    access_token: str
    token_type: str = "bearer"

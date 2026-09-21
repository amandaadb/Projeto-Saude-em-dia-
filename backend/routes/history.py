from typing import List
from fastapi import APIRouter, Depends, HTTPException
from database import get_history_by_user, get_history_by_id, insert_history, get_routine_by_id
from models import HistoryCreate, HistoryResponse
from routes.auth import get_current_user

router = APIRouter()

@router.get("",response_model=List[HistoryResponse], tags=["History"])
def list_history(user_id: str = Depends(get_current_user)):
    """Lista o histórico do usuário autenticado."""
    return get_history_by_user(user_id)

@router.post("",response_model=HistoryResponse,tags=["History"])
def create_history(history: HistoryCreate,user_id: str = Depends(get_current_user)):
    """Registra se o usuário tomou ou não o medicamento."""
    routine = get_routine_by_id(
        routine_id=history.routine_id,
        user_id=user_id
    )
    if not routine:
        raise HTTPException(
            status_code=404,
            detail="Rotina não encontrada."
        )
    new_history = insert_history(
        routine_id=history.routine_id,
        user_id=user_id,
        fl_taken=history.fl_taken,
        dt_hour=(
            history.dt_hour.isoformat()
            if history.dt_hour is not None
            else None
        )
    )
    if not new_history:
        raise HTTPException(
            status_code=500,
            detail="Erro ao registrar histórico."
        )
    return new_history

@router.get("/{history_id}",response_model=HistoryResponse,tags=["History"])
def get_history(history_id: str, user_id: str = Depends(get_current_user)):
    """Retorna um registro específico do histórico."""
    history = get_history_by_id(
        history_id=history_id,
        user_id=user_id
    )
    if not history:
        raise HTTPException(
            status_code=404,
            detail="Registro de histórico não encontrado."
        )
    return history
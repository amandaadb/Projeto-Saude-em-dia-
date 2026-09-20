from typing import List
from fastapi import APIRouter, Depends, HTTPException
from database import insert_routine, get_routines_by_user, get_routine_by_id, update_routine as update_routine_db, delete_routine as delete_routine_db, get_medicine_by_id
from models import RoutineCreate, RoutineUpdate, RoutineResponse
from routes.auth import get_current_user

router = APIRouter()

@router.get("", response_model=List[RoutineResponse], tags=["Routines"])
def list_routines(user_id: str = Depends(get_current_user)):
    """Lista todas as rotinas ativas do usuário."""
    return get_routines_by_user(user_id)

@router.post("", response_model=RoutineResponse, tags=["Routines"])
def create_routine(routine: RoutineCreate, user_id: str = Depends(get_current_user)):
    """Cria uma rotina para um medicamento do usuário."""
    medicine = get_medicine_by_id(
        medicine_id=routine.medicine_id,
        user_id=user_id
    )
    if not medicine:
        raise HTTPException(
            status_code=404,
            detail="Medicamento não encontrado."
        )
    new_routine = insert_routine(
        user_id=user_id,
        medicine_id=routine.medicine_id,
        time=routine.time.isoformat(),
        days_of_week=routine.days_of_week
    )
    if not new_routine:
        raise HTTPException(
            status_code=500,
            detail="Erro ao criar rotina."
        )
    return new_routine

@router.get(
    "/{routine_id}",
    response_model=RoutineResponse,
    tags=["Routines"]
)
def get_routine(routine_id: str, user_id: str = Depends(get_current_user)):
    """Retorna uma rotina específica."""
    routine = get_routine_by_id(
        routine_id=routine_id,
        user_id=user_id
    )
    if not routine:
        raise HTTPException(
            status_code=404,
            detail="Rotina não encontrada."
        )
    return routine

@router.put(
    "/{routine_id}",
    response_model=RoutineResponse,
    tags=["Routines"]
)
def update_routine(routine_id: str, routine: RoutineUpdate, user_id: str = Depends(get_current_user)):
    """Atualiza uma rotina."""
    existing_routine = get_routine_by_id(
        routine_id=routine_id,
        user_id=user_id
    )
    if not existing_routine:
        raise HTTPException(
            status_code=404,
            detail="Rotina não encontrada."
        )
    updated_routine = update_routine_db(
        routine_id=routine_id,
        user_id=user_id,
        time=(
            routine.time.isoformat()
            if routine.time is not None
            else None
        ),
        days_of_week=routine.days_of_week
    )

    if not updated_routine:
        raise HTTPException(
            status_code=500,
            detail="Erro ao atualizar rotina."
        )
    return updated_routine

@router.delete("/{routine_id}", tags=["Routines"])
def delete_routine(routine_id: str, user_id: str = Depends(get_current_user)):
    """Desativa uma rotina."""
    existing_routine = get_routine_by_id(
        routine_id=routine_id,
        user_id=user_id
    )
    if not existing_routine:
        raise HTTPException(
            status_code=404,
            detail="Rotina não encontrada."
        )
    deleted_routine = delete_routine_db(
        routine_id=routine_id,
        user_id=user_id
    )
    if not deleted_routine:
        raise HTTPException(
            status_code=500,
            detail="Erro ao desativar rotina."
        )
    return {"mensagem": "Rotina desativada com sucesso."}
from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List
from database import insert_medicine, get_medicines_by_user, get_medicine_by_id, update_medicine as update_medicine_db, delete_medicine as delete_medicine_db
from models import MedicineCreate, MedicineUpdate, MedicineResponse
from routes.auth import get_current_user

router = APIRouter()

@router.get("", response_model=List[MedicineResponse], tags=["Medicines"])
def list_medicines(user_id: str = Depends(get_current_user)):
    """Lista todos os medicamentos ativos do usuário."""
    return get_medicines_by_user(user_id)

@router.post("", response_model=MedicineResponse, tags=["Medicines"])
def create_medicine(medicine: MedicineCreate, user_id: str = Depends(get_current_user)):
    """Cria um novo medicamento."""
    # Verifica se já existe medicamento com mesmo nome e dosagem.
    medicines = get_medicines_by_user(user_id)
    for existing in medicines:
        if (existing["name"] == medicine.name and existing.get("dosage") == medicine.dosage):
            raise HTTPException(status_code=400, detail="Medicamento já existe.")
    # Insere medicamento.
    new_medicine = insert_medicine(
        user_id=user_id,
        name=medicine.name,
        dosage=medicine.dosage,
        quantity=medicine.quantity,
        usage_type=medicine.usage_type,
        usage_instructions=medicine.usage_instructions,
        stock=medicine.stock,
        description=medicine.description,
        stock_limit=medicine.stock_limit,
        notification_enabled=medicine.notification_enabled
    )

    if not new_medicine:
        raise HTTPException(status_code=500, detail="Erro ao criar medicamento.")
    return new_medicine

@router.get("/{medicine_id}", response_model=MedicineResponse, tags=["Medicines"])
def get_medicine(medicine_id: str, user_id: str = Depends(get_current_user)):
    """Retorna um medicamento específico."""
    medicine = get_medicine_by_id(medicine_id=medicine_id, user_id=user_id)
    if not medicine:
        raise HTTPException(status_code=404, detail="Medicamento não encontrado.")
    return medicine

@router.put("/{medicine_id}", response_model=MedicineResponse, tags=["Medicines"])
def update_medicine(medicine_id: str, medicine: MedicineUpdate, user_id: str = Depends(get_current_user)):
    """Atualiza um medicamento."""
    # Busca medicamento.
    existing_medicine = get_medicine_by_id(
        medicine_id=medicine_id, 
        user_id=user_id
    )
    if not existing_medicine:
        raise HTTPException(status_code=404, detail="Medicamento não encontrado.")
    # Verifica quais campos foram enviados.
    name = medicine.name if medicine.name is not None else existing_medicine["name"]
    dosage = medicine.dosage if medicine.dosage is not None else existing_medicine["dosage"]
    quantity = medicine.quantity if medicine.quantity is not None else existing_medicine["quantity"]
    usage_type = medicine.usage_type if medicine.usage_type is not None else existing_medicine["usage_type"]
    usage_instructions = medicine.usage_instructions if medicine.usage_instructions is not None else existing_medicine["usage_instructions"]
    stock = medicine.stock if medicine.stock is not None else existing_medicine["stock"]
    description = medicine.description if medicine.description is not None else existing_medicine["description"]
    stock_limit = medicine.stock_limit if medicine.stock_limit is not None else existing_medicine["stock_limit"]
    notification_enabled = medicine.notification_enabled if medicine.notification_enabled is not None else existing_medicine["notification_enabled"]
    
    # 🔍 PASSO 3: Atualiza medicamento.
    updated_medicine = update_medicine_db(
        medicine_id=medicine_id,
        user_id=user_id,
        name=name,
        dosage=dosage,
        quantity=quantity,
        usage_type=usage_type,
        usage_instructions=usage_instructions,
        stock=stock,
        description=description,
        stock_limit=stock_limit,
        notification_enabled=notification_enabled
    )
    if not updated_medicine:
        raise HTTPException(status_code=500, detail="Erro ao atualizar medicamento.")
    return updated_medicine

@router.delete("/{medicine_id}", tags=["Medicines"])
def delete_medicine(medicine_id: str, user_id: str = Depends(get_current_user)):
    """Deleta um medicamento através de soft delete (também desativa suas rotinas)."""
    # Verifica se medicamento existe.
    existing_medicine = get_medicine_by_id(medicine_id=medicine_id, user_id=user_id)

    if not existing_medicine:
        raise HTTPException(status_code=404, detail="Medicamento não encontrado.")
    
    # 🔍 PASSO 2: Realiza soft delete (que também desativa as rotinas).
    deleted_medicine = delete_medicine_db(
        medicine_id=medicine_id,
        user_id=user_id
    )
    if not deleted_medicine:
        raise HTTPException(status_code=500, detail="Erro ao deletar medicamento.")
    return {"mensagem": "Medicamento deletado com sucesso."}


@router.patch("/{medicine_id}/notifications", response_model=MedicineResponse, tags=["Medicines"])
def update_notifications(medicine_id: str, notification_enabled: bool = Query(..., description="True para habilitar, False para desabilitar"), user_id: str = Depends(get_current_user)):
    """
    Habilita ou desabilita notificações para um medicamento.
    
    Parâmetros:
    - medicine_id: ID do medicamento
    - notification_enabled: True para habilitar, False para desabilitar
    
    Exemplo de uso:
    PATCH /api/medicines/{medicine_id}/notifications?notification_enabled=false
    """
    # 🔍 PASSO 1: Busca medicamento.
    existing_medicine = get_medicine_by_id(
        medicine_id=medicine_id,
        user_id=user_id
    )
    
    if not existing_medicine:
        raise HTTPException(status_code=404, detail="Medicamento não encontrado.")
    
    # 🔍 PASSO 2: Atualiza preferência de notificação.
    updated_medicine = update_medicine_db(
        medicine_id=medicine_id,
        user_id=user_id,
        notification_enabled=notification_enabled
    )
    
    if not updated_medicine:
        raise HTTPException(status_code=500, detail="Erro ao atualizar notificações.")
    
    return updated_medicine


@router.patch("/{medicine_id}/stock-limit", response_model=MedicineResponse, tags=["Medicines"])
def update_stock_limit(medicine_id: str, stock_limit: int = Query(..., ge=0, description="Quantidade mínima para disparar notificação (>= 0)"), user_id: str = Depends(get_current_user)):
    """
    Atualiza o limite de estoque para notificações.
    
    Parâmetros:
    - medicine_id: ID do medicamento
    - stock_limit: Quantidade mínima para disparar notificação (>= 0)
    
    Exemplo de uso:
    PATCH /api/medicines/{medicine_id}/stock-limit?stock_limit=10
    """
    # 🔍 PASSO 1: Busca medicamento.
    existing_medicine = get_medicine_by_id(
        medicine_id=medicine_id,
        user_id=user_id
    )
    
    if not existing_medicine:
        raise HTTPException(status_code=404, detail="Medicamento não encontrado.")
    
    # 🔍 PASSO 2: Atualiza limite de estoque.
    updated_medicine = update_medicine_db(
        medicine_id=medicine_id,
        user_id=user_id,
        stock_limit=stock_limit
    )
    
    if not updated_medicine:
        raise HTTPException(status_code=500, detail="Erro ao atualizar limite de estoque.")
    
    return updated_medicine
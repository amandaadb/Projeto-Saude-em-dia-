from fastapi import APIRouter, HTTPException, Depends
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
        description=medicine.description
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
    # Atualiza medicamento.
    updated_medicine = update_medicine_db(
        medicine_id=medicine_id,
        user_id=user_id,
        name=name,
        dosage=dosage,
        quantity=quantity,
        usage_type=usage_type,
        usage_instructions=usage_instructions,
        stock=stock,
        description=description
    )
    if not updated_medicine:
        raise HTTPException(status_code=500, detail="Erro ao atualizar medicamento.")
    return updated_medicine

@router.delete("/{medicine_id}", tags=["Medicines"])
def delete_medicine(medicine_id: str, user_id: str = Depends(get_current_user)):
    """Deleta um medicamento através de soft delete."""
    # Verifica se medicamento existe.
    existing_medicine = get_medicine_by_id(medicine_id=medicine_id, user_id=user_id)

    if not existing_medicine:
        raise HTTPException(status_code=404, detail="Medicamento não encontrado.")
    # Realiza soft delete.
    deleted_medicine = delete_medicine_db(
        medicine_id=medicine_id,
        user_id=user_id
    )
    if not deleted_medicine:
        raise HTTPException(status_code=500, detail="Erro ao deletar medicamento.")
    return {"mensagem": "Medicamento deletado com sucesso."}
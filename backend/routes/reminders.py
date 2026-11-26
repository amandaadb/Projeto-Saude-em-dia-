from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException

from database import get_user_by_id, supabase
from models import ReminderPreferencesResponse, ReminderPreferencesUpdate
from routes.auth import get_current_user

router = APIRouter()


@router.get("", response_model=ReminderPreferencesResponse, tags=["Reminders"])
def get_preferences(user_id: str = Depends(get_current_user)):
    """Consulta as preferências de lembretes do usuário."""
    if not get_user_by_id(user_id):
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    result = supabase.table("reminder_preferences").select("enabled,channel,phone,consent_at").eq("user_id", user_id).execute()
    return result.data[0] if result.data else {"enabled": False}


@router.put("", response_model=ReminderPreferencesResponse, tags=["Reminders"])
def enable_reminders(preferences: ReminderPreferencesUpdate, user_id: str = Depends(get_current_user)):
    """Ativa lembretes por SMS com consentimento separado do cadastro."""
    if not get_user_by_id(user_id):
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    data = {
        "user_id": user_id,
        "enabled": True,
        "channel": preferences.channel,
        "phone": preferences.phone,
        "consent_at": datetime.now(timezone.utc).isoformat(),
    }
    result = supabase.table("reminder_preferences").upsert(data, on_conflict="user_id").execute()
    if not result.data:
        raise HTTPException(status_code=500, detail="Erro ao salvar preferências de lembrete.")
    return result.data[0]


@router.delete("", response_model=ReminderPreferencesResponse, tags=["Reminders"])
def disable_reminders(user_id: str = Depends(get_current_user)):
    """Revoga o consentimento para novos lembretes."""
    if not get_user_by_id(user_id):
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    result = supabase.table("reminder_preferences").update({"enabled": False}).eq("user_id", user_id).execute()
    return result.data[0] if result.data else {"enabled": False}

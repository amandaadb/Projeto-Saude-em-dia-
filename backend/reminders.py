
import logging
from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo

from apscheduler.schedulers.background import BackgroundScheduler
from httpx import HTTPError
from postgrest.exceptions import APIError
from requests.exceptions import RequestException
from twilio.base.exceptions import TwilioRestException
from twilio.http.http_client import TwilioHttpClient
from twilio.rest import Client

from config import settings
from database import supabase
from models import normalize_days_of_week

logger = logging.getLogger(__name__)
TIMEZONE = ZoneInfo("America/Sao_Paulo")
DAYS = ("seg", "ter", "qua", "qui", "sex", "sab", "dom")
TEXTS = {
    "dose": "MedControl: voce tem um lembrete. Acesse o aplicativo para consultar.",
    "stock": "MedControl: voce tem um aviso de estoque. Acesse o aplicativo para consultar.",
}


def pages(table, columns, **filters):
    """Lê todas as páginas, inclusive quando o Supabase limita o tamanho da resposta."""
    key = "user_id" if table == "reminder_preferences" else "id"
    last_id = None
    while True:
        query = supabase.table(table).select(columns)
        for column, value in filters.items():
            query = query.eq(column, value)
        if last_id is not None:
            query = query.gt(key, last_id)
        result = query.order(key).limit(500).execute()
        if not result.data:
            break
        yield from result.data
        last_id = result.data[-1][key]


def due_dates(routine, now):
    days = normalize_days_of_week(routine["days_of_week"])
    scheduled = time.fromisoformat(routine["time"])
    dates = (now.date() - timedelta(days=1), now.date())
    for day in dates:
        if days != "Todos" and DAYS[day.weekday()] not in days.split(","):
            continue
        due_at = datetime.combine(day, time(scheduled.hour, scheduled.minute), tzinfo=TIMEZONE)
        if timedelta(0) <= now - due_at <= timedelta(minutes=15):
            yield day


def set_status(attempt_id, status, provider_id=None):
    result = supabase.table("reminder_attempts").update({
        "status": status, "provider_id": provider_id
    }).eq("id", attempt_id).execute()
    if not result.data:
        raise RuntimeError("Não foi possível atualizar o registro da tentativa de lembrete.")


def send_reminder(client, preference, attempt_id, kind):
    if preference["channel"] != "sms":
        logger.error("Canal não suportado na tentativa %s; envio cancelado.", attempt_id)
        set_status(attempt_id, "cancelled")
        return
    # Confere novamente o consentimento e o número antes da chamada ao provedor.
    current = supabase.table("reminder_preferences").select("enabled,channel,phone,consent_at").eq(
        "user_id", preference["user_id"]
    ).execute()
    user = supabase.table("users").select("fl_active").eq("id", preference["user_id"]).execute()
    if not current.data or not user.data or not user.data[0]["fl_active"] or any(
        current.data[0][key] != preference[key] for key in ("enabled", "channel", "phone", "consent_at")
    ):
        set_status(attempt_id, "cancelled")
        return

    try:
        message = client.messages.create(
            from_=settings.TWILIO_SMS_FROM,
            to=preference["phone"],
            body="sms_appointment_reminders" if settings.TWILIO_TRIAL_MODE else TEXTS[kind],
        )
    except TwilioRestException as exc:
        status = "unknown" if exc.status >= 500 or exc.status in (408, 409) else "failed"
        logger.error("Erro Twilio na tentativa %s: HTTP %s, código %s.", attempt_id, exc.status, exc.code)
        set_status(attempt_id, status)
        return
    except RequestException:
        logger.error("Resultado da tentativa %s desconhecido por erro de comunicação.", attempt_id)
        set_status(attempt_id, "unknown")
        return
    set_status(attempt_id, "accepted", message.sid)


def process_user_reminders(client, preference, now=None):
    user_id = preference["user_id"]
    for medicine in pages("medicines", "id,stock,stock_limit", user_id=user_id, fl_active=True, notification_enabled=True):
        if medicine["stock"] <= medicine["stock_limit"]:
            attempt = supabase.rpc("claim_stock_reminder", {
                "p_medicine_id": medicine["id"], "p_user_id": user_id
            }).execute().data
            if attempt:
                send_reminder(client, preference, attempt, "stock")

    for routine in pages("routines", "id,time,days_of_week", user_id=user_id, fl_active=True):
        try:
            dates = list(due_dates(routine, now or datetime.now(TIMEZONE)))
        except ValueError:
            logger.error("Rotina %s tem horário ou dias inválidos; lembrete ignorado.", routine["id"])
            continue
        for day in dates:
            attempt = supabase.rpc("claim_dose_reminder", {
                "p_routine_id": routine["id"], "p_user_id": user_id,
                "p_date": day.isoformat(), "p_time": routine["time"],
                "p_days": routine["days_of_week"]
            }).execute().data
            if attempt:
                send_reminder(client, preference, attempt, "dose")


def process_reminders(client, now=None):
    for preference in pages("reminder_preferences", "user_id,enabled,channel,phone,consent_at", enabled=True, channel="sms"):
        try:
            process_user_reminders(client, preference, now)
        except (APIError, HTTPError, RuntimeError):
            logger.exception("Erro ao processar lembretes do usuário %s.", preference["user_id"])


def start_reminder_scheduler():
    required = {
        "TWILIO_ACCOUNT_SID": settings.TWILIO_ACCOUNT_SID,
        "TWILIO_AUTH_TOKEN": settings.TWILIO_AUTH_TOKEN,
        "TWILIO_SMS_FROM": settings.TWILIO_SMS_FROM,
    }
    missing = [key for key, value in required.items() if not value]
    if missing:
        raise RuntimeError("Configuração de lembretes incompleta: " + ", ".join(missing))
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN, http_client=TwilioHttpClient(timeout=10))
    scheduler = BackgroundScheduler(timezone=TIMEZONE)
    scheduler.add_job(
        process_reminders, "cron", minute="*", args=[client], max_instances=1,
        next_run_time=datetime.now(TIMEZONE), misfire_grace_time=60
    )
    scheduler.start()
    return scheduler

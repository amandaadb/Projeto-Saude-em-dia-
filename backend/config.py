import os
from dotenv import load_dotenv

load_dotenv() # Carrega variáveis do arquivo .env

class Settings: 
    """Configurações da aplicação."""

    # Supabase.
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")
    SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

    # Google.
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
    GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")

    # Lembretes por Twilio.
    REMINDERS_ENABLED = os.getenv("REMINDERS_ENABLED", "False").lower() == "true"
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_SMS_FROM = os.getenv("TWILIO_SMS_FROM")
    TWILIO_TRIAL_MODE = os.getenv("TWILIO_TRIAL_MODE", "False").lower() == "true"

    # JWT (segurança).
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM", "HS256")

    # Servidor.
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))

# Instância global.
settings = Settings()
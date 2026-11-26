CREATE TABLE public.users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    dt_birth DATE NOT NULL,
    blood_type TEXT,
    emergency_contact_name TEXT,
    emergency_contact_phone TEXT,
    allergies TEXT,
    chronic_conditions TEXT,
    fl_active BOOLEAN NOT NULL DEFAULT TRUE,
    dt_created TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    dt_updated TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE public.medicines (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL,
    name TEXT NOT NULL,
    dosage TEXT NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    usage_type TEXT,
    usage_instructions TEXT,
    stock INTEGER NOT NULL DEFAULT 0 CHECK (stock >= 0),
    description TEXT,
    stock_limit INTEGER NOT NULL DEFAULT 5 CHECK (stock_limit >= 0),
    notification_enabled BOOLEAN NOT NULL DEFAULT TRUE,
    fl_active BOOLEAN NOT NULL DEFAULT TRUE,
    dt_created TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    dt_updated TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT medicines_user_id_fkey
        FOREIGN KEY (user_id)
        REFERENCES public.users(id)
        ON DELETE CASCADE
);
CREATE TABLE public.routines (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL,
    medicine_id UUID NOT NULL,
    time TIME NOT NULL,
    days_of_week TEXT NOT NULL DEFAULT 'Todos',
    fl_active BOOLEAN NOT NULL DEFAULT TRUE,
    dt_created TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    dt_updated TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT routines_user_id_fkey
        FOREIGN KEY (user_id)
        REFERENCES public.users(id)
        ON DELETE CASCADE,
    CONSTRAINT routines_medicine_id_fkey
        FOREIGN KEY (medicine_id)
        REFERENCES public.medicines(id)
        ON DELETE CASCADE
);
CREATE TABLE public.history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    routine_id UUID NOT NULL,
    user_id UUID NOT NULL,
    dt_hour TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    fl_taken BOOLEAN NOT NULL,
    dt_created TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT history_routine_id_fkey
        FOREIGN KEY (routine_id)
        REFERENCES public.routines(id)
        ON DELETE CASCADE,
    CONSTRAINT history_user_id_fkey
        FOREIGN KEY (user_id)
        REFERENCES public.users(id)
        ON DELETE CASCADE
);

CREATE OR REPLACE FUNCTION public.update_dt_updated()
RETURNS TRIGGER AS $$
BEGIN
    NEW.dt_updated = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_users_dt_updated
BEFORE UPDATE ON public.users
FOR EACH ROW
EXECUTE FUNCTION public.update_dt_updated();
CREATE TRIGGER trg_medicines_dt_updated
BEFORE UPDATE ON public.medicines
FOR EACH ROW
EXECUTE FUNCTION public.update_dt_updated();
CREATE TRIGGER trg_routines_dt_updated
BEFORE UPDATE ON public.routines
FOR EACH ROW
EXECUTE FUNCTION public.update_dt_updated();

CREATE INDEX idx_medicines_user_id
ON public.medicines(user_id);
CREATE INDEX idx_medicines_active
ON public.medicines(user_id, fl_active);
CREATE INDEX idx_routines_user_id
ON public.routines(user_id);
CREATE INDEX idx_routines_medicine_id
ON public.routines(medicine_id);
CREATE INDEX idx_routines_active
ON public.routines(user_id, fl_active);
CREATE INDEX idx_history_user_id
ON public.history(user_id);
CREATE INDEX idx_history_routine_id
ON public.history(routine_id);
CREATE INDEX idx_history_dt_hour
ON public.history(dt_hour);

-- Execute após tables.sql; também pode ser aplicado a um banco já existente.
CREATE TABLE public.reminder_preferences (
    user_id UUID PRIMARY KEY REFERENCES public.users(id) ON DELETE CASCADE,
    enabled BOOLEAN NOT NULL DEFAULT FALSE,
    channel TEXT NOT NULL CHECK (channel IN ('sms', 'whatsapp')),
    phone TEXT NOT NULL CHECK (phone ~ '^\+[1-9][0-9]{7,14}$'),
    consent_at TIMESTAMPTZ NOT NULL
);

CREATE TABLE public.reminder_stock_cycles (
    medicine_id UUID PRIMARY KEY REFERENCES public.medicines(id) ON DELETE CASCADE,
    cycle_id UUID NOT NULL DEFAULT gen_random_uuid()
);

CREATE TABLE public.reminder_attempts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
    event_key TEXT NOT NULL UNIQUE,
    kind TEXT NOT NULL CHECK (kind IN ('dose', 'stock')),
    status TEXT NOT NULL DEFAULT 'claimed' CHECK (status IN ('claimed', 'accepted', 'failed', 'unknown', 'cancelled')),
    provider_id TEXT,
    dt_created TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    dt_updated TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TRIGGER trg_reminder_attempts_dt_updated
BEFORE UPDATE ON public.reminder_attempts
FOR EACH ROW EXECUTE FUNCTION public.update_dt_updated();

CREATE OR REPLACE FUNCTION public.reset_reminder_stock_cycle()
RETURNS TRIGGER LANGUAGE plpgsql AS $$
BEGIN
    IF NEW.stock > NEW.stock_limit AND OLD.stock <= OLD.stock_limit THEN
        DELETE FROM public.reminder_stock_cycles WHERE medicine_id = NEW.id;
    END IF;
    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_reset_reminder_stock_cycle
AFTER UPDATE OF stock, stock_limit ON public.medicines
FOR EACH ROW EXECUTE FUNCTION public.reset_reminder_stock_cycle();

-- A reserva é atômica entre processos; a mensagem é enviada somente após a reserva.
CREATE OR REPLACE FUNCTION public.claim_stock_reminder(p_medicine_id UUID, p_user_id UUID)
RETURNS UUID LANGUAGE plpgsql AS $$
DECLARE
    v_cycle UUID;
    v_attempt UUID;
BEGIN
    PERFORM 1 FROM public.medicines m
    JOIN public.users u ON u.id = m.user_id
    JOIN public.reminder_preferences p ON p.user_id = u.id
    WHERE m.id = p_medicine_id AND m.user_id = p_user_id
      AND m.fl_active AND m.notification_enabled AND m.stock <= m.stock_limit
      AND u.fl_active AND p.enabled
    FOR UPDATE OF m;
    IF NOT FOUND THEN RETURN NULL; END IF;

    INSERT INTO public.reminder_stock_cycles (medicine_id) VALUES (p_medicine_id)
    ON CONFLICT (medicine_id) DO NOTHING;
    SELECT cycle_id INTO v_cycle FROM public.reminder_stock_cycles WHERE medicine_id = p_medicine_id;
    INSERT INTO public.reminder_attempts (user_id, event_key, kind)
    VALUES (p_user_id, 'stock:' || p_medicine_id::TEXT || ':' || v_cycle::TEXT, 'stock')
    ON CONFLICT (event_key) DO NOTHING RETURNING id INTO v_attempt;
    RETURN v_attempt;
END;
$$;

CREATE OR REPLACE FUNCTION public.claim_dose_reminder(
    p_routine_id UUID, p_user_id UUID, p_date DATE, p_time TIME, p_days TEXT
)
RETURNS UUID LANGUAGE plpgsql AS $$
DECLARE
    v_attempt UUID;
BEGIN
    INSERT INTO public.reminder_attempts (user_id, event_key, kind)
    SELECT p_user_id, 'dose:' || r.id::TEXT || ':' || p_date::TEXT, 'dose'
    FROM public.routines r
    JOIN public.medicines m ON m.id = r.medicine_id AND m.user_id = r.user_id
    JOIN public.users u ON u.id = r.user_id
    JOIN public.reminder_preferences p ON p.user_id = u.id
    WHERE r.id = p_routine_id AND r.user_id = p_user_id AND r.fl_active
      AND r.time = p_time AND r.days_of_week = p_days AND m.fl_active
      AND u.fl_active AND p.enabled
    ON CONFLICT (event_key) DO NOTHING RETURNING id INTO v_attempt;
    RETURN v_attempt;
END;
$$;

REVOKE ALL ON public.reminder_preferences, public.reminder_stock_cycles, public.reminder_attempts FROM PUBLIC, anon, authenticated;
REVOKE ALL ON FUNCTION public.claim_stock_reminder(UUID, UUID) FROM PUBLIC, anon, authenticated;
REVOKE ALL ON FUNCTION public.claim_dose_reminder(UUID, UUID, DATE, TIME, TEXT) FROM PUBLIC, anon, authenticated;
GRANT ALL ON public.reminder_preferences, public.reminder_stock_cycles, public.reminder_attempts TO service_role;
GRANT EXECUTE ON FUNCTION public.claim_stock_reminder(UUID, UUID) TO service_role;
GRANT EXECUTE ON FUNCTION public.claim_dose_reminder(UUID, UUID, DATE, TIME, TEXT) TO service_role;

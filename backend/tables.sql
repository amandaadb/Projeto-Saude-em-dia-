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
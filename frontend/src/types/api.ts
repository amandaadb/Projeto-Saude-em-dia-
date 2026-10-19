// Espelho EXATO dos modelos do back-end (backend/models.py).
// Se o back mudar um campo, muda aqui também — é o contrato entre vocês.

export type Medicine = {
  id: string;
  user_id: string;
  name: string;
  dosage: string;                    // "50 mg"
  quantity: number;                  // obrigatório e > 0 no banco (semântica: confirmar com o back)
  usage_type: string | null;
  usage_instructions: string | null;
  stock: number;                     // >= 0
  description: string | null;
  fl_active: boolean;
  dt_created: string;
  dt_updated: string;
};

// Rotina = "tome o remédio X às HH:MM nesses dias"
export type Routine = {
  id: string;
  medicine_id: string;
  user_id: string;
  time: string;          // "08:00:00"
  days_of_week: string;  // padrão "Todos" (formato dos outros valores: confirmar com o back)
  fl_active: boolean;
  dt_created: string;
  dt_updated: string;
};

// Histórico = registro de UMA dose que aconteceu (ou não)
export type History = {
  id: string;
  routine_id: string;
  user_id: string;
  dt_hour: string;   // data/hora da dose
  fl_taken: boolean; // true = tomou | false = não tomou
  dt_created: string;
};

export type TokenResponse = { access_token: string; token_type: 'bearer' };

// Usuário (UserResponse — senha nunca volta da API)
export type User = {
  id: string;
  name: string;
  email: string;
  phone: string;
  dt_birth: string;               // "AAAA-MM-DD"
  blood_type: string | null;
  emergency_contact_name: string | null;
  emergency_contact_phone: string | null;
  allergies: string | null;
  chronic_conditions: string | null;
  fl_active: boolean;
  dt_created: string;
  dt_updated: string;
};

// Campos que o formulário envia (MedicineCreate / MedicineUpdate)
export type MedicineInput = Pick<
  Medicine,
  'name' | 'dosage' | 'quantity' | 'usage_type' | 'usage_instructions' | 'stock' | 'description'
>;

// Campos editáveis do perfil (UserUpdate, sem senha)
export type UserInput = Partial<Omit<User, 'id' | 'fl_active' | 'dt_created' | 'dt_updated'>>;

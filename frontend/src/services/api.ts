// =============================================================
// Cliente da API (FastAPI do back-end). AINDA NÃO usado pelas telas:
// esta semana é layout com dados de teste. Fica pronto pra integração,
// quando cada ação do MedStore passa a chamar a função daqui.
// =============================================================
import { History, Medicine, MedicineInput, Routine, TokenResponse, User, UserInput } from '../types/api';

// Endereço da API. No celular físico, "localhost" é o próprio celular:
// use o IP do computador que roda o back (ex.: http://192.168.0.10:8000).
const BASE_URL = process.env.EXPO_PUBLIC_API_URL ?? 'http://localhost:8000';

let token: string | null = null;
export const setToken = (t: string | null) => { token = t; };

async function request<T>(path: string, method = 'GET', body?: unknown): Promise<T> {
  const res = await fetch(`${BASE_URL}${path}`, {
    method,
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  const data = await res.json().catch(() => null);
  // FastAPI devolve erros como { detail: "mensagem" }
  if (!res.ok) throw new Error(data?.detail ?? `Erro ${res.status}`);
  return data as T;
}

export const api = {
  // Auth
  login: (email: string, password: string) =>
    request<TokenResponse>('/api/auth/login', 'POST', { email, password }),
  me: () => request<User>('/api/auth/me'),
  updateMe: (patch: UserInput & { password?: string }) => request<User>('/api/auth/me', 'PUT', patch),
  deleteAccount: () => request<{ mensagem: string }>('/api/auth/delete-account', 'DELETE'),

  // Medicamentos
  listMedicines: () => request<Medicine[]>('/api/medicines'),
  createMedicine: (input: MedicineInput) => request<Medicine>('/api/medicines', 'POST', input),
  updateMedicine: (id: string, input: Partial<MedicineInput>) =>
    request<Medicine>(`/api/medicines/${id}`, 'PUT', input),
  deleteMedicine: (id: string) => request<{ mensagem: string }>(`/api/medicines/${id}`, 'DELETE'),

  // Rotinas (horários)
  listRoutines: () => request<Routine[]>('/api/routines'),
  createRoutine: (medicine_id: string, time: string, days_of_week = 'Todos') =>
    request<Routine>('/api/routines', 'POST', { medicine_id, time, days_of_week }),
  deleteRoutine: (id: string) => request<{ mensagem: string }>(`/api/routines/${id}`, 'DELETE'),

  // Histórico
  listHistory: () => request<History[]>('/api/history'),
  registerDose: (routine_id: string, fl_taken: boolean) =>
    request<History>('/api/history', 'POST', { routine_id, fl_taken }),
};

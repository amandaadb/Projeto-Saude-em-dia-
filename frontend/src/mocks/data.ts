// Dados FALSOS no MESMO formato que a API devolve (types/api.ts).
// Quando ligar na API de verdade, a tela não muda: só a origem dos dados.
import { Medicine, Routine, History, User } from '../types/api';

const now = '2026-10-13T00:00:00Z';
const USER = 'u1';

const med = (id: string, name: string, dosage: string, stock: number): Medicine => ({
  id, user_id: USER, name, dosage, quantity: 1, usage_type: 'Oral',
  usage_instructions: null, stock, description: null, fl_active: true,
  dt_created: now, dt_updated: now,
});

const routine = (id: string, medicine_id: string, time: string): Routine => ({
  id, medicine_id, user_id: USER, time, days_of_week: 'Todos',
  fl_active: true, dt_created: now, dt_updated: now,
});

export const medicines: Medicine[] = [
  med('m1', 'Losartana', '50 mg', 24),
  med('m2', 'Vitamina D', '2000 UI', 3),   // ⚠️ estoque baixo
  med('m3', 'Omeprazol', '20 mg', 12),
];

export const routines: Routine[] = [
  routine('r1', 'm3', '07:00:00'),
  routine('r2', 'm1', '08:00:00'),
  routine('r3', 'm2', '12:00:00'),
  routine('r4', 'm1', '20:00:00'),
];

// Gera o histórico com a data de HOJE, pra o mock funcionar em qualquer dia
const todayAt = (hhmm: string, daysAgo = 0) => {
  const d = new Date();
  d.setDate(d.getDate() - daysAgo);
  const [h, m] = hhmm.split(':').map(Number);
  d.setHours(h, m, 0, 0);
  return d.toISOString();
};

export const history: History[] = [
  { id: 'h1', routine_id: 'r1', user_id: USER, dt_hour: todayAt('07:05'), fl_taken: true,  dt_created: now },
  { id: 'h2', routine_id: 'r2', user_id: USER, dt_hour: todayAt('09:30'), fl_taken: false, dt_created: now },
  // r3 e r4 sem registro hoje -> aparecem como ⏰ Pendente
  // Ontem (pra aba Histórico ter o que agrupar por data)
  { id: 'h3', routine_id: 'r1', user_id: USER, dt_hour: todayAt('07:02', 1), fl_taken: true,  dt_created: now },
  { id: 'h4', routine_id: 'r2', user_id: USER, dt_hour: todayAt('08:10', 1), fl_taken: true,  dt_created: now },
  { id: 'h5', routine_id: 'r3', user_id: USER, dt_hour: todayAt('13:40', 1), fl_taken: false, dt_created: now },
  { id: 'h6', routine_id: 'r4', user_id: USER, dt_hour: todayAt('20:05', 1), fl_taken: true,  dt_created: now },
];

export const user: User = {
  id: USER, name: 'Daniela Rosa', email: 'daniela@email.com', phone: '(11) 99999-0000',
  dt_birth: '1995-05-20', blood_type: 'O+', emergency_contact_name: null,
  emergency_contact_phone: null, allergies: null, chronic_conditions: null,
  fl_active: true, dt_created: now, dt_updated: now,
};

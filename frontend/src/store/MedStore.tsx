// =============================================================
// MedStore — estado ÚNICO do app, compartilhado pelas 4 abas.
// Marcou dose em "Hoje"? Aparece no "Histórico".
// Mudou estoque em "Medicamentos"? O ⚠️ atualiza em "Hoje".
//
// Analogia (GOT7): o store é o fandom IGOT7 — uma fonte só,
// e cada membro (tela) lê dela em vez de guardar sua própria cópia.
//
// Cada ação tem o endpoint correspondente comentado. Na integração,
// troca-se o corpo da função pela chamada em services/api.ts.
// =============================================================
import { createContext, ReactNode, useContext, useState } from 'react';
import * as mock from '../mocks/data';
import { History, Medicine, MedicineInput, Routine, User, UserInput } from '../types/api';

export type NotificationPrefs = {
  doseReminders: boolean;
  lowStockAlerts: boolean;
};

type Store = {
  user: User;
  medicines: Medicine[]; // inclui inativos (ver nota em HistoryScreen)
  routines: Routine[];
  history: History[];
  notificationPrefs: NotificationPrefs;

  createMedicine: (input: MedicineInput, times: string[]) => void;
  updateMedicine: (id: string, input: MedicineInput, times: string[]) => void;
  deleteMedicine: (id: string) => void;
  adjustStock: (id: string, delta: number) => void;
  registerDose: (routineId: string, taken: boolean) => void;
  updateUser: (patch: UserInput) => void;
  setNotificationPrefs: (prefs: NotificationPrefs) => void;
};

const MedStoreContext = createContext<Store | null>(null);

const newId = () => `local-${Date.now()}-${Math.random().toString(36).slice(2, 7)}`;
const nowIso = () => new Date().toISOString();
const toApiTime = (hhmm: string) => `${hhmm}:00`; // "08:00" -> "08:00:00"

export function MedStoreProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User>(mock.user);
  const [medicines, setMedicines] = useState<Medicine[]>(mock.medicines);
  const [routines, setRoutines] = useState<Routine[]>(mock.routines);
  const [history, setHistory] = useState<History[]>(mock.history);
  // ⚠️ Sem endpoint no back: hoje fica só no aparelho.
  const [notificationPrefs, setNotificationPrefs] = useState<NotificationPrefs>({
    doseReminders: true,
    lowStockAlerts: true,
  });

  const makeRoutine = (medicineId: string, hhmm: string): Routine => ({
    id: newId(), medicine_id: medicineId, user_id: user.id, time: toApiTime(hhmm),
    days_of_week: 'Todos', fl_active: true, dt_created: nowIso(), dt_updated: nowIso(),
  });

  // POST /api/medicines  +  POST /api/routines (uma por horário)
  function createMedicine(input: MedicineInput, times: string[]) {
    const id = newId();
    setMedicines((prev) => [
      ...prev,
      { ...input, id, user_id: user.id, fl_active: true, dt_created: nowIso(), dt_updated: nowIso() },
    ]);
    setRoutines((prev) => [...prev, ...times.map((t) => makeRoutine(id, t))]);
  }

  // PUT /api/medicines/{id}
  // + DELETE /api/routines/{id} p/ horários removidos e POST p/ horários novos
  function updateMedicine(id: string, input: MedicineInput, times: string[]) {
    setMedicines((prev) =>
      prev.map((m) => (m.id === id ? { ...m, ...input, dt_updated: nowIso() } : m))
    );
    setRoutines((prev) => {
      const current = prev.filter((r) => r.medicine_id === id && r.fl_active);
      const currentTimes = current.map((r) => r.time.slice(0, 5));
      const removed = current.filter((r) => !times.includes(r.time.slice(0, 5)));
      const added = times.filter((t) => !currentTimes.includes(t));
      return [
        ...prev.map((r) => (removed.some((x) => x.id === r.id) ? { ...r, fl_active: false } : r)),
        ...added.map((t) => makeRoutine(id, t)),
      ];
    });
  }

  // DELETE /api/medicines/{id}  (soft delete: fl_active = false)
  // ⚠️ O back NÃO desativa as rotinas junto; o front precisa chamar
  // DELETE /api/routines/{id} de cada uma, senão sobram rotinas órfãs.
  function deleteMedicine(id: string) {
    setMedicines((prev) => prev.map((m) => (m.id === id ? { ...m, fl_active: false } : m)));
    setRoutines((prev) => prev.map((r) => (r.medicine_id === id ? { ...r, fl_active: false } : r)));
  }

  // PUT /api/medicines/{id}  { stock }
  function adjustStock(id: string, delta: number) {
    setMedicines((prev) =>
      prev.map((m) => (m.id === id ? { ...m, stock: Math.max(0, m.stock + delta) } : m))
    );
  }

  // POST /api/history  { routine_id, fl_taken }
  // ⚠️ O back aceita registrar a mesma dose duas vezes; quem impede é o front
  // (só dose "pendente" deixa registrar).
  function registerDose(routineId: string, taken: boolean) {
    setHistory((prev) => [
      { id: newId(), routine_id: routineId, user_id: user.id, dt_hour: nowIso(), fl_taken: taken, dt_created: nowIso() },
      ...prev,
    ]);
  }

  // PUT /api/auth/me
  function updateUser(patch: UserInput) {
    setUser((prev) => ({ ...prev, ...patch, dt_updated: nowIso() }));
  }

  return (
    <MedStoreContext.Provider
      value={{
        user, medicines, routines, history, notificationPrefs,
        createMedicine, updateMedicine, deleteMedicine, adjustStock,
        registerDose, updateUser, setNotificationPrefs,
      }}
    >
      {children}
    </MedStoreContext.Provider>
  );
}

// Hook que as telas usam: const { medicines, registerDose } = useMedStore();
export function useMedStore() {
  const ctx = useContext(MedStoreContext);
  if (!ctx) throw new Error('useMedStore precisa estar dentro de <MedStoreProvider>');
  return ctx;
}

// O back-end NÃO guarda "pendente". Ele só tem:
//   routines  -> o que deveria acontecer
//   history   -> o que de fato aconteceu (fl_taken true/false)
// Então o status de cada dose de HOJE é CALCULADO no front:
//
//   existe history da rotina hoje?  ── não ──▶ ⏰ pending
//              │ sim
//              ▼
//          fl_taken? ── true ──▶ ✅ taken
//              └──── false ──▶ ❌ missed
import { DoseStatus } from '../theme';
import { History, Medicine, Routine } from '../types/api';

// ⚠️ O banco não tem campo de limite de estoque. Valor provisório no front;
// sugerir ao back um campo `stock_alert` em medicines.
export const LOW_STOCK_THRESHOLD = 5;

export type TodayDose = {
  routineId: string;
  medicine: Medicine;
  time: string;          // "08:00"
  status: DoseStatus;
  lowStock: boolean;
};

const isSameDay = (iso: string, ref: Date) => {
  const d = new Date(iso);
  return (
    d.getFullYear() === ref.getFullYear() &&
    d.getMonth() === ref.getMonth() &&
    d.getDate() === ref.getDate()
  );
};

export function buildTodayDoses(
  routines: Routine[],
  history: History[],
  medicines: Medicine[],
  today = new Date()
): TodayDose[] {
  return routines
    .filter((r) => r.fl_active)
    // TODO: filtrar por days_of_week quando o formato estiver definido
    .map((r) => {
      const medicine = medicines.find((m) => m.id === r.medicine_id);
      if (!medicine || !medicine.fl_active) return null;

      const record = history.find(
        (h) => h.routine_id === r.id && isSameDay(h.dt_hour, today)
      );

      const status: DoseStatus = !record ? 'pending' : record.fl_taken ? 'taken' : 'missed';

      return {
        routineId: r.id,
        medicine,
        time: r.time.slice(0, 5),
        status,
        lowStock: medicine.stock <= LOW_STOCK_THRESHOLD,
      };
    })
    .filter((d): d is TodayDose => d !== null)
    .sort((a, b) => a.time.localeCompare(b.time));
}

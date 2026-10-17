// Conversões entre o que o usuário digita e o que a API espera.

// "8:5" não; "08:05" sim. Aceita 00:00 a 23:59.
export const isValidTime = (v: string) => /^([01]\d|2[0-3]):[0-5]\d$/.test(v);

// "20/05/1995" -> "1995-05-20" (formato do back) | null se inválida
export function brDateToIso(v: string): string | null {
  const m = /^(\d{2})\/(\d{2})\/(\d{4})$/.exec(v);
  if (!m) return null;
  const [, d, mo, y] = m;
  const date = new Date(Number(y), Number(mo) - 1, Number(d));
  const ok = date.getDate() === Number(d) && date.getMonth() === Number(mo) - 1;
  return ok ? `${y}-${mo}-${d}` : null;
}

// "1995-05-20" -> "20/05/1995"
export function isoToBrDate(v: string) {
  const [y, m, d] = v.slice(0, 10).split('-');
  return `${d}/${m}/${y}`;
}

// ISO completo -> "13/10/2026" e "08:05" (no fuso do aparelho)
export const formatDate = (iso: string) => new Date(iso).toLocaleDateString('pt-BR');
export const formatTime = (iso: string) =>
  new Date(iso).toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' });

// Campo de texto vazio vira null (o back espera null, não "")
export const emptyToNull = (v: string) => (v.trim() === '' ? null : v.trim());

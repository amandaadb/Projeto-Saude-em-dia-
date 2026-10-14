// =============================================================
// MedControl — Guia de estilos em código (design tokens)
// Fonte: UI-UX.md do repositório (paleta oficial + tipografia).
// Regra de ouro: nenhum componente escreve cor/tamanho "na mão".
// =============================================================

// ---------- Paleta oficial (UI-UX.md) ----------
export const palette = {
  blue100: '#BDDDFC', // Azul claro
  blue300: '#88BDF2', // Azul médio
  blue500: '#6A89A7', // Azul principal
  blue900: '#384959', // Azul escuro

  green100: '#E3F0A3', // Verde claro
  green300: '#BADBA2', // Verde suave
  green500: '#80EF80', // Verde principal
  green700: '#42D674', // Verde vibrante

  pink100: '#FAD2E1', // Rosa claro
  pink300: '#F8B4CD', // Rosa médio
  pink500: '#E06D95', // Rosa principal
  pink900: '#7D2845', // Rosa escuro
};

// ---------- Papéis semânticos (o que os componentes usam) ----------
export const colors = {
  primary: palette.blue500,
  // Fundo de botão usa o azul ESCURO: branco sobre #6A89A7 dá contraste
  // ~3,7:1 (reprova WCAG AA p/ texto normal); sobre #384959 dá ~9,3:1.
  primaryStrong: palette.blue900,
  primarySoft: palette.blue100,
  background: '#F7FAFD',   // neutro derivado do azul claro (não está no guia)
  surface: '#FFFFFF',
  text: palette.blue900,
  textMuted: palette.blue500,
  border: '#E1EBF5',       // neutro derivado (não está no guia)
  danger: palette.pink900, // rosa principal c/ texto branco dá ~3,1:1; o escuro passa folgado
  white: '#FFFFFF',
};

export const spacing = { xs: 4, sm: 8, md: 16, lg: 24, xl: 32 };
export const radius = { sm: 8, md: 14, pill: 999 };

// ---------- Tipografia (Inter + Nunito Sans) ----------
// No React Native, fonte customizada NÃO responde a fontWeight no Android:
// cada peso é uma fontFamily diferente. Por isso o peso vai no nome.
// Os nomes abaixo são os exportados por @expo-google-fonts (ver useAppFonts).
export const fonts = {
  regular: 'Inter_400Regular',
  medium: 'Inter_500Medium',
  semibold: 'Inter_600SemiBold',
  bold: 'Inter_700Bold',
  secondary: 'NunitoSans_400Regular',
};

// Tamanhos pensados p/ público idoso (requisito não funcional da proposta)
export const typography = {
  title:    { fontFamily: fonts.bold,     fontSize: 24 },
  subtitle: { fontFamily: fonts.semibold, fontSize: 18 },
  body:     { fontFamily: fonts.regular,  fontSize: 16 },
  caption:  { fontFamily: fonts.medium,   fontSize: 14 },
};

// -------------------------------------------------------------
// Estados da DOSE
// -------------------------------------------------------------
export type DoseStatus = 'taken' | 'pending' | 'missed';

export const doseStatusStyle: Record<
  DoseStatus,
  { label: string; icon: string; bg: string; fg: string }
> = {
  taken:   { label: 'Tomado',     icon: '✅', bg: palette.green300, fg: palette.blue900 },
  pending: { label: 'Pendente',   icon: '⏰', bg: palette.blue100,  fg: palette.blue900 },
  missed:  { label: 'Não tomado', icon: '❌', bg: palette.pink100,  fg: palette.pink900 },
};

// -------------------------------------------------------------
// Estado do ESTOQUE (do medicamento, coexiste com o da dose)
// ⚠️ O guia não tem cor de alerta (amarelo/laranja). Valores abaixo
// são PROVISÓRIOS — confirmar com o UX/UI.
// -------------------------------------------------------------
export const lowStockStyle = {
  label: 'Estoque baixo',
  icon: '⚠️',
  bg: '#FFE8C2',
  fg: '#8A4B00',
};

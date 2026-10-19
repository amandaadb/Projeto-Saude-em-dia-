import { ReactNode } from 'react';
import { View, Text, Pressable, StyleSheet } from 'react-native';
import { colors, radius, spacing, typography, DoseStatus } from '../theme';
import { StatusBadge } from './StatusBadge';

// Card "burro" (presentational): só recebe dados e mostra.
// Quem decide o que acontece no toque é a TELA, via onPress.
type Props = {
  name: string;
  dosage: string;
  time?: string;          // "08:00" — aparece na aba Hoje
  status?: DoseStatus;    // badge de dose (opcional)
  stock?: number;         // aparece na aba Medicamentos
  lowStock?: boolean;     // badge ⚠️
  onPress?: () => void;
  subtitle?: string;      // linha extra (ex.: horários na aba Medicamentos)
  children?: ReactNode;   // área extra no rodapé (ex.: controle de estoque)
};

export function MedicationCard({ name, dosage, time, status, stock, lowStock, onPress, subtitle, children }: Props) {
  return (
    <Pressable
      onPress={onPress}
      style={({ pressed }) => [styles.card, pressed && { opacity: 0.9 }]}
    >
      <View style={styles.row}>
        <View style={{ flex: 1 }}>
          <Text style={styles.name}>{name}</Text>
          <Text style={styles.meta}>
            {dosage}
            {stock !== undefined && ` · ${stock} un.`}
          </Text>
          {!!subtitle && <Text style={styles.meta}>{subtitle}</Text>}
        </View>
        {time && <Text style={styles.time}>{time}</Text>}
      </View>

      {(status || lowStock) && (
        <View style={styles.badges}>
          {status && <StatusBadge status={status} />}
          {lowStock && <StatusBadge lowStock />}
        </View>
      )}
      {children}
    </Pressable>
  );
}

const styles = StyleSheet.create({
  card: {
    backgroundColor: colors.surface,
    borderRadius: radius.md,
    padding: spacing.md,
    marginBottom: spacing.sm + 4,
    borderWidth: 1,
    borderColor: colors.border,
    // sombra: iOS usa shadow*, Android usa elevation
    shadowColor: '#000',
    shadowOpacity: 0.05,
    shadowRadius: 6,
    shadowOffset: { width: 0, height: 2 },
    elevation: 2,
  },
  row: { flexDirection: 'row', alignItems: 'center' },
  name: { ...typography.subtitle, color: colors.text },
  meta: { ...typography.body, color: colors.textMuted, marginTop: 2 },
  time: { ...typography.title, color: colors.primaryStrong },
  badges: { flexDirection: 'row', gap: spacing.sm, marginTop: spacing.sm },
});

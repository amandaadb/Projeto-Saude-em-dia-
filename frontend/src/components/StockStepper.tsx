// Controle de estoque: [ − ]  12 un.  [ + ]
// Botões grandes (48px) — alvo de toque confortável p/ idosos.
import { View, Text, Pressable, StyleSheet } from 'react-native';
import { colors, radius, spacing, typography } from '../theme';

type Props = {
  value: number;
  onChange: (delta: number) => void;
};

export function StockStepper({ value, onChange }: Props) {
  return (
    <View style={styles.row}>
      <Text style={styles.label}>Estoque</Text>
      <Step symbol="−" label="Diminuir estoque" onPress={() => onChange(-1)} disabled={value === 0} />
      <Text style={styles.value}>{value} un.</Text>
      <Step symbol="+" label="Aumentar estoque" onPress={() => onChange(1)} />
    </View>
  );
}

function Step({ symbol, label, onPress, disabled }: {
  symbol: string; label: string; onPress: () => void; disabled?: boolean;
}) {
  return (
    <Pressable
      onPress={onPress}
      disabled={disabled}
      accessibilityRole="button"
      accessibilityLabel={label}
      style={({ pressed }) => [styles.btn, pressed && { opacity: 0.7 }, disabled && { opacity: 0.3 }]}
    >
      <Text style={styles.symbol}>{symbol}</Text>
    </Pressable>
  );
}

const styles = StyleSheet.create({
  row: {
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: spacing.sm + 4,
    paddingTop: spacing.sm + 4,
    borderTopWidth: 1,
    borderTopColor: colors.border,
  },
  label: { ...typography.caption, color: colors.textMuted, flex: 1 },
  btn: {
    width: 48,
    height: 48,
    borderRadius: radius.md,
    backgroundColor: colors.primarySoft,
    alignItems: 'center',
    justifyContent: 'center',
  },
  symbol: { ...typography.title, color: colors.primaryStrong },
  value: { ...typography.subtitle, color: colors.text, minWidth: 72, textAlign: 'center' },
});

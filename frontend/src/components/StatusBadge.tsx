import { View, Text, StyleSheet } from 'react-native';
import { doseStatusStyle, lowStockStyle, radius, spacing, typography, DoseStatus } from '../theme';

// Uso:
//   <StatusBadge status="pending" />
//   <StatusBadge lowStock />
type Props =
  | { status: DoseStatus; lowStock?: never }
  | { lowStock: true; status?: never };

export function StatusBadge(props: Props) {
  const s = props.lowStock ? lowStockStyle : doseStatusStyle[props.status];

  return (
    <View
      style={[styles.badge, { backgroundColor: s.bg }]}
      accessibilityLabel={s.label} // leitor de tela lê o texto, não o emoji
    >
      <Text style={[styles.text, { color: s.fg }]}>
        {s.icon} {s.label}
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  badge: {
    alignSelf: 'flex-start',
    paddingHorizontal: spacing.sm,
    paddingVertical: spacing.xs,
    borderRadius: radius.pill,
  },
  text: typography.caption,
});

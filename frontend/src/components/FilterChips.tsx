// Filtro em "pílulas": [Todas] [Tomadas] [Não tomadas]
// Genérico: funciona com qualquer lista de opções (T = tipo do valor).
import { View, Text, Pressable, StyleSheet } from 'react-native';
import { colors, radius, spacing, typography } from '../theme';

type Option<T> = { value: T; label: string };

type Props<T> = {
  options: Option<T>[];
  selected: T;
  onSelect: (value: T) => void;
};

export function FilterChips<T extends string>({ options, selected, onSelect }: Props<T>) {
  return (
    <View style={styles.row}>
      {options.map((o) => {
        const active = o.value === selected;
        return (
          <Pressable
            key={o.value}
            onPress={() => onSelect(o.value)}
            accessibilityRole="button"
            accessibilityState={{ selected: active }}
            style={[styles.chip, active && styles.chipActive]}
          >
            <Text style={[styles.text, active && styles.textActive]}>{o.label}</Text>
          </Pressable>
        );
      })}
    </View>
  );
}

const styles = StyleSheet.create({
  row: { flexDirection: 'row', gap: spacing.sm, paddingHorizontal: spacing.md, marginBottom: spacing.sm },
  chip: {
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.sm,
    borderRadius: radius.pill,
    borderWidth: 1.5,
    borderColor: colors.border,
    backgroundColor: colors.surface,
  },
  chipActive: { backgroundColor: colors.primaryStrong, borderColor: colors.primaryStrong },
  text: { ...typography.caption, color: colors.text },
  textActive: { color: colors.white },
});

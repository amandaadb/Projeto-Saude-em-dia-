import { Pressable, Text, StyleSheet } from 'react-native';
import { colors, radius, spacing, typography } from '../theme';

type Variant = 'primary' | 'secondary' | 'danger';

type Props = {
  title: string;
  onPress: () => void;
  variant?: Variant;   // padrão: 'primary'
  disabled?: boolean;
};

export function AppButton({ title, onPress, variant = 'primary', disabled }: Props) {
  return (
    <Pressable
      onPress={onPress}
      disabled={disabled}
      accessibilityRole="button"
      // "pressed" vem do Pressable: dá feedback visual ao toque
      style={({ pressed }) => [
        styles.base,
        styles[variant],
        pressed && { opacity: 0.8 },
        disabled && { opacity: 0.4 },
      ]}
    >
      <Text style={[styles.label, variant === 'secondary' && { color: colors.primaryStrong }]}>
        {title}
      </Text>
    </Pressable>
  );
}

const styles = StyleSheet.create({
  base: {
    paddingVertical: spacing.md - 4,
    paddingHorizontal: spacing.lg,
    borderRadius: radius.md,
    alignItems: 'center',
  },
  primary: { backgroundColor: colors.primaryStrong },
  secondary: { backgroundColor: 'transparent', borderWidth: 1.5, borderColor: colors.primaryStrong },
  danger: { backgroundColor: colors.danger },
  label: { ...typography.subtitle, color: colors.white },
});

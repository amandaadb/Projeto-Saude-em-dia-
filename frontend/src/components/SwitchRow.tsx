// Linha de preferência: texto à esquerda, interruptor à direita.
import { View, Text, Switch, StyleSheet } from 'react-native';
import { colors, palette, spacing, typography } from '../theme';

type Props = {
  label: string;
  description?: string;
  value: boolean;
  onChange: (v: boolean) => void;
};

export function SwitchRow({ label, description, value, onChange }: Props) {
  return (
    <View style={styles.row}>
      <View style={{ flex: 1, paddingRight: spacing.md }}>
        <Text style={styles.label}>{label}</Text>
        {!!description && <Text style={styles.desc}>{description}</Text>}
      </View>
      <Switch
        value={value}
        onValueChange={onChange}
        accessibilityLabel={label}
        trackColor={{ false: colors.border, true: palette.green700 }}
        thumbColor={colors.white}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  row: { flexDirection: 'row', alignItems: 'center', paddingVertical: spacing.sm + 4 },
  label: { ...typography.body, color: colors.text },
  desc: { ...typography.caption, color: colors.textMuted, marginTop: 2 },
});

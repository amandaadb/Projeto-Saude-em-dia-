// Moldura padrão de toda tela: área segura + fundo + título.
// Mantém as 4 abas visualmente idênticas na "casca".
import { ReactNode } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { colors, spacing, typography } from '../theme';

type Props = {
  title: string;
  right?: ReactNode;   // ação no canto do título (ex.: botão "+")
  children: ReactNode;
};

export function Screen({ title, right, children }: Props) {
  return (
    <SafeAreaView style={styles.container} edges={['top']}>
      <View style={styles.header}>
        <Text style={styles.title} accessibilityRole="header">{title}</Text>
        {right}
      </View>
      <View style={{ flex: 1 }}>{children}</View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: colors.background },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: spacing.md,
    paddingTop: spacing.md,
    paddingBottom: spacing.sm,
  },
  title: { ...typography.title, color: colors.text },
});

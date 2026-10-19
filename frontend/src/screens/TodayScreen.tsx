// ABA HOJE — próximos medicamentos, horários e status da dose.
import { useMemo } from 'react';
import { FlatList, View, Text, StyleSheet, Alert } from 'react-native';
import { colors, palette, radius, spacing, typography } from '../theme';
import { Screen } from '../components/Screen';
import { MedicationCard } from '../components/MedicationCard';
import { useMedStore } from '../store/MedStore';
import { buildTodayDoses } from '../utils/doses';

export function TodayScreen() {
  const { routines, history, medicines, registerDose } = useMedStore();

  // Derivado do store: recalcula só quando algo dele muda
  const doses = useMemo(
    () => buildTodayDoses(routines, history, medicines),
    [routines, history, medicines]
  );

  const count = {
    taken: doses.filter((d) => d.status === 'taken').length,
    pending: doses.filter((d) => d.status === 'pending').length,
    missed: doses.filter((d) => d.status === 'missed').length,
  };

  // Próxima dose = primeira pendente cujo horário ainda não passou
  const nowHHMM = new Date().toTimeString().slice(0, 5);
  const next = doses.find((d) => d.status === 'pending' && d.time >= nowHHMM);

  function askRegister(routineId: string, name: string, time: string) {
    Alert.alert(name, `Dose das ${time}`, [
      { text: 'Cancelar', style: 'cancel' },
      { text: 'Não tomei ❌', onPress: () => registerDose(routineId, false) },
      { text: 'Tomei ✅', onPress: () => registerDose(routineId, true) },
    ]);
  }

  return (
    <Screen title="Hoje">
      <FlatList
        data={doses}
        keyExtractor={(item) => item.routineId}
        contentContainerStyle={{ padding: spacing.md, paddingTop: spacing.sm }}
        ListHeaderComponent={
          <View style={styles.summary}>
            <Text style={styles.summaryTitle}>
              {next ? `Próxima: ${next.medicine.name} às ${next.time}` : 'Sem doses pendentes por agora'}
            </Text>
            <Text style={styles.summaryCount}>
              ✅ {count.taken}   ⏰ {count.pending}   ❌ {count.missed}
            </Text>
          </View>
        }
        ListEmptyComponent={
          <Text style={styles.empty}>Nenhuma dose agendada. Cadastre em Medicamentos.</Text>
        }
        renderItem={({ item }) => (
          <MedicationCard
            name={item.medicine.name}
            dosage={item.medicine.dosage}
            time={item.time}
            status={item.status}
            lowStock={item.lowStock}
            onPress={
              item.status === 'pending'
                ? () => askRegister(item.routineId, item.medicine.name, item.time)
                : undefined
            }
          />
        )}
      />
    </Screen>
  );
}

const styles = StyleSheet.create({
  summary: {
    backgroundColor: palette.blue100,
    borderRadius: radius.md,
    padding: spacing.md,
    marginBottom: spacing.md,
  },
  summaryTitle: { ...typography.subtitle, color: colors.text },
  summaryCount: { ...typography.body, color: colors.text, marginTop: spacing.xs },
  empty: { ...typography.body, color: colors.textMuted, textAlign: 'center', marginTop: spacing.xl },
});

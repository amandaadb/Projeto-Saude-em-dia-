// ABA HISTÓRICO — doses tomadas e não tomadas, com data e horário.
// Fonte: GET /api/history (já vem ordenado do mais recente p/ o mais antigo).
import { useMemo, useState } from 'react';
import { SectionList, View, Text, StyleSheet } from 'react-native';
import { colors, radius, spacing, typography } from '../theme';
import { Screen } from '../components/Screen';
import { StatusBadge } from '../components/StatusBadge';
import { FilterChips } from '../components/FilterChips';
import { useMedStore } from '../store/MedStore';
import { formatDate, formatTime } from '../utils/format';

type Filter = 'all' | 'taken' | 'missed';

export function HistoryScreen() {
  const { history, routines, medicines } = useMedStore();
  const [filter, setFilter] = useState<Filter>('all');

  // Agrupa por dia: [{ title: "13/10/2026", data: [...] }, ...]
  const sections = useMemo(() => {
    const filtered = history
      .filter((h) => filter === 'all' || (filter === 'taken' ? h.fl_taken : !h.fl_taken))
      .sort((a, b) => b.dt_hour.localeCompare(a.dt_hour));

    const groups = new Map<string, typeof filtered>();
    for (const h of filtered) {
      const day = formatDate(h.dt_hour);
      groups.set(day, [...(groups.get(day) ?? []), h]);
    }
    return [...groups].map(([title, data]) => ({ title, data }));
  }, [history, filter]);

  // routine -> medicine. ⚠️ Na API real, GET /routines e GET /medicines só
  // devolvem itens ATIVOS: registro de remédio excluído perde o nome.
  const medicineOf = (routineId: string) => {
    const r = routines.find((x) => x.id === routineId);
    return r && medicines.find((x) => x.id === r.medicine_id);
  };

  return (
    <Screen title="Histórico">
      <FilterChips<Filter>
        options={[
          { value: 'all', label: 'Todas' },
          { value: 'taken', label: '✅ Tomadas' },
          { value: 'missed', label: '❌ Não tomadas' },
        ]}
        selected={filter}
        onSelect={setFilter}
      />
      <SectionList
        sections={sections}
        keyExtractor={(h) => h.id}
        contentContainerStyle={{ padding: spacing.md, paddingTop: 0 }}
        stickySectionHeadersEnabled={false}
        renderSectionHeader={({ section }) => <Text style={styles.day}>{section.title}</Text>}
        renderItem={({ item }) => {
          const med = medicineOf(item.routine_id);
          return (
            <View style={styles.row}>
              <Text style={styles.time}>{formatTime(item.dt_hour)}</Text>
              <View style={{ flex: 1 }}>
                <Text style={styles.name} numberOfLines={1}>{med?.name ?? 'Medicamento removido'}</Text>
                {med && <Text style={styles.dosage}>{med.dosage}</Text>}
              </View>
              <StatusBadge status={item.fl_taken ? 'taken' : 'missed'} />
            </View>
          );
        }}
        ListEmptyComponent={<Text style={styles.empty}>Nenhum registro ainda.</Text>}
      />
    </Screen>
  );
}

const styles = StyleSheet.create({
  day: { ...typography.caption, color: colors.textMuted, marginTop: spacing.md, marginBottom: spacing.sm },
  row: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.sm + 4,
    backgroundColor: colors.surface,
    borderRadius: radius.md,
    borderWidth: 1,
    borderColor: colors.border,
    padding: spacing.md,
    marginBottom: spacing.sm,
  },
  time: { ...typography.subtitle, color: colors.primaryStrong, width: 56 },
  name: { ...typography.body, color: colors.text },
  dosage: { ...typography.caption, color: colors.textMuted },
  empty: { ...typography.body, color: colors.textMuted, textAlign: 'center', marginTop: spacing.xl },
});

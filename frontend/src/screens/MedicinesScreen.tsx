// ABA MEDICAMENTOS — listagem + controle de estoque.
// Inclusão/edição/exclusão acontecem em MedicineFormScreen.
// A tela NÃO conhece a navegação: recebe callbacks (onAdd, onEdit).
import { FlatList, Text, StyleSheet } from 'react-native';
import { colors, spacing, typography } from '../theme';
import { Screen } from '../components/Screen';
import { MedicationCard } from '../components/MedicationCard';
import { StockStepper } from '../components/StockStepper';
import { AppButton } from '../components/AppButton';
import { useMedStore } from '../store/MedStore';
import { LOW_STOCK_THRESHOLD } from '../utils/doses';

type Props = {
  onAdd: () => void;
  onEdit: (medicineId: string) => void;
};

export function MedicinesScreen({ onAdd, onEdit }: Props) {
  const { medicines, routines, adjustStock } = useMedStore();
  const active = medicines
    .filter((m) => m.fl_active)
    .sort((a, b) => a.name.localeCompare(b.name, 'pt-BR'));

  const timesOf = (medicineId: string) =>
    routines
      .filter((r) => r.medicine_id === medicineId && r.fl_active)
      .map((r) => r.time.slice(0, 5))
      .sort()
      .join(' · ');

  return (
    <Screen title="Medicamentos">
      <FlatList
        data={active}
        keyExtractor={(m) => m.id}
        contentContainerStyle={{ padding: spacing.md, paddingTop: spacing.sm }}
        ListHeaderComponent={
          <AppButton title="+ Adicionar medicamento" onPress={onAdd} />
        }
        ListHeaderComponentStyle={{ marginBottom: spacing.md }}
        ListEmptyComponent={
          <Text style={styles.empty}>Nenhum medicamento cadastrado ainda.</Text>
        }
        renderItem={({ item }) => (
          <MedicationCard
            name={item.name}
            dosage={item.dosage}
            subtitle={timesOf(item.id) || 'Sem horários definidos'}
            lowStock={item.stock <= LOW_STOCK_THRESHOLD}
            onPress={() => onEdit(item.id)}
          >
            <StockStepper value={item.stock} onChange={(delta) => adjustStock(item.id, delta)} />
          </MedicationCard>
        )}
      />
    </Screen>
  );
}

const styles = StyleSheet.create({
  empty: { ...typography.body, color: colors.textMuted, textAlign: 'center', marginTop: spacing.xl },
});

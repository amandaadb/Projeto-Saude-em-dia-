// INCLUSÃO / EDIÇÃO / EXCLUSÃO de medicamento.
// Sem medicineId = novo. Com medicineId = edição.
// Campos = exatamente os de MedicineCreate (backend/models.py)
// + lista de horários, que vira uma rotina por horário.
import { useState } from 'react';
import { ScrollView, View, Text, Pressable, StyleSheet, Alert, KeyboardAvoidingView, Platform } from 'react-native';
import { colors, palette, radius, spacing, typography } from '../theme';
import { AppInput } from '../components/AppInput';
import { AppButton } from '../components/AppButton';
import { Section } from '../components/Section';
import { useMedStore } from '../store/MedStore';
import { emptyToNull, isValidTime } from '../utils/format';

type Props = {
  medicineId?: string;
  onDone: () => void; // volta para a lista
};

export function MedicineFormScreen({ medicineId, onDone }: Props) {
  const { medicines, routines, createMedicine, updateMedicine, deleteMedicine } = useMedStore();
  const editing = medicines.find((m) => m.id === medicineId && m.fl_active);

  // Estado do formulário: tudo como TEXTO (é o que o TextInput entrega)
  const [name, setName] = useState(editing?.name ?? '');
  const [dosage, setDosage] = useState(editing?.dosage ?? '');
  const [quantity, setQuantity] = useState(String(editing?.quantity ?? 1));
  const [stock, setStock] = useState(String(editing?.stock ?? 0));
  const [usageType, setUsageType] = useState(editing?.usage_type ?? '');
  const [instructions, setInstructions] = useState(editing?.usage_instructions ?? '');
  const [description, setDescription] = useState(editing?.description ?? '');
  const [times, setTimes] = useState<string[]>(
    editing
      ? routines.filter((r) => r.medicine_id === editing.id && r.fl_active).map((r) => r.time.slice(0, 5)).sort()
      : []
  );
  const [newTime, setNewTime] = useState('');
  const [errors, setErrors] = useState<Record<string, string>>({});

  function addTime() {
    if (!isValidTime(newTime)) return setErrors({ ...errors, time: 'Use o formato HH:MM, ex.: 08:00' });
    if (times.includes(newTime)) return setErrors({ ...errors, time: 'Esse horário já está na lista' });
    setTimes([...times, newTime].sort());
    setNewTime('');
    setErrors({ ...errors, time: '' });
  }

  // Validação espelha as regras do banco (tables.sql)
  function validate() {
    const e: Record<string, string> = {};
    if (!name.trim()) e.name = 'Informe o nome';
    if (!dosage.trim()) e.dosage = 'Informe a dosagem';
    if (!/^\d+$/.test(quantity) || Number(quantity) <= 0) e.quantity = 'Número inteiro maior que zero';
    if (!/^\d+$/.test(stock)) e.stock = 'Número inteiro (0 ou mais)';
    setErrors(e);
    return Object.keys(e).length === 0;
  }

  function save() {
    if (!validate()) return;

    // O back recusa nome + dosagem repetidos (400 "Medicamento já existe.")
    const duplicate = medicines.some(
      (m) => m.fl_active && m.id !== medicineId && m.name === name.trim() && m.dosage === dosage.trim()
    );
    if (duplicate) return Alert.alert('Já cadastrado', 'Existe um medicamento com esse nome e dosagem.');

    const input = {
      name: name.trim(),
      dosage: dosage.trim(),
      quantity: Number(quantity),
      stock: Number(stock),
      usage_type: emptyToNull(usageType),
      usage_instructions: emptyToNull(instructions),
      description: emptyToNull(description),
    };
    if (editing) updateMedicine(editing.id, input, times);
    else createMedicine(input, times);
    onDone();
  }

  function confirmDelete() {
    if (!editing) return;
    Alert.alert('Excluir medicamento?', `${editing.name} e seus horários deixarão de aparecer.`, [
      { text: 'Cancelar', style: 'cancel' },
      { text: 'Excluir', style: 'destructive', onPress: () => { deleteMedicine(editing.id); onDone(); } },
    ]);
  }

  return (
    <KeyboardAvoidingView style={{ flex: 1 }} behavior={Platform.OS === 'ios' ? 'padding' : undefined}>
      <ScrollView style={styles.container} contentContainerStyle={{ padding: spacing.md }} keyboardShouldPersistTaps="handled">
        <Section title="Dados do medicamento">
          <AppInput label="Nome *" value={name} onChangeText={setName} error={errors.name} placeholder="Ex.: Losartana" />
          <AppInput label="Dosagem *" value={dosage} onChangeText={setDosage} error={errors.dosage} placeholder="Ex.: 50 mg" />
          <AppInput label="Quantidade por dose *" value={quantity} onChangeText={setQuantity} error={errors.quantity} keyboardType="number-pad" />
          <AppInput label="Estoque atual (unidades)" value={stock} onChangeText={setStock} error={errors.stock} keyboardType="number-pad" />
          <AppInput label="Tipo de uso" value={usageType} onChangeText={setUsageType} placeholder="Ex.: Oral, Tópico" />
          <AppInput label="Instruções de uso" value={instructions} onChangeText={setInstructions} placeholder="Ex.: Após o café" />
          <AppInput label="Descrição" value={description} onChangeText={setDescription} multiline />
        </Section>

        <Section title="Horários">
          <View style={styles.chips}>
            {times.length === 0 && <Text style={styles.hint}>Nenhum horário. Sem horário, não aparece em Hoje.</Text>}
            {times.map((t) => (
              <Pressable
                key={t}
                onPress={() => setTimes(times.filter((x) => x !== t))}
                accessibilityLabel={`Remover horário ${t}`}
                style={styles.chip}
              >
                <Text style={styles.chipText}>{t}  ✕</Text>
              </Pressable>
            ))}
          </View>
          <AppInput label="Novo horário" value={newTime} onChangeText={setNewTime} placeholder="HH:MM" keyboardType="numbers-and-punctuation" maxLength={5} error={errors.time} />
          <AppButton title="Adicionar horário" variant="secondary" onPress={addTime} />
        </Section>

        <View style={{ gap: spacing.sm }}>
          <AppButton title={editing ? 'Salvar alterações' : 'Cadastrar'} onPress={save} />
          {editing && <AppButton title="Excluir medicamento" variant="danger" onPress={confirmDelete} />}
        </View>
      </ScrollView>
    </KeyboardAvoidingView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: colors.background },
  chips: { flexDirection: 'row', flexWrap: 'wrap', gap: spacing.sm, marginBottom: spacing.md },
  chip: { backgroundColor: palette.blue100, borderRadius: radius.pill, paddingHorizontal: spacing.md, paddingVertical: spacing.sm },
  chipText: { ...typography.caption, color: colors.text },
  hint: { ...typography.caption, color: colors.textMuted },
});

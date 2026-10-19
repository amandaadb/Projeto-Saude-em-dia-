// Rota única para criar e editar: /medicamento/novo  ou  /medicamento/<id>
import { Stack, router, useLocalSearchParams } from 'expo-router';
import { MedicineFormScreen } from '../../screens/MedicineFormScreen';

export default function MedicamentoForm() {
  const { id } = useLocalSearchParams<{ id: string }>();
  const isNew = id === 'novo';

  return (
    <>
      <Stack.Screen options={{ title: isNew ? 'Novo medicamento' : 'Editar medicamento' }} />
      <MedicineFormScreen medicineId={isNew ? undefined : id} onDone={() => router.back()} />
    </>
  );
}

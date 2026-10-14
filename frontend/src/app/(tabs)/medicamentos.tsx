import { router } from 'expo-router';
import { MedicinesScreen } from '../../screens/MedicinesScreen';

export default function MedicamentosTab() {
  return (
    <MedicinesScreen
      onAdd={() => router.push('/medicamento/novo')}
      onEdit={(id) => router.push(`/medicamento/${id}`)}
    />
  );
}

// Layout RAIZ: carrega fontes, liga o store e define a pilha de telas.
// ⚠️ Se a navegação já feita pelo time usa outros nomes/arquivos,
// adapte só ESTA pasta src/app/ — as telas em src/screens não mudam.
import { Stack } from 'expo-router';
import { MedStoreProvider } from '../store/MedStore';
import { useAppFonts } from '../theme/useAppFonts';
import { colors, typography } from '../theme';

export default function RootLayout() {
  const fontsLoaded = useAppFonts();
  if (!fontsLoaded) return null;

  return (
    <MedStoreProvider>
      <Stack
        screenOptions={{
          headerStyle: { backgroundColor: colors.background },
          headerTitleStyle: { ...typography.subtitle, color: colors.text },
          headerTintColor: colors.primaryStrong,
          headerShadowVisible: false,
        }}
      >
        <Stack.Screen name="(tabs)" options={{ headerShown: false }} />
        <Stack.Screen name="medicamento/[id]" options={{ presentation: 'modal' }} />
      </Stack>
    </MedStoreProvider>
  );
}

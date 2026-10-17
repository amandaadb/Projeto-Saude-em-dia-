// Carrega Inter e Nunito Sans antes de mostrar o app.
// Instalar (na raiz do projeto):
//   npx expo install expo-font expo-splash-screen @expo-google-fonts/inter @expo-google-fonts/nunito-sans
//
// Uso no layout raiz (app/_layout.tsx ou App.tsx):
//   const fontsLoaded = useAppFonts();
//   if (!fontsLoaded) return null;   // segura a splash até as fontes chegarem
import { useFonts } from 'expo-font';
import {
  Inter_400Regular,
  Inter_500Medium,
  Inter_600SemiBold,
  Inter_700Bold,
} from '@expo-google-fonts/inter';
import { NunitoSans_400Regular } from '@expo-google-fonts/nunito-sans';

export function useAppFonts() {
  const [loaded] = useFonts({
    Inter_400Regular,
    Inter_500Medium,
    Inter_600SemiBold,
    Inter_700Bold,
    NunitoSans_400Regular,
  });
  return loaded;
}

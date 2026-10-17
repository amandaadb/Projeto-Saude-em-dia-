import { Alert } from 'react-native';
import { SettingsScreen } from '../../screens/SettingsScreen';

export default function AjustesTab() {
  // Login/cadastro não estão no escopo desta semana.
  // Na integração: apagar o token salvo e router.replace('/login').
  return <SettingsScreen onLogout={() => Alert.alert('Sair', 'Fluxo de login ainda não implementado.')} />;
}

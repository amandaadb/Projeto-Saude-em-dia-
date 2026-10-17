// ABA AJUSTES — perfil, dados da conta e preferências de notificação.
// Perfil/conta: GET e PUT /api/auth/me. Exclusão: DELETE /api/auth/delete-account.
import { useState } from 'react';
import { ScrollView, Alert, View, KeyboardAvoidingView, Platform } from 'react-native';
import { spacing } from '../theme';
import { Screen } from '../components/Screen';
import { Section } from '../components/Section';
import { AppInput } from '../components/AppInput';
import { AppButton } from '../components/AppButton';
import { SwitchRow } from '../components/SwitchRow';
import { useMedStore } from '../store/MedStore';
import { brDateToIso, emptyToNull, isoToBrDate } from '../utils/format';

type Props = {
  onLogout: () => void; // apaga o token e volta p/ login (fluxo de auth)
};

export function SettingsScreen({ onLogout }: Props) {
  const { user, updateUser, notificationPrefs, setNotificationPrefs } = useMedStore();

  // ----- Perfil (dados pessoais e de saúde) -----
  const [name, setName] = useState(user.name);
  const [birth, setBirth] = useState(isoToBrDate(user.dt_birth));
  const [bloodType, setBloodType] = useState(user.blood_type ?? '');
  const [allergies, setAllergies] = useState(user.allergies ?? '');
  const [conditions, setConditions] = useState(user.chronic_conditions ?? '');
  const [emergencyName, setEmergencyName] = useState(user.emergency_contact_name ?? '');
  const [emergencyPhone, setEmergencyPhone] = useState(user.emergency_contact_phone ?? '');

  // ----- Conta (login e contato) -----
  const [email, setEmail] = useState(user.email);
  const [phone, setPhone] = useState(user.phone);
  const [password, setPassword] = useState('');

  const [errors, setErrors] = useState<Record<string, string>>({});

  function saveProfile() {
    const iso = brDateToIso(birth);
    const e: Record<string, string> = {};
    if (!name.trim()) e.name = 'Informe o nome';
    if (!iso) e.birth = 'Data inválida (DD/MM/AAAA)';
    setErrors(e);
    if (Object.keys(e).length) return;

    updateUser({
      name: name.trim(),
      dt_birth: iso!,
      blood_type: emptyToNull(bloodType),
      allergies: emptyToNull(allergies),
      chronic_conditions: emptyToNull(conditions),
      emergency_contact_name: emptyToNull(emergencyName),
      emergency_contact_phone: emptyToNull(emergencyPhone),
    });
    Alert.alert('Perfil atualizado ✅');
  }

  function saveAccount() {
    const e: Record<string, string> = {};
    if (!/^\S+@\S+\.\S+$/.test(email)) e.email = 'E-mail inválido';
    if (!phone.trim()) e.phone = 'Informe o telefone';
    if (password && password.length < 6) e.password = 'Mínimo de 6 caracteres';
    setErrors(e);
    if (Object.keys(e).length) return;

    // Na API: PUT /api/auth/me { email, phone, password? } — senha só se preenchida.
    // No mock a senha não é guardada (a API nunca devolve senha).
    updateUser({ email: email.trim(), phone: phone.trim() });
    setPassword('');
    Alert.alert('Conta atualizada ✅');
  }

  function confirmDeleteAccount() {
    Alert.alert('Excluir conta?', 'Seus dados deixarão de ser acessíveis. Essa ação não pode ser desfeita pelo app.', [
      { text: 'Cancelar', style: 'cancel' },
      { text: 'Excluir', style: 'destructive', onPress: onLogout },
    ]);
  }

  return (
    <Screen title="Ajustes">
      <KeyboardAvoidingView style={{ flex: 1 }} behavior={Platform.OS === 'ios' ? 'padding' : undefined}>
        <ScrollView contentContainerStyle={{ padding: spacing.md, paddingTop: spacing.sm }} keyboardShouldPersistTaps="handled">
          <Section title="👤 Perfil">
            <AppInput label="Nome" value={name} onChangeText={setName} error={errors.name} />
            <AppInput label="Data de nascimento" value={birth} onChangeText={setBirth} error={errors.birth} placeholder="DD/MM/AAAA" keyboardType="numbers-and-punctuation" maxLength={10} />
            <AppInput label="Tipo sanguíneo" value={bloodType} onChangeText={setBloodType} placeholder="Ex.: O+" maxLength={3} autoCapitalize="characters" />
            <AppInput label="Alergias" value={allergies} onChangeText={setAllergies} multiline />
            <AppInput label="Condições crônicas" value={conditions} onChangeText={setConditions} multiline />
            <AppInput label="Contato de emergência" value={emergencyName} onChangeText={setEmergencyName} placeholder="Nome" />
            <AppInput label="Telefone de emergência" value={emergencyPhone} onChangeText={setEmergencyPhone} keyboardType="phone-pad" />
            <AppButton title="Salvar perfil" onPress={saveProfile} />
          </Section>

          <Section title="🔐 Dados da conta">
            <AppInput label="E-mail" value={email} onChangeText={setEmail} error={errors.email} keyboardType="email-address" autoCapitalize="none" />
            <AppInput label="Telefone" value={phone} onChangeText={setPhone} error={errors.phone} keyboardType="phone-pad" />
            <AppInput label="Nova senha (opcional)" value={password} onChangeText={setPassword} error={errors.password} secureTextEntry />
            <AppButton title="Salvar conta" onPress={saveAccount} />
          </Section>

          <Section title="🔔 Notificações">
            <SwitchRow
              label="Lembrete de dose"
              description="Aviso no horário de cada medicamento"
              value={notificationPrefs.doseReminders}
              onChange={(v) => setNotificationPrefs({ ...notificationPrefs, doseReminders: v })}
            />
            <SwitchRow
              label="Alerta de estoque baixo"
              description="Aviso quando um remédio estiver acabando"
              value={notificationPrefs.lowStockAlerts}
              onChange={(v) => setNotificationPrefs({ ...notificationPrefs, lowStockAlerts: v })}
            />
          </Section>

          <View style={{ gap: spacing.sm, marginBottom: spacing.xl }}>
            <AppButton title="Sair" variant="secondary" onPress={onLogout} />
            <AppButton title="Excluir conta" variant="danger" onPress={confirmDeleteAccount} />
          </View>
        </ScrollView>
      </KeyboardAvoidingView>
    </Screen>
  );
}

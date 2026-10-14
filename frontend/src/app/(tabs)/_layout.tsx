// As 4 abas. Ícones do Ionicons (já vem no Expo via @expo/vector-icons).
import { Tabs } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';
import { ComponentProps } from 'react';
import { ColorValue } from 'react-native';
import { colors, fonts } from '../../theme';

type IconName = ComponentProps<typeof Ionicons>['name'];

const tab = (title: string, icon: IconName) => ({
  title,
  tabBarIcon: ({ color, size }: { color: ColorValue; size: number }) => (
    <Ionicons name={icon} size={size} color={color} />
  ),
});

export default function TabsLayout() {
  return (
    <Tabs
      screenOptions={{
        headerShown: false,
        tabBarActiveTintColor: colors.primaryStrong,
        tabBarInactiveTintColor: colors.textMuted,
        tabBarLabelStyle: { fontFamily: fonts.medium, fontSize: 12 },
        tabBarItemStyle: { paddingVertical: 4 },
        tabBarStyle: { backgroundColor: colors.surface, borderTopColor: colors.border, minHeight: 60 },
      }}
    >
      <Tabs.Screen name="index" options={tab('Hoje', 'today-outline')} />
      <Tabs.Screen name="medicamentos" options={tab('Medicamentos', 'medkit-outline')} />
      <Tabs.Screen name="historico" options={tab('Histórico', 'time-outline')} />
      <Tabs.Screen name="ajustes" options={tab('Ajustes', 'settings-outline')} />
    </Tabs>
  );
}

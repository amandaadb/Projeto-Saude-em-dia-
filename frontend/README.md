# Front-end - MedControl

> Aplicativo móvel do MedControl, desenvolvido em **React Native + Expo (SDK 57)** com **Expo Router**. Nesta etapa, o app utiliza **dados de teste** (`src/mocks/`); a integração com a API do `backend/` será feita em uma próxima etapa.

Documentação relacionada: [Leia-me principal](../README.md) · [Back-end](../backend/README.md) · [UI/UX](../UI-UX.md) · [Componentes](../COMPONENTS.md) · [Acessibilidade](../ACCESSIBILITY.md) · [Protótipo](../docs/prototipo.md) · [Changelog](../CHANGELOG.md) · [Contribuindo](../CONTRIBUTING.md)

---

## Tecnologias

| Tecnologia | Uso |
| :--- | :--- |
| **React Native** | Desenvolvimento do aplicativo móvel |
| **Expo (SDK 57)** | Ambiente de desenvolvimento e execução |
| **Expo Router** | Navegação baseada em arquivos (rotas) |
| **TypeScript** | Tipagem dos dados, espelhando `backend/models.py` |
| **Inter e Nunito Sans** | Fontes (via `@expo-google-fonts`) |

## Como rodar?

### Pré-requisitos

- [Node.js LTS](https://nodejs.org) instalado no computador;
- Aplicativo **Expo Go** instalado no celular.

### Passo a passo

```bash
cd frontend
npm install        # baixa as dependências (cria a pasta node_modules)
npx expo start     # exibe um QR code no terminal
```

Abra o **Expo Go** no celular e leia o QR code.

> **Atenção:** o computador e o celular precisam estar conectados à **mesma rede Wi-Fi**.

### Scripts disponíveis

| Comando | O que faz |
| :--- | :--- |
| `npm start` | Inicia o servidor de desenvolvimento |
| `npm run android` | Abre no Android |
| `npm run ios` | Abre no iOS |
| `npm run web` | Abre no navegador |
| `npm run lint` | Verifica o código com o lint do Expo |
| `npx tsc --noEmit` | Verifica os tipos do TypeScript |

## Variáveis de ambiente

| Variável | Para que serve | Padrão |
| :--- | :--- | :--- |
| `EXPO_PUBLIC_API_URL` | Endereço da API | `http://localhost:8000` |

No celular físico, `localhost` é o próprio celular. Use o IP do computador que roda o back-end, por exemplo `http://192.168.0.10:8000`. Crie um arquivo `.env.local` (ignorado pelo Git) com essa variável. Nunca coloque chaves secretas (como a service key do Supabase) no front-end: tudo que começa com `EXPO_PUBLIC_` fica visível no aplicativo.

## Estrutura do projeto

```text
src/
├── app/          rotas (Expo Router): 4 abas + formulário de medicamento
├── screens/      telas (Hoje, Medicamentos, Formulário, Histórico, Ajustes)
├── components/   componentes reutilizáveis (veja COMPONENTS.md)
├── store/        estado compartilhado entre as abas (MedStore)
├── services/     cliente da API (pronto, ainda não utilizado)
├── theme/        paleta e tipografia oficiais (UI-UX.md)
├── types/        tipos espelhando backend/models.py
├── utils/        cálculo de status das doses e formatação
└── mocks/        dados de teste
```

## Como os dados fluem

1. As telas leem e alteram os dados pelo `MedStore` (`useMedStore()`), a única fonte de estado do app;
2. Hoje, o `MedStore` guarda tudo na memória, a partir de `mocks/data`. **Ao fechar o app, as alterações se perdem**;
3. Na integração, o corpo de cada função do `MedStore` passa a chamar `services/api.ts`. Cada função já traz, em comentário, o endpoint correspondente.

## Estados visuais

| Estado | Origem |
| :--- | :--- |
| **Tomado** | `history.fl_taken = true` |
| **Não tomado** | `history.fl_taken = false` |
| **Pendente** | Rotina de hoje **sem** registro em `history` (calculado no front-end, em `utils/doses.ts`) |
| **Estoque baixo** | `medicines.stock` menor ou igual ao limite (valor provisório: 5) |

## Telas

| Tela | Arquivo | Observação |
| :--- | :--- | :--- |
| Hoje | `screens/TodayScreen.tsx` | Resumo, próxima dose e registro de dose |
| Medicamentos | `screens/MedicinesScreen.tsx` | Lista e ajuste de estoque |
| Formulário | `screens/MedicineFormScreen.tsx` | Cadastro, edição, exclusão e horários |
| Histórico | `screens/HistoryScreen.tsx` | Agrupado por dia, com filtro |
| Ajustes | `screens/SettingsScreen.tsx` | Perfil, conta, notificações, sair e excluir conta |

## Pendências conhecidas da integração

Para a equipe do front-end e do back-end alinharem antes de ligar o app à API:

- O cliente `services/api.ts` ainda **não tem a função de cadastro** (`/api/auth/register`);
- A **exclusão de conta** em Ajustes hoje apenas faz logout (no mock). Na API, é uma exclusão lógica;
- Ao excluir um medicamento, o back-end **não desativa as rotinas**; o app precisa chamar a exclusão de cada rotina;
- O back-end aceita registrar a **mesma dose duas vezes**; o app impede isso (só dose pendente pode ser registrada);
- O filtro por `days_of_week` ainda não existe (`TODO` em `utils/doses.ts`), porque o formato dos valores não foi definido;
- As preferências de notificação ficam só no aparelho e **não têm efeito**: o app não envia notificações. Com os lembretes por WhatsApp, a preferência e o número passarão a ser **guardados no servidor**, então será preciso novo contrato com o back-end (campos e endpoints), e a tela de Ajustes deverá pedir o consentimento de forma separada;
- O registro de dose usa `Alert.alert`, e a tela de login precisa ser confirmada ou criada;
- As notificações do celular e a integração com Google Agenda e com o calendário do aparelho são etapas futuras e ainda não têm biblioteca instalada nem permissões configuradas.

## Acessibilidade

Antes de abrir um Pull Request com mudança visual, siga o checklist de [ACCESSIBILITY.md](../ACCESSIBILITY.md). As divergências já conhecidas entre o app e as regras do projeto estão em [COMPONENTS.md](../COMPONENTS.md#divergências-conhecidas).

---

> O MedControl é uma ferramenta de organização e **não substitui orientação médica**.
---

© 2026 MedControl. Todos os direitos reservados.

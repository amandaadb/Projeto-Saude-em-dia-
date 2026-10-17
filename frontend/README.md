# MedControl — Front-end

App em **React Native + Expo (SDK 57)** com **Expo Router**. Esta etapa usa **dados de teste** (`src/mocks/`); a integração com a API do `backend/` vem depois.

## ▶️ Como rodar

Pré-requisitos: [Node.js LTS](https://nodejs.org) no computador e o app **Expo Go** no celular.

```bash
cd frontend
npm install        # baixa as dependências (cria a pasta node_modules)
npx expo start     # mostra um QR code
```

Abra o **Expo Go** e leia o QR code (computador e celular na mesma rede Wi-Fi).

## 🗂️ Estrutura

```
src/
├── app/          rotas (Expo Router): 4 abas + formulário de medicamento
├── screens/      telas (Hoje, Medicamentos, Formulário, Histórico, Ajustes)
├── components/   componentes reutilizáveis (botão, campo, card, badge...)
├── store/        estado compartilhado entre as abas (MedStore)
├── services/     cliente da API (pronto, ainda não usado)
├── theme/        paleta e tipografia oficiais (UI-UX.md)
├── types/        tipos espelhando backend/models.py
├── utils/        cálculo de status das doses e formatação
└── mocks/        dados de teste
```

## 🎨 Estados visuais

| Estado | Origem |
|---|---|
| ✅ Tomado | `history.fl_taken = true` |
| ❌ Não tomado | `history.fl_taken = false` |
| ⏰ Pendente | rotina de hoje **sem** registro no `history` (calculado no front) |
| ⚠️ Estoque baixo | `medicines.stock` ≤ limite (provisório: 5) |

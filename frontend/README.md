# Front-end - MedControl

> Aplicativo móvel do MedControl, desenvolvido em **React Native + Expo (SDK 57)** com **Expo Router**. Nesta etapa, o app utiliza **dados de teste** (`src/mocks/`); a integração com a API do `backend/` será feita em uma próxima etapa.

Documentação relacionada: [Leia-me principal](../README.md) · [UI/UX](../UI-UX.md) · [Componentes](../COMPONENTS.md) · [Acessibilidade](../ACCESSIBILITY.md) · [Protótipo](../docs/prototipo.md) · [Changelog](../CHANGELOG.md) · [Contribuindo](../CONTRIBUTING.md)

---

## Tecnologias

| Tecnologia | Uso |
| :--- | :--- |
| **React Native** | Desenvolvimento do aplicativo móvel |
| **Expo (SDK 57)** | Ambiente de desenvolvimento e execução |
| **Expo Router** | Navegação baseada em arquivos (rotas) |
| **TypeScript** | Tipagem dos dados, espelhando `backend/models.py` |

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

## Estrutura do projeto

```text
src/
├── app/          rotas (Expo Router): 4 abas + formulário de medicamento
├── screens/      telas (Hoje, Medicamentos, Formulário, Histórico, Ajustes)
├── components/   componentes reutilizáveis (botão, campo, card, badge etc.)
├── store/        estado compartilhado entre as abas (MedStore)
├── services/     cliente da API (pronto, ainda não utilizado)
├── theme/        paleta e tipografia oficiais (UI-UX.md)
├── types/        tipos espelhando backend/models.py
├── utils/        cálculo de status das doses e formatação
└── mocks/        dados de teste
```

## Estados visuais

| Estado | Origem |
| :--- | :--- |
| **Tomado** | `history.fl_taken = true` |
| **Não tomado** | `history.fl_taken = false` |
| **Pendente** | Rotina de hoje **sem** registro em `history` (calculado no front-end) |
| **Estoque baixo** | `medicines.stock` menor ou igual ao limite (valor provisório: 5) |

---

> O MedControl é uma ferramenta de organização e **não substitui orientação médica**.

---

© 2026 MedControl. Todos os direitos reservados.

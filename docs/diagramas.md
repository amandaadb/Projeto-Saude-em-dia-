# Diagramas - MedControl

> Fluxogramas e diagramas que descrevem o funcionamento, a arquitetura e os dados do aplicativo, conforme o código atual.

A fonte do modelo de dados é o `backend/tables.sql`. Se o banco mudar, atualize este documento no mesmo Pull Request.

## Arquitetura

Situação atual: o app usa dados de teste e ainda não chama a API.

```mermaid
flowchart LR
    T["Telas<br/>(Hoje, Medicamentos, Histórico, Ajustes)"] --> S["MedStore<br/>(estado do app)"]
    S --> M["Dados de teste<br/>(mocks)"]
    S -.->|"próxima etapa"| C["Cliente da API<br/>(services/api.ts)"]
    C -.->|"HTTP + JWT"| B["API FastAPI"]
    B --> D[("Supabase<br/>PostgreSQL")]
    B -.->|"planejado: lembretes"| W["Provedor de WhatsApp"]
    W -.-> U(["WhatsApp do usuário"])
    B -.->|"planejado: agenda"| G["Google Agenda"]
    S -.->|"planejado"| N["Notificações e calendário do celular"]
```

As linhas tracejadas ainda **não estão ligadas**. Os lembretes por WhatsApp partem do servidor; as notificações e o calendário do celular são tratados no próprio aparelho.

## Casos de uso

```mermaid
flowchart LR
    U(["Usuário"])

    subgraph MedControl
        UC1(["Criar conta e fazer login"])
        UC2(["Gerenciar medicamentos e horários"])
        UC3(["Ver as doses do dia"])
        UC4(["Registrar dose"])
        UC5(["Consultar histórico"])
        UC6(["Ajustar estoque"])
        UC7(["Editar perfil e dados de saúde"])
        UC8(["Excluir conta"])
    end

    U --> UC1
    U --> UC2
    U --> UC3
    U --> UC4
    U --> UC5
    U --> UC6
    U --> UC7
    U --> UC8
```

## Fluxograma: cadastro e login

Fluxo do back-end. A tela de login do app precisa ser confirmada.

```mermaid
flowchart TD
    A([Início]) --> B{Possui conta?}
    B -- Não --> C[Informar dados do cadastro]
    C --> D{E-mail já cadastrado?}
    D -- Sim --> E[Exibir erro]
    E --> C
    D -- Não --> F[Criar conta e gerar token JWT]
    B -- Sim --> G[Informar e-mail e senha]
    G --> H{Credenciais corretas?}
    H -- Não --> I[Exibir erro]
    I --> G
    H -- Sim --> F
    F --> J([Tela inicial])
```

## Fluxograma: status da dose

O status de cada dose de hoje é calculado no app. O banco só guarda o que **aconteceu** (histórico).

```mermaid
flowchart TD
    A[Rotina ativa de um medicamento ativo] --> B{Existe registro<br/>dessa rotina hoje?}
    B -- Não --> C[Pendente]
    B -- Sim --> D{Foi tomada?}
    D -- Sim --> E[Tomada]
    D -- Não --> F[Não tomada]
```

## Fluxograma: registro de dose

```mermaid
flowchart TD
    A([Aba Hoje]) --> B{Status da dose}
    B -- "Tomada ou não tomada" --> C[Nada acontece]
    B -- Pendente --> D[Usuário toca na dose]
    D --> E{Escolha}
    E -- Cancelar --> A
    E -- "Tomei" --> F[Registrar como tomada]
    E -- "Não tomei" --> G[Registrar como não tomada]
    F --> H[Aparece no Histórico]
    G --> H
```

O registro **não desconta o estoque**. O estoque só muda quando a pessoa usa os botões de + e - em Medicamentos. Os lembretes (WhatsApp, notificações do celular e agendas) ainda não existem.

## Fluxograma: gestão de medicamentos

```mermaid
flowchart TD
    A([Aba Medicamentos]) --> B{Ação desejada}
    B -- Adicionar --> C[Preencher formulário e horários]
    C --> D[Cadastrar medicamento e uma rotina por horário]
    B -- "Tocar no card" --> E[Editar dados e horários]
    E --> F[Salvar alterações]
    E --> G{Excluir?}
    G -- Sim --> H[Confirmar]
    H --> I[Desativar medicamento e suas rotinas]
    B -- "+ ou -" --> J[Ajustar estoque]
    D --> A
    F --> A
    I --> A
    J --> A
```

## Diagrama de sequência: login

```mermaid
sequenceDiagram
    actor U as Usuário
    participant App as Aplicativo
    participant API as API FastAPI
    participant DB as Supabase

    U->>App: Informa e-mail e senha
    App->>API: POST /api/auth/login
    API->>DB: Busca usuário ativo pelo e-mail
    DB-->>API: Dados do usuário
    alt Credenciais válidas
        API-->>App: Token JWT (7 dias)
        App-->>U: Acesso liberado
    else Credenciais inválidas
        API-->>App: Erro 401
        App-->>U: Exibe mensagem de erro
    end
```

## Diagrama de sequência: registro de dose

Sequência prevista para quando o app estiver integrado.

```mermaid
sequenceDiagram
    actor U as Usuário
    participant App as Aplicativo
    participant API as API FastAPI
    participant DB as Supabase

    U->>App: Toca na dose pendente e escolhe Tomei ou Não tomei
    App->>API: POST /api/history (routine_id, fl_taken)
    API->>DB: Confere se a rotina é do usuário
    alt Rotina encontrada
        API->>DB: Grava no histórico
        API-->>App: Registro criado
        App-->>U: Dose passa a Tomada ou Não tomada
    else Rotina não encontrada
        API-->>App: Erro 404
        App-->>U: Exibe mensagem de erro
    end
```

## Diagrama de sequência: lembrete por WhatsApp (planejado)

Ainda **não implementado**. Mostra o fluxo previsto quando o envio for criado.

```mermaid
sequenceDiagram
    participant AG as Agendador (servidor)
    participant API as API FastAPI
    participant DB as Supabase
    participant WA as Provedor de WhatsApp
    actor U as Usuário

    AG->>API: Verifica rotinas que vencem agora
    API->>DB: Busca rotinas ativas de usuários com lembrete ativado
    DB-->>API: Rotinas e números de WhatsApp
    loop Para cada dose no horário
        API->>WA: Envia mensagem genérica ao número
        WA-->>U: "Está na hora do seu medicamento"
        WA-->>API: Confirmação de envio ou erro
    end
    U->>API: Registra "Tomei" ou "Não tomei" no app
    API->>DB: Grava no histórico
```

O lembrete **não registra** a dose: quem registra é a pessoa, no app. A mensagem não cita o nome do medicamento (veja [privacidade.md](./privacidade.md)).

## Modelo entidade-relacionamento

Conforme `tables.sql`. As tabelas `users`, `medicines` e `routines` usam exclusão lógica (`fl_active`); `history` não tem esse campo.

```mermaid
erDiagram
    USERS ||--o{ MEDICINES : possui
    USERS ||--o{ ROUTINES : possui
    USERS ||--o{ HISTORY : possui
    MEDICINES ||--o{ ROUTINES : "tem horários"
    ROUTINES ||--o{ HISTORY : "gera registros"

    USERS {
        uuid id PK
        text name
        text email UK
        text phone
        text password_hash
        date dt_birth
        text blood_type
        text emergency_contact_name
        text emergency_contact_phone
        text allergies
        text chronic_conditions
        boolean fl_active
        timestamptz dt_created
        timestamptz dt_updated
    }

    MEDICINES {
        uuid id PK
        uuid user_id FK
        text name
        text dosage
        int quantity
        text usage_type
        text usage_instructions
        int stock
        text description
        boolean fl_active
        timestamptz dt_created
        timestamptz dt_updated
    }

    ROUTINES {
        uuid id PK
        uuid user_id FK
        uuid medicine_id FK
        time time
        text days_of_week
        boolean fl_active
        timestamptz dt_created
        timestamptz dt_updated
    }

    HISTORY {
        uuid id PK
        uuid routine_id FK
        uuid user_id FK
        timestamptz dt_hour
        boolean fl_taken
        timestamptz dt_created
    }
```

Restrições do banco: `quantity > 0`, `stock >= 0` e `users.email` único.

> Os diagramas representam o escopo do MVP. O modo cuidador, as consultas e receitas, as recompensas, os lembretes (WhatsApp e notificações do celular) e a integração com agendas serão adicionados quando forem desenvolvidos. O diagrama de lembrete por WhatsApp acima é uma previsão.

# Diagramas - MedControl

> Fluxogramas e diagramas UML que descrevem o funcionamento, a arquitetura e os dados do aplicativo.

## Arquitetura

```mermaid
flowchart LR
    A["App Mobile<br/>(Front-end)"] -->|"HTTP + JWT"| B["API FastAPI<br/>(Back-end)"]
    B -->|"Consultas e gravações"| C[("Supabase<br/>Banco de dados")]
    B -.->|"Valida token"| D["Autenticação JWT"]
```

## Casos de uso

```mermaid
flowchart LR
    U(["Usuário"])

    subgraph MedControl
        UC1(["Criar conta e fazer login"])
        UC2(["Gerenciar medicamentos"])
        UC3(["Receber lembretes"])
        UC4(["Registrar dose"])
        UC5(["Consultar histórico"])
        UC6(["Controlar estoque"])
    end

    U --> UC1
    U --> UC2
    U --> UC3
    U --> UC4
    U --> UC5
    U --> UC6
    UC4 -.->|"atualiza"| UC6
```

## Fluxograma: cadastro e login

```mermaid
flowchart TD
    A([Início]) --> B[Abrir o aplicativo]
    B --> C{Possui conta?}
    C -- Não --> D[Preencher cadastro]
    D --> E{Dados válidos?}
    E -- Não --> D
    E -- Sim --> F[Criar conta]
    F --> G[Tela de login]
    C -- Sim --> G
    G --> H[Informar e-mail e senha]
    H --> I{Credenciais corretas?}
    I -- Não --> J[Exibir mensagem de erro]
    J --> H
    I -- Sim --> K[Gerar token JWT]
    K --> L[Manter usuário logado]
    L --> M([Tela inicial])
```

## Fluxograma: lembrete e registro de dose

```mermaid
flowchart TD
    A([Chegou o horário da dose]) --> B[Enviar notificação]
    B --> C{Resposta do usuário}
    C -- Tomei --> D[Registrar dose como tomada]
    D --> E[Descontar do estoque]
    E --> F{Estoque abaixo do mínimo?}
    F -- Sim --> G[Enviar alerta de estoque baixo]
    F -- Não --> H([Fim])
    G --> H
    C -- Adiar --> I[Registrar dose como adiada]
    I --> J[Reagendar lembrete]
    J --> B
    C -- Sem resposta --> K[Registrar dose como perdida]
    K --> H
```

## Fluxograma: gestão de medicamentos

```mermaid
flowchart TD
    A([Tela de medicamentos]) --> B{Ação desejada}
    B -- Cadastrar --> C[Informar nome, dose, frequência, horários e estoque]
    C --> D[Salvar medicamento]
    B -- Editar --> E[Selecionar medicamento]
    E --> F[Alterar dados]
    F --> D
    B -- Excluir --> G[Selecionar medicamento]
    G --> H{Confirmar exclusão?}
    H -- Sim --> I[Remover medicamento]
    H -- Não --> A
    B -- Listar --> J[Exibir medicamentos do usuário]
    D --> A
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
    App->>API: POST /login
    API->>DB: Busca usuário
    DB-->>API: Dados do usuário
    alt Credenciais válidas
        API-->>App: Token JWT
        App-->>U: Acesso liberado
    else Credenciais inválidas
        API-->>App: Erro de autenticação
        App-->>U: Exibe mensagem de erro
    end
```

## Diagrama de sequência: registro de dose

```mermaid
sequenceDiagram
    actor U as Usuário
    participant App as Aplicativo
    participant API as API FastAPI
    participant DB as Supabase

    App-->>U: Notificação no horário da dose
    U->>App: Marca dose como tomada
    App->>API: Registra dose (token JWT)
    API->>DB: Salva no histórico
    API->>DB: Atualiza estoque
    DB-->>API: Estoque atual
    alt Estoque abaixo do mínimo
        API-->>App: Alerta de estoque baixo
        App-->>U: Exibe alerta
    else Estoque suficiente
        API-->>App: Confirmação
    end
```

## Diagrama de classes

```mermaid
classDiagram
    class Usuario {
        +int id
        +string nome
        +string email
        +string senha_hash
        +cadastrar()
        +autenticar()
        +atualizar()
        +excluir()
    }

    class Medicamento {
        +int id
        +string nome
        +string dose
        +string frequencia
        +int estoque_atual
        +int estoque_minimo
        +cadastrar()
        +atualizar()
        +excluir()
        +verificarEstoque()
    }

    class Horario {
        +int id
        +time hora
    }

    class RegistroDose {
        +int id
        +datetime horario_previsto
        +datetime registrado_em
        +StatusDose status
        +registrar()
    }

    class StatusDose {
        <<enumeration>>
        TOMADA
        ADIADA
        PERDIDA
    }

    Usuario "1" --> "*" Medicamento : possui
    Medicamento "1" --> "*" Horario : tem
    Medicamento "1" --> "*" RegistroDose : gera
    RegistroDose --> StatusDose
```

## Modelo entidade-relacionamento

```mermaid
erDiagram
    USUARIO ||--o{ MEDICAMENTO : possui
    MEDICAMENTO ||--o{ HORARIO : tem
    MEDICAMENTO ||--o{ REGISTRO_DOSE : gera

    USUARIO {
        int id PK
        string nome
        string email
        string senha_hash
        datetime criado_em
    }

    MEDICAMENTO {
        int id PK
        int usuario_id FK
        string nome
        string dose
        string frequencia
        int estoque_atual
        int estoque_minimo
    }

    HORARIO {
        int id PK
        int medicamento_id FK
        time hora
    }

    REGISTRO_DOSE {
        int id PK
        int medicamento_id FK
        datetime horario_previsto
        datetime registrado_em
        string status
    }
```

> Os diagramas representam o escopo do MVP. O modo cuidador, as consultas e receitas e as recompensas serão adicionados quando forem desenvolvidos.

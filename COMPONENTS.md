# Componentes - MedControl

> Catálogo dos componentes reutilizáveis da interface (botões, campos, cards de medicamentos, selos de status e demais elementos), garantindo consistência visual em todo o aplicativo.

Os componentes ficam em `frontend/src/components/` e usam apenas os tokens de `frontend/src/theme/index.ts`. Os valores estão em [UI-UX.md](./UI-UX.md). Nenhum componente escreve cor ou tamanho "na mão".

> As propriedades abaixo foram levantadas pelo uso nas telas. Quem mantém cada componente deve confirmar no código e ajustar este documento.

## Como ler este documento

| Situação | Significado |
| :--- | :--- |
| Em uso | Existe e é usado nas telas; as regras de acessibilidade ainda precisam ser conferidas no código |
| Não é componente | Elemento tratado direto na tela, sem componente reutilizável |

## Componentes

| Componente | Uso | Situação |
| :--- | :--- | :--- |
| `Screen` | Estrutura de toda tela (título e fundo) | Em uso |
| `Section` | Grupo de campos com título | Em uso |
| `AppButton` | Ações principais, secundárias e de perigo | Em uso |
| `AppInput` | Entrada de dados nos formulários | Em uso |
| `MedicationCard` | Card de medicamento ou de dose | Em uso |
| `StatusBadge` | Estado da dose (e do estoque) | Em uso |
| `StockStepper` | Aumentar ou diminuir o estoque (+/-) | Em uso |
| `SwitchRow` | Interruptor com rótulo e descrição | Em uso |
| `FilterChips` | Filtro por opções (Histórico) | Em uso |
| Confirmação | Escolhas e confirmações (`Alert.alert` nativo) | Não é componente |
| Chips de horário | Lista de horários no formulário (`Pressable`) | Não é componente |

## Regras para todos os componentes

- **Alvo de toque:** mínimo de 48 x 48 dp; ação principal, como registrar dose, com 56 dp de altura;
- **Espaço entre alvos:** pelo menos 8 dp (`spacing.sm`);
- **Texto:** informação essencial (dose, horário, estoque, aviso, erro) com tamanho 16 ou mais, sem altura nem largura fixas, e sem `numberOfLines` que corte informação importante;
- **Fonte do sistema:** o texto cresce com o tamanho de fonte do aparelho;
- **Cor:** nenhuma informação depende só de cor nem só de emoji; sempre há texto;
- **Contraste:** pares de cor devem constar na tabela de [UI-UX.md](./UI-UX.md#contraste);
- **Leitor de tela:** todo elemento interativo tem `accessibilityRole` e `accessibilityLabel` que dizem a ação e o objeto; ícones decorativos ficam ocultos (`accessible={false}`).

## `Screen`

Recebe `title` e o conteúdo. Define o fundo (`background`) e o título (estilo Título, 24). O título deve ser anunciado como cabeçalho (`accessibilityRole="header"`).

## `Section`

Recebe `title` e os campos como filhos. Hoje os títulos de seção em Ajustes usam emoji ("👤 Perfil"); o emoji deve ser ocultado do leitor de tela ou removido.

## `AppButton`

Propriedades usadas: `title`, `onPress` e `variant` (`primary`, `secondary` ou `danger`).

| Variante | Fundo | Texto | Uso |
| :--- | :--- | :--- | :--- |
| Principal | `primaryStrong` (`blue900`) | `white` | Ação principal da tela |
| Secundário | `surface` com borda | `text` | Ações alternativas (sair, adicionar horário) |
| Perigo | `danger` (`pink900`) | `white` | Ações destrutivas (excluir medicamento, excluir conta) |

Regras:

- Rótulo com verbo claro ("Salvar alterações"), nunca só "OK";
- Altura mínima de 48 dp (56 dp na ação principal);
- Estado desabilitado: cor reduzida **e** motivo explicado em texto próximo;
- Evite emoji no rótulo, como em "+ Adicionar medicamento": prefira "Adicionar medicamento", com o ícone decorativo à parte.

## `AppInput`

Propriedades usadas: `label`, `value`, `onChangeText`, `error`, `placeholder`, `keyboardType`, `multiline`, `maxLength`, `secureTextEntry` e `autoCapitalize`.

| Parte | Especificação |
| :--- | :--- |
| Rótulo | Sempre visível **acima** do campo, nunca só placeholder |
| Borda | Mínimo de 3:1 sobre o fundo (veja [UI-UX.md](./UI-UX.md#contraste)) |
| Texto digitado | `text`, Inter Regular 16 |
| Erro | Mensagem abaixo, dizendo o que houve e como resolver, junto de ícone ou texto "Erro:" |

Campos obrigatórios levam `*` no rótulo ("Nome *"). Quando houver `*`, o formulário deve explicar o que ele significa.

Formatos esperados pela API (veja `frontend/src/utils/format.ts`):

| Campo | Digitado | Enviado ao back-end |
| :--- | :--- | :--- |
| Horário | `08:30` (00:00 a 23:59) | `08:30:00` |
| Data de nascimento | `20/05/1995` | `1995-05-20` |
| Campo opcional vazio | (vazio) | `null`, nunca `""` |

Mensagens de erro atuais: "Use o formato HH:MM, ex.: 08:00", "Data inválida (DD/MM/AAAA)" e "Número inteiro maior que zero".

## `MedicationCard`

Propriedades usadas: `name`, `dosage`, `time`, `subtitle`, `status`, `lowStock`, `onPress` e filhos (usado para o `StockStepper`).

Conteúdo: nome e dosagem, horário ou subtítulo, selo de status da dose, selo de estoque baixo (quando `lowStock`) e filhos.

Regras:

- Fundo `surface`, arredondamento `radius.md`, espaçamento interno `spacing.md`;
- Só é tocável quando há `onPress`. Em Hoje, apenas doses **pendentes** são tocáveis;
- Leitor de tela: um único rótulo resumido, como "Losartana 50 mg, 08:00, pendente, estoque baixo", e dica de ação ("Toque para registrar a dose") quando tocável.

## `StatusBadge`

Recebe `status` (`taken`, `pending` ou `missed`). Mostra **ícone + texto**; a cor é reforço.

| Estado | Texto | Fundo | Texto (cor) | Contraste |
| :--- | :--- | :--- | :--- | :--- |
| Tomado | Tomado | `green300` | `blue900` | 6,06:1 |
| Pendente | Pendente | `blue100` | `blue900` | 6,58:1 |
| Não tomado | Não tomado | `pink100` | `pink900` | 6,80:1 |
| Estoque baixo | Estoque baixo | `#FFE8C2` (provisório) | `#8A4B00` | 5,69:1 |

- Tokens vêm de `doseStatusStyle` e `lowStockStyle`;
- Os ícones atuais são emojis; a recomendação é trocá-los por ícones vetoriais ocultos do leitor de tela;
- Leitor de tela: lido como texto ("Status: pendente").

## `StockStepper`

Propriedades usadas: `value` e `onChange(delta)`. Botões de diminuir e aumentar de 48 x 48 dp ou mais, com o valor entre eles. O estoque não fica abaixo de zero (regra do `adjustStock`).

Rótulos de leitor de tela: "Diminuir estoque de <medicamento>" e "Aumentar estoque de <medicamento>", com o valor atual anunciado. O rótulo precisa incluir o nome do medicamento, porque a tela tem vários steppers.

## `SwitchRow`

Propriedades usadas: `label`, `description`, `value` e `onChange`. Rótulo e descrição em texto ao lado do interruptor, com o estado anunciado por `accessibilityState`.

> **Atenção:** as preferências de notificação hoje ficam só no aparelho e o app ainda não envia lembretes. Até os lembretes por WhatsApp existirem, a tela deve mostrar "Em breve" ou desabilitar o interruptor, para ninguém confiar em um aviso que não acontece. Quando existirem, o consentimento do WhatsApp deve ser pedido em uma tela ou opção própria, com o número informado e a política de privacidade à vista, e não apenas por um interruptor.

## `FilterChips`

Propriedades usadas: `options` (lista de `value` e `label`), `selected` e `onSelect`. Cada chip com 48 dp de altura mínima, estado selecionado indicado por texto ou ícone (`accessibilityState={{ selected }}`), e não só pela cor. Os rótulos atuais usam emoji ("✅ Tomadas"); prefira texto puro.

## Elementos que não são componentes

### Confirmação (`Alert.alert`)

Usada para registrar dose (Hoje), excluir medicamento e excluir conta. É acessível por padrão, mas tem limites:

- No registro de dose, os rótulos têm emoji ("Tomei ✅"); prefira só texto: "Tomei" e "Não tomei";
- A ação destrutiva usa o estilo `destructive`; a alternativa segura ("Cancelar") deve ser a mais fácil de achar;
- O texto explica a consequência em linguagem simples.

### Chips de horário (formulário)

Cada horário é um `Pressable` que remove o horário ao tocar, com rótulo "Remover horário 08:00". Hoje o chip tem altura estimada abaixo de 48 dp e usa fonte 14. Se o padrão se repetir em outra tela, transforme em componente.

## Divergências conhecidas

Pontos em que o código atual não segue as regras acima. Cada item deve virar uma issue com a etiqueta `accessibility`.

| Onde | Divergência | Regra afetada | Severidade |
| :--- | :--- | :--- | :--- |
| Formulário | Chips de horário com altura estimada abaixo de 48 dp | Alvo de toque | Alta |
| Hoje | Resumo mostra só emojis e números ("✅ 3 ⏰ 1 ❌ 0"), sem texto | Informação sem depender só de cor e emoji | Alta |
| Hoje | Registro de dose por `Alert` com emoji, em vez de botão de 56 dp | Alvo de toque e clareza | Média |
| Histórico | Horário com `width: 56` fixo | Layout com fonte grande | Alta |
| Histórico | Nome do medicamento com `numberOfLines={1}` | Informação cortada | Alta |
| Histórico e Medicamentos | Dosagem e data em fonte 14 com `textMuted` | Tamanho e contraste (3,65:1) | Média |
| Várias telas | Emojis como ícones (filtros, status, títulos de seção) | Ícone decorativo e leitor de tela | Média |
| Ajustes | Interruptor de lembrete ligado por padrão, sem efeito. Lembretes por WhatsApp exigirão consentimento próprio, desligado por padrão | Informação enganosa | Alta |

## Como adicionar ou alterar um componente

1. Confira se já existe um componente neste catálogo antes de criar outro;
2. Use apenas os tokens do tema; se faltar um, proponha em [UI-UX.md](./UI-UX.md) antes;
3. Atualize este documento (propriedades, estados e regras de acessibilidade);
4. Siga o checklist de [ACCESSIBILITY.md](./ACCESSIBILITY.md) e inclua prints antes e depois no Pull Request;
5. Registre no [CHANGELOG.md](./CHANGELOG.md).

> O MedControl é uma ferramenta de organização e **não substitui orientação médica**.

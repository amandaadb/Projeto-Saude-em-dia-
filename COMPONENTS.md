# Componentes - MedControl

> Catálogo dos componentes reutilizáveis da interface (botões, campos, cards de medicamentos, badges e modais de alerta), garantindo consistência visual em todo o aplicativo.

Os componentes ficam em `frontend/src/components/` e usam apenas os tokens de `frontend/src/theme/index.ts` (cores, tipografia, espaçamento e arredondamento). Veja os valores em [UI-UX.md](./UI-UX.md). Nenhum componente escreve cor ou tamanho "na mão".

## Como ler este documento

| Situação | Significado |
| :--- | :--- |
| Especificado | Comportamento definido neste documento; falta confirmar se o código segue |
| Implementado | Existe no código e segue esta especificação |
| Planejado | Depende de funcionalidade que ainda não existe |

Todos os componentes abaixo estão como **Especificado**. Quem implementa deve atualizar a coluna ao confirmar no código.

## Componentes

| Componente | Uso | Situação |
| :--- | :--- | :--- |
| Botão | Ações principais, secundárias e de perigo | Especificado |
| Campo | Entrada de dados nos formulários | Especificado |
| Card de medicamento | Exibição de cada medicamento | Especificado |
| Badge de status | Estado da dose e do estoque | Especificado |
| Modal de alerta | Avisos e confirmações | Especificado |
| Ajuste de estoque | Aumentar ou diminuir o estoque (+/-) | Especificado |
| Seletor de horários | Adicionar e remover horários do medicamento | Especificado |
| Interruptor | Preferências de notificação | Especificado |

## Regras para todos os componentes

- **Alvo de toque:** mínimo de 48 x 48 dp; botões de ação principal, como registrar dose, com 56 dp de altura;
- **Espaço entre alvos:** pelo menos 8 dp (`spacing.sm`);
- **Texto:** nunca menor que 16 em informação essencial. Sem altura fixa em containers de texto;
- **Fonte do sistema:** o texto cresce com o tamanho de fonte do aparelho;
- **Cor:** nenhuma informação depende só de cor; sempre há texto e/ou ícone;
- **Contraste:** pares de cor devem constar na tabela de [UI-UX.md](./UI-UX.md#contraste);
- **Leitor de tela:** todo elemento interativo tem `accessibilityRole` e `accessibilityLabel` que dizem a ação e o objeto, e ícones decorativos ficam ocultos (`accessible={false}`).

## Botão

| Variante | Fundo | Texto | Uso |
| :--- | :--- | :--- | :--- |
| Principal | `primaryStrong` (`blue900`) | `white` | Ação principal da tela (salvar, entrar, registrar dose) |
| Secundário | `surface` com borda `blue500` | `text` | Ações alternativas (cancelar, voltar) |
| Perigo | `danger` (`pink900`) | `white` | Ações destrutivas (excluir medicamento, excluir conta) |

Estados:

| Estado | Comportamento |
| :--- | :--- |
| Normal | Cores da variante |
| Pressionado | Escurece o fundo ou reduz a opacidade; deve ser perceptível |
| Desabilitado | Cor reduzida **e** o motivo explicado em texto próximo (a opacidade sozinha não basta) |
| Carregando | Indicador de progresso e texto mantido (ex.: "Salvando...") |

Regras:

- Rótulo com verbo claro ("Salvar medicamento"), nunca só "OK";
- Altura mínima de 48 dp (56 dp na ação principal), largura total em formulários;
- Texto: Inter SemiBold, tamanho 16 ou mais.

## Campo

| Parte | Especificação |
| :--- | :--- |
| Rótulo | Sempre visível **acima** do campo, nunca só como placeholder |
| Borda | `blue500` (3,65:1 sobre branco); a borda `border` não atende ao mínimo de 3:1 |
| Fundo | `surface` |
| Texto digitado | `text`, Inter Regular 16 |
| Ajuda | Texto curto abaixo, dizendo o formato (ex.: "Use horas e minutos, como 08:30") |
| Erro | Borda `danger`, ícone e mensagem abaixo dizendo o que houve e como resolver |

Formatos esperados pela API (veja `frontend/src/utils/format.ts`):

| Campo | Digitado | Enviado ao back-end |
| :--- | :--- | :--- |
| Horário | `08:30` (00:00 a 23:59) | `08:30:00` |
| Data de nascimento | `20/05/1995` | `1995-05-20` |
| Campo opcional vazio | (vazio) | `null`, nunca `""` |

Mensagens de erro de exemplo: "Horário inválido. Use o formato 08:30." e "Data inválida. Use dia/mês/ano, como 20/05/1995."

## Card de medicamento

Conteúdo, nesta ordem:

1. Nome do medicamento e dosagem (Subtítulo, 18);
2. Próximo horário (Corpo, 16);
3. Badge de status da dose;
4. Badge de estoque baixo, quando o estoque for menor ou igual ao limite;
5. Estoque atual em texto ("Restam 3 unidades").

Regras:

- Fundo `surface`, arredondamento `radius.md`, espaçamento interno `spacing.md`;
- O card inteiro é um alvo de toque quando abre o detalhe/edição;
- Leitor de tela: um único rótulo resumido, por exemplo "Losartana 50 mg, 08:00, pendente, estoque baixo".

## Badge de status

Cada badge mostra **ícone + texto**. A cor é reforço, nunca a única informação.

| Estado | Texto | Ícone | Fundo | Texto (cor) | Contraste |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Tomado | Tomado | Check | `green300` | `blue900` | 6,06:1 |
| Pendente | Pendente | Relógio | `blue100` | `blue900` | 6,58:1 |
| Não tomado | Não tomado | X | `pink100` | `pink900` | 6,80:1 |
| Estoque baixo | Estoque baixo | Alerta | `#FFE8C2` | `#8A4B00` | 5,69:1 |

Regras:

- Tokens vêm de `doseStatusStyle` e `lowStockStyle`, em `theme/index.ts`;
- O badge de dose e o de estoque podem aparecer juntos no mesmo card;
- Texto em Inter Medium, 14 ou mais (não menor que a legenda);
- Leitor de tela: o badge é lido como texto ("Status: pendente"), com o ícone oculto;
- Pendências: a cor de estoque baixo é provisória, e os emojis atuais devem ser trocados por ícones vetoriais.

Exemplo de uso com leitor de tela:

```tsx
<View accessible accessibilityRole="text" accessibilityLabel={`Status: ${style.label}`}>
  <Text accessible={false}>{style.icon}</Text>
  <Text>{style.label}</Text>
</View>
```

## Modal de alerta

Usado para confirmar ações destrutivas e avisar erros importantes.

| Parte | Especificação |
| :--- | :--- |
| Título | Diz a ação ("Excluir Losartana?"), em Título ou Subtítulo |
| Texto | Explica a consequência em linguagem simples ("Os horários deste medicamento também serão removidos.") |
| Botões | Dois botões, com a ação destrutiva em **Perigo** e a alternativa segura em **Secundário** |
| Ordem | Alternativa segura primeiro; a ação destrutiva nunca é o botão padrão |
| Fechar | Botão explícito; não depende de tocar fora do modal |

Regras:

- O foco do leitor de tela vai para o título ao abrir o modal;
- Em exclusões, o texto avisa se a ação não pode ser desfeita;
- Evite usar modais para mensagens que não exigem decisão.

## Ajuste de estoque

- Dois botões (`-` e `+`) de 48 x 48 dp ou mais, com o valor entre eles em Corpo, 16 ou mais;
- O estoque não fica abaixo de zero (comportamento do `adjustStock` no `MedStore`);
- Rótulos de leitor de tela: "Diminuir estoque de Losartana" e "Aumentar estoque de Losartana", com o valor atual anunciado.

## Seletor de horários

- Lista dos horários do medicamento, cada um com botão de remover (rótulo: "Remover horário 08:00");
- Botão "Adicionar horário" abre campo no formato `08:30`;
- Cada horário vira uma rotina no back-end; horários repetidos não são aceitos;
- Mesma validação do componente Campo.

## Interruptor

Usado nas preferências de notificação (lembretes de dose e alertas de estoque baixo).

- Rótulo em texto ao lado, nunca só o interruptor;
- O estado "ligado/desligado" é anunciado por texto (`accessibilityState`), e não só pela cor;
- **Atenção:** essas preferências ficam só no aparelho; não há endpoint no back-end, e o app ainda não envia notificações (planejado, ver [README.md](./README.md)).

## Como adicionar ou alterar um componente

1. Confira se já existe um componente neste catálogo antes de criar outro;
2. Use apenas os tokens do tema; se faltar um, proponha em [UI-UX.md](./UI-UX.md) antes;
3. Atualize este documento (propriedades, estados e regras de acessibilidade);
4. Siga o checklist de [ACCESSIBILITY.md](./ACCESSIBILITY.md) e inclua prints antes e depois no Pull Request;
5. Registre no [CHANGELOG.md](./CHANGELOG.md).

> O MedControl é uma ferramenta de organização e **não substitui orientação médica**.

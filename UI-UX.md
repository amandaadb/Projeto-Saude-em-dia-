# UI/UX - MedControl

> Documentação visual do aplicativo, contendo o logo, a paleta de cores oficial, a tipografia, o espaçamento, os estados visuais e o contraste das cores.

A fonte de verdade no código é `frontend/src/theme/index.ts`. Ao alterar uma cor, uma fonte ou um tamanho, atualize o código e este documento no mesmo Pull Request.

## Logo

<img width="1254" height="1254" alt="Logo" src="https://github.com/user-attachments/assets/594354a5-b0bc-4ab5-9a56-fd2a9a885d6a" />

## Protótipo

- **Telas:** [docs/prototipo.md](./docs/prototipo.md).

## Paleta oficial

| Token | Nome | Hexadecimal |
| :--- | :--- | :--- |
| `blue100` | Azul claro | `#BDDDFC` |
| `blue300` | Azul médio | `#88BDF2` |
| `blue500` | Azul principal | `#6A89A7` |
| `blue900` | Azul escuro | `#384959` |
| `green100` | Verde claro | `#E3F0A3` |
| `green300` | Verde suave | `#BADBA2` |
| `green500` | Verde principal | `#80EF80` |
| `green700` | Verde vibrante | `#42D674` |
| `pink100` | Rosa claro | `#FAD2E1` |
| `pink300` | Rosa médio | `#F8B4CD` |
| `pink500` | Rosa principal | `#E06D95` |
| `pink900` | Rosa escuro | `#7D2845` |

Os tokens `blue300`, `green100`, `green500`, `green700`, `pink300` e `pink500` fazem parte da paleta, mas ainda não têm papel definido nas telas. Nunca use texto branco sobre `blue100`, `blue300`, `green500`, `green700` ou `pink500`: o contraste fica abaixo do mínimo.

## Cores por função

Os componentes usam apenas estes papéis, nunca um hexadecimal direto.

| Papel | Valor | Uso | Observação |
| :--- | :--- | :--- | :--- |
| `primary` | `blue500` | Ícones e elementos de destaque | Não usar como cor de texto normal |
| `primaryStrong` | `blue900` | Fundo de botão principal | Texto branco sobre ele: 9,27:1 |
| `primarySoft` | `blue100` | Fundos suaves e selecionados | Só com texto escuro |
| `background` | `#F7FAFD` | Fundo das telas | Neutro derivado, fora do guia |
| `surface` | `#FFFFFF` | Cards e campos | |
| `text` | `blue900` | Texto principal | 9,27:1 sobre branco |
| `textMuted` | `blue500` | Texto secundário | Reprova AA, ver seção Contraste |
| `border` | `#E1EBF5` | Divisórias e bordas de card | Neutro derivado, fora do guia |
| `danger` | `pink900` | Ações destrutivas e erros | Texto branco sobre ele: 9,29:1 |
| `white` | `#FFFFFF` | Texto sobre fundos escuros | |

## Tipografia

Fonte principal: **Inter**. Fonte secundária: **Nunito Sans**. No Android, a fonte customizada não responde a `fontWeight`, então cada peso é uma família diferente (`Inter_400Regular`, `Inter_500Medium`, `Inter_600SemiBold`, `Inter_700Bold` e `NunitoSans_400Regular`). Nunca use `fontWeight` nos estilos.

| Estilo | Família | Tamanho | Uso |
| :--- | :--- | :--- | :--- |
| Título | Inter Bold | 24 | Título de tela |
| Subtítulo | Inter SemiBold | 18 | Nome do medicamento, seções |
| Corpo | Inter Regular | 16 | Texto corrido, campos, botões |
| Legenda | Inter Medium | 14 | Informação complementar |
| Secundária | Nunito Sans Regular | A definir | Textos de apoio |

Regras de uso:

- O tamanho 14 (legenda) nunca é usado para horários, doses, estoque, avisos ou erros. Esses textos usam 16 ou mais;
- Nenhum texto desativa o aumento de fonte do sistema. Se limitar, use `maxFontSizeMultiplier` de pelo menos 2;
- Containers de texto não têm altura fixa, para crescerem com a fonte aumentada.

## Espaçamento e arredondamento

| Token | Valor |
| :--- | :--- |
| `spacing.xs` | 4 |
| `spacing.sm` | 8 |
| `spacing.md` | 16 |
| `spacing.lg` | 24 |
| `spacing.xl` | 32 |
| `radius.sm` | 8 |
| `radius.md` | 14 |
| `radius.pill` | 999 |

## Estados visuais

Todo estado é comunicado por **ícone + texto + cor**. A cor sozinha nunca basta.

### Estado da dose

O back-end não guarda "pendente". O status é calculado no app: sem registro no histórico hoje é pendente; com registro, depende de `fl_taken`.

| Estado | Texto | Ícone | Fundo | Texto (cor) | Contraste |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Tomado | Tomado | Check | `green300` `#BADBA2` | `blue900` | 6,06:1 |
| Pendente | Pendente | Relógio | `blue100` `#BDDDFC` | `blue900` | 6,58:1 |
| Não tomado | Não tomado | X | `pink100` `#FAD2E1` | `pink900` | 6,80:1 |

### Estado do estoque

O estado de estoque convive com o da dose no mesmo medicamento.

| Estado | Texto | Ícone | Fundo | Texto (cor) | Contraste |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Estoque baixo | Estoque baixo | Alerta | `#FFE8C2` | `#8A4B00` | 5,69:1 |

Pendências deste estado:

- O guia oficial não tem cor de alerta. O laranja acima é **provisório** e precisa de aprovação do UX/UI;
- O limite de estoque baixo é **5 unidades**, fixo no app. O banco não tem esse campo, e a sugestão ao back-end é criar `stock_alert` em `medicines`;
- Hoje os ícones são emojis. Eles variam por aparelho e podem ser lidos de forma estranha pelos leitores de tela. A recomendação é trocar por ícones vetoriais (`@expo/vector-icons`), marcados como decorativos.

## Contraste

**Método:** razão de contraste calculada pela fórmula de luminância relativa do WCAG 2.x, em 25/10/2026, a partir dos hexadecimais de `theme/index.ts`. **Ainda não foi conferida em ferramenta externa** nem em aparelho real; antes de declarar conformidade, valide os pares com o WebAIM Contrast Checker.

**Metas:** texto normal 4,5:1 (AA) e, para textos principais, 7:1 (AAA). Texto grande (a partir de 18 pt, ou 14 pt em negrito) e componentes de interface (bordas de campo, ícones): 3:1.

| Uso | Texto | Fundo | Razão | AA | AAA |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Texto principal na tela | `#384959` | `#F7FAFD` | 8,85:1 | Sim | Sim |
| Texto principal no card | `#384959` | `#FFFFFF` | 9,27:1 | Sim | Sim |
| Botão principal | `#FFFFFF` | `#384959` | 9,27:1 | Sim | Sim |
| Botão de perigo | `#FFFFFF` | `#7D2845` | 9,29:1 | Sim | Sim |
| Badge Tomado | `#384959` | `#BADBA2` | 6,06:1 | Sim | Não |
| Badge Pendente | `#384959` | `#BDDDFC` | 6,58:1 | Sim | Não |
| Badge Não tomado | `#7D2845` | `#FAD2E1` | 6,80:1 | Sim | Não |
| Badge Estoque baixo | `#8A4B00` | `#FFE8C2` | 5,69:1 | Sim | Não |
| Texto escuro sobre azul médio | `#384959` | `#88BDF2` | 4,68:1 | Sim | Não |
| Texto secundário atual | `#6A89A7` | `#FFFFFF` | 3,65:1 | **Não** | Não |
| Texto secundário atual | `#6A89A7` | `#F7FAFD` | 3,49:1 | **Não** | Não |
| Texto secundário atual | `#6A89A7` | `#BDDDFC` | 2,59:1 | **Não** | Não |
| Texto secundário proposto | `#4F6A85` | `#F7FAFD` | 5,37:1 | Sim | Não |
| Texto secundário proposto | `#4F6A85` | `#FFFFFF` | 5,63:1 | Sim | Não |
| Texto branco sobre azul claro | `#FFFFFF` | `#BDDDFC` | 1,41:1 | **Não** | Não |

| Componente | Cor | Fundo | Razão | Mínimo (3:1) |
| :--- | :--- | :--- | :--- | :--- |
| Borda atual | `#E1EBF5` | `#FFFFFF` | 1,21:1 | **Não** |
| Borda de campo proposta | `#6A89A7` | `#FFFFFF` | 3,65:1 | Sim |

Decisões pendentes:

- **Texto secundário:** a cor `blue500` não pode ser usada em texto normal. Opções: usar `blue900` ou adotar `#4F6A85` (cor nova, fora do guia oficial);
- **Borda de campo:** a borda `#E1EBF5` serve para separar cards, mas campos de formulário precisam de borda com pelo menos 3:1 (por exemplo, `blue500`);
- Não há modo escuro nem alto contraste. O app está fixado no tema claro (`userInterfaceStyle: light`). O alto contraste está no roadmap e na tela prevista de Acessibilidade.

## Identidade do app

Configuração atual em `frontend/app.json`:

| Item | Situação |
| :--- | :--- |
| Ícone do app e ícone adaptativo (Android) | Imagens padrão do template Expo; substituir pelo logo do MedControl |
| Fundo do ícone adaptativo | `#E6F4FE`, cor padrão do Expo, fora da paleta |
| Splash | Fundo `#BDDDFC` (`blue100`, dentro da paleta); imagem ainda padrão do template |
| Favicon (web) | Imagem padrão do template |

## Pendências de design

- [ ] Substituir ícone, ícone adaptativo, splash e favicon pelo logo do MedControl;
- [ ] Decidir a cor do texto secundário e a borda de campo (seção Contraste);
- [ ] Aprovar a cor de alerta de estoque baixo e definir o tamanho da fonte secundária (Nunito Sans);
- [ ] Trocar os emojis de status por ícones vetoriais;
- [ ] Desenhar a paleta de alto contraste e as três escalas de fonte (normal, grande e muito grande);
- [ ] Conferir os contrastes em ferramenta externa e registrar o resultado em [ACCESSIBILITY.md](./ACCESSIBILITY.md).

## Documentos relacionados

- [COMPONENTS.md](./COMPONENTS.md): catálogo de componentes;
- [ACCESSIBILITY.md](./ACCESSIBILITY.md): compromissos e limitações de acessibilidade;
- [docs/prototipo.md](./docs/prototipo.md): telas do protótipo.

> O MedControl é uma ferramenta de organização e **não substitui orientação médica**.

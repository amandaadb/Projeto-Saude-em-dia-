# Acessibilidade - MedControl

> Compromissos de acessibilidade do projeto, expectativas para quem contribui, como relatar barreiras encontradas no aplicativo e o que já sabemos que ainda não funciona bem.

## Por que isso importa?

O MedControl ajuda pessoas a organizar medicamentos e horários, e muitas delas são idosas, têm baixa visão, dificuldade de leitura, tremores nas mãos ou pouca familiaridade com tecnologia. Se o aplicativo for difícil de usar, o risco é real: uma dose esquecida ou uma informação mal compreendida.

Por isso, queremos que o aplicativo seja utilizável por qualquer pessoa, com ou sem deficiência, e que qualquer pessoa possa contribuir com o projeto. Este documento explica o que priorizamos, o que esperamos de quem contribui, como relatar uma barreira e o que já sabemos que ainda não funciona bem.

Se você chegou aqui depois de encontrar uma dificuldade no aplicativo, sentimos muito. Seu relato nos ajuda a melhorar.

## Prioridades

- **Leitura confortável:** textos grandes e legíveis, com bom contraste entre texto e fundo;
- **Telas simples:** poucas ações por tela, textos curtos e navegação previsível, pensando principalmente em idosos;
- **Toque fácil:** botões grandes (mínimo de 48 dp, e 56 dp nas ações principais) e com espaço entre si;
- **Informação sem depender só de cor:** o estado da dose (tomada, pendente, não tomada) e o estoque baixo são mostrados com texto, e não apenas com cor ou emoji;
- **Alertas claros:** avisos escritos em linguagem simples;
- **Português claro:** o aplicativo é em português, e buscamos evitar termos técnicos.

Adotamos as diretrizes internacionais de acessibilidade para conteúdo web (WCAG, nível AA) como **meta de referência**. Isso é um objetivo, **não uma declaração de conformidade**: o MedControl ainda não passou por uma avaliação formal de acessibilidade. Se isso mudar, registraremos aqui o escopo avaliado, a data, o método e quem avaliou.

## Expectativas para quem contribui

Alterações que afetam a interface devem manter ou melhorar a acessibilidade. Antes de abrir um Pull Request com mudanças visuais, confira:

- [ ] O texto continua legível, com bom contraste e sem tamanho ou largura fixos que impeçam o aumento da fonte;
- [ ] Informação essencial (dose, horário, estoque, erro) usa fonte de 16 ou mais;
- [ ] Botões e áreas de toque têm pelo menos 48 x 48 dp e espaço de 8 dp entre si;
- [ ] Nenhuma informação importante depende apenas de cor ou de emoji;
- [ ] Todo elemento interativo tem `accessibilityLabel` e `accessibilityRole`, e ícones decorativos ficam ocultos do leitor de tela;
- [ ] Mensagens de erro dizem o que aconteceu e como resolver;
- [ ] Os componentes seguem o catálogo em [COMPONENTS.md](./COMPONENTS.md) e a identidade visual em [UI-UX.md](./UI-UX.md);
- [ ] A tela foi testada em tamanhos de tela diferentes e com a fonte do sistema aumentada.

**Evidências:** em mudanças visuais, inclua no Pull Request prints antes e depois e uma breve nota sobre como a alteração foi testada (por exemplo, com fonte aumentada ou em tela pequena). Se você usou algum recurso de acessibilidade do celular para testar, como leitor de tela ou ampliação, conte qual.

## Ferramentas e verificações

| Verificação | Situação |
| :--- | :--- |
| Contraste das cores | Calculado pela fórmula do WCAG em 25/10/2026, **sem conferência em ferramenta externa**. Resultado em [UI-UX.md](./UI-UX.md#contraste) |
| `npm run lint` | Disponível, mas não é específico de acessibilidade |
| Testes automatizados de acessibilidade | Ainda não usamos |
| Teste com leitor de tela (TalkBack e VoiceOver) | Ainda não realizado |
| Teste com pessoas idosas ou com deficiência | Ainda não realizado |

## Relatando problemas de acessibilidade

Se você encontrou uma barreira ou precisa de ajuda para usar o MedControl, escreva para:

**amanda.db@uni9.edu.br**

Ou abra uma issue com o modelo "Relatar problema de acessibilidade". Para nos ajudar a entender o problema, conte, se puder:

- O que você estava tentando fazer (por exemplo, cadastrar um medicamento ou registrar uma dose);
- Em qual tela aconteceu;
- O que aconteceu e o que você esperava que acontecesse;
- O modelo do aparelho e o sistema operacional;
- Se usa algum recurso de apoio (leitor de tela, ampliação de tela, comando por voz, entre outros).

Prints ou gravações são **opcionais**. Você **não precisa** informar nenhuma deficiência ou condição de saúde para relatar um problema. Se não conseguir escrever, peça a alguém de confiança para enviar por você.

### Severidade

Ao analisar o relato, a equipe define a severidade conforme o quanto a barreira impede a pessoa de concluir a tarefa. Quem relata não precisa classificar.

| Nível | Descrição | Exemplo |
| :--- | :--- | :--- |
| **Crítica** | Impede uma tarefa essencial e sem alternativa | Não é possível registrar uma dose como tomada |
| **Alta** | Dificulta muito a tarefa, mas há um jeito difícil de concluir | Botão ou chip muito pequeno e difícil de tocar |
| **Média** | Causa incômodo ou exige esforço extra | Texto com contraste baixo em uma tela secundária |
| **Baixa** | Melhoria que torna o uso mais agradável | Mensagem que poderia ser escrita de forma mais simples |

### Como respondemos?

- **Confirmação de recebimento:** em até 2 dias úteis;
- **Atualização sobre o andamento:** em até 7 dias úteis;
- **Alternativas:** quando houver uma forma de contornar o problema enquanto a correção não sai, enviaremos para você;
- **Verificação:** depois de corrigido, avisaremos e, se você quiser, pediremos que confirme se o problema foi resolvido;
- **Se não for possível corrigir:** explicaremos o motivo.

Por ser um projeto acadêmico mantido por uma equipe pequena, não prometemos prazo de correção, mas todo relato será lido e respondido.

## Responsabilidade e manutenção

A acessibilidade é responsabilidade de toda a equipe, com os seguintes papéis:

- **Front-end (Daniela e Luana):** implementam a acessibilidade visual e de interação nas telas;
- **UX/UI (Gabriel):** garante que cores, fontes e componentes sejam acessíveis desde o protótipo;
- **Testes e Documentação (Guilherme):** inclui verificações de acessibilidade nos testes e registra os resultados;
- **Contato com usuários (Amanda):** recebe os relatos e repassa para a equipe.

Este documento deve ser revisado a cada nova versão do aplicativo e sempre que uma limitação for corrigida ou descoberta. Se alguém sair do projeto, suas responsabilidades devem ser repassadas a outro integrante e o documento atualizado.

## Ambientes suportados

O MedControl é um aplicativo mobile, executado hoje pelo Expo Go durante o desenvolvimento. Até o momento, **não houve uma avaliação formal em uma lista definida de aparelhos, sistemas operacionais ou tecnologias assistivas**, e por isso não afirmamos suporte a nenhuma combinação específica.

Configurações atuais do app que afetam a acessibilidade:

- **Orientação:** fixa em retrato;
- **Tema:** fixo no claro, mesmo que o aparelho esteja em modo escuro.

Quando os testes forem feitos, esta seção listará os sistemas operacionais e versões testados (Android e iOS), os tipos de aparelho, os recursos de apoio testados e o suporte parcial, quando houver.

## Limitações conhecidas

Estas são barreiras que já sabemos que existem, ou que ainda não foram tratadas:

- **Os lembretes de dose ainda não existem.** O app não envia avisos. O interruptor "Lembrete de dose" em Ajustes ainda não tem efeito, e a pessoa precisa conferir a aba "Hoje" por conta própria. O canal inicial planejado é o **WhatsApp**, que muitas pessoas idosas já usam e que acompanha o tamanho de fonte do aparelho. Som, vibração e exibição na tela bloqueada dependem das configurações do WhatsApp da própria pessoa, e **o MedControl não controla isso**. Depois virão as notificações do celular e a integração com agendas, que ainda não têm acessibilidade avaliada;
- **O aplicativo não tem ajuste de tamanho de fonte próprio.** O texto acompanha o tamanho de fonte do aparelho, mas algumas telas têm largura fixa ou `numberOfLines` (por exemplo, o Histórico) e podem cortar ou quebrar o layout com a fonte muito grande;
- **Alguns alvos de toque são pequenos**, como os chips de horário no formulário de medicamento;
- **Parte das informações usa emojis como ícones** (resumo de "Hoje", status e filtros), e o resumo não tem texto equivalente;
- **O texto secundário e a borda dos campos não atingem o contraste mínimo.** O texto secundário (`#6A89A7`) tem 3,65:1 sobre branco, e a borda (`#E1EBF5`) tem 1,21:1. Detalhes em [UI-UX.md](./UI-UX.md#contraste);
- **Não há modo de alto contraste nem modo escuro**;
- **O suporte a leitores de tela ainda não foi avaliado.** Não sabemos se todos os botões e campos são anunciados corretamente;
- **A navegação simplificada ainda não existe.** O fluxo atual tem várias telas e pode ser cansativo para algumas pessoas;
- **O registro de dose usa uma janela de diálogo com três botões**, e não um botão grande dedicado.

A lista completa de divergências do código está em [COMPONENTS.md](./COMPONENTS.md#divergências-conhecidas). Ajuste de fonte, alto contraste, leitor de tela e navegação simplificada estão no roadmap do [README.md](./README.md) como melhorias futuras e **não estão implementados** na versão atual.

## Testes realizados

Ainda não fizemos testes com pessoas idosas, com pessoas com deficiência nem com leitores de tela. Por isso, não afirmamos que o aplicativo não tem barreiras: apenas que ainda não as avaliamos por completo.

Quando houver testes, registre aqui cada um:

| Data | Tipo de teste | Participantes | Tarefas | Resultado | Correções feitas |
| :--- | :--- | :--- | :--- | :--- | :--- |
| (a preencher) | | | | | |

Use sempre **dados fictícios** e peça consentimento antes de gravar ou fotografar. Veja [docs/privacidade.md](./docs/privacidade.md#cuidados-para-quem-contribui).

## Sugestões e melhorias

Quer sugerir uma melhoria neste documento ou nas nossas práticas de acessibilidade? Escreva para **amanda.db@uni9.edu.br** ou, se for da equipe, fale pelo grupo do WhatsApp do projeto.

Se você está enfrentando uma barreira agora, use o processo da seção [Relatando problemas de acessibilidade](#relatando-problemas-de-acessibilidade).

> O MedControl é uma ferramenta de organização e **não substitui orientação médica**.

# Acessibilidade - MedControl

> Compromissos de acessibilidade do projeto, expectativas para quem contribui e como relatar barreiras encontradas no aplicativo.

## Por que isso importa?

O MedControl ajuda pessoas a organizar medicamentos e horários, e muitas delas são idosas, têm baixa visão, dificuldade de leitura, tremores nas mãos ou pouca familiaridade com tecnologia. Se o aplicativo for difícil de usar, o risco é real: uma dose esquecida ou uma informação mal compreendida.

Por isso, queremos que o aplicativo seja utilizável por qualquer pessoa, com ou sem deficiência, e que qualquer pessoa possa contribuir com o projeto. Este documento explica o que priorizamos, o que esperamos de quem contribui, como relatar uma barreira e o que já sabemos que ainda não funciona bem.

Se você chegou aqui depois de encontrar uma dificuldade no aplicativo, sentimos muito. Seu relato nos ajuda a melhorar.

## Prioridades

Trabalhamos para que o aplicativo seja fácil de ver, entender e usar. Nossas prioridades são:

- **Leitura confortável:** textos grandes e legíveis, com bom contraste entre texto e fundo;
- **Telas simples:** poucas ações por tela, textos curtos e navegação previsível, pensando principalmente em idosos;
- **Toque fácil:** botões grandes e com espaço entre si, para quem tem dificuldade de precisão;
- **Informação sem depender só de cor:** alertas e status de dose (tomada, adiada, perdida) devem ser entendidos também por texto ou ícone, e não apenas pela cor;
- **Alertas claros:** lembretes e avisos de estoque baixo escritos em linguagem simples;
- **Português claro:** o aplicativo é em português, e buscamos evitar termos técnicos.

Adotamos as diretrizes internacionais de acessibilidade para conteúdo web (WCAG, nível AA) como **meta de referência**. Isso é um objetivo, **não uma declaração de conformidade**: o MedControl ainda não passou por uma avaliação formal de acessibilidade. Se isso mudar, registraremos aqui o escopo avaliado, a data, o método e quem avaliou.

## Expectativas para quem contribui

Alterações que afetam a interface devem manter ou melhorar a acessibilidade. Antes de abrir um Pull Request com mudanças visuais, confira:

- [ ] O texto continua legível, com bom contraste e sem tamanho fixo que impeça o aumento da fonte;
- [ ] Botões e áreas de toque são grandes o suficiente e não ficam muito próximos;
- [ ] Nenhuma informação importante depende apenas de cor;
- [ ] Mensagens de erro dizem o que aconteceu e como resolver;
- [ ] Os componentes seguem o catálogo em [COMPONENTS.md](./COMPONENTS.md) e a identidade visual em [UI-UX.md](./UI-UX.md);
- [ ] A tela foi testada em tamanhos de tela diferentes.

**Evidências:** em mudanças visuais, inclua no Pull Request prints antes e depois e uma breve nota sobre como a alteração foi testada (por exemplo, com fonte aumentada ou em tela pequena). Se você usou algum recurso de acessibilidade do celular para testar, como leitor de tela ou ampliação, conte qual.

Ainda não usamos ferramentas automatizadas de acessibilidade. Quando passarmos a usar, elas serão listadas aqui.

## Relatando problemas de acessibilidade

Se você encontrou uma barreira ou precisa de ajuda para usar o MedControl, escreva para:

**amanda.db@uni9.edu.br**

Para nos ajudar a entender o problema, conte, se puder:

- O que você estava tentando fazer (por exemplo, cadastrar um medicamento ou registrar uma dose);
- Em qual tela aconteceu;
- O que aconteceu e o que você esperava que acontecesse;
- O modelo do aparelho e o sistema operacional;
- Se usa algum recurso de apoio (leitor de tela, ampliação de tela, comando por voz, entre outros).

Prints ou gravações são **opcionais**. Você **não precisa** informar nenhuma deficiência ou condição de saúde para relatar um problema.

Se não conseguir escrever por e-mail, peça a alguém de confiança para enviar por você.

### Severidade

Ao analisar o relato, a equipe define a severidade conforme o quanto a barreira impede a pessoa de concluir a tarefa. Quem relata não precisa classificar.

| Nível | Descrição | Exemplo |
| :--- | :--- | :--- |
| **Crítica** | Impede uma tarefa essencial e sem alternativa | Não é possível registrar uma dose como tomada |
| **Alta** | Dificulta muito a tarefa, mas há um jeito difícil de concluir | Botão de confirmação muito pequeno e difícil de tocar |
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
- **Testes e Documentação (Guilherme):** inclui verificações de acessibilidade nos testes e mantém este documento atualizado;
- **Contato com usuários (Amanda):** recebe os relatos e repassa para a equipe.

Este documento deve ser revisado a cada nova versão do aplicativo e sempre que uma limitação for corrigida ou descoberta. Se alguém sair do projeto, suas responsabilidades devem ser repassadas a outro integrante e o documento atualizado.

## Ambientes suportados

O MedControl é um aplicativo mobile. Até o momento, **não houve uma avaliação formal em uma lista definida de aparelhos, sistemas operacionais ou tecnologias assistivas**, e por isso não afirmamos suporte a nenhuma combinação específica.

Quando os testes forem feitos, esta seção listará:

- Sistemas operacionais e versões testados (Android e iOS);
- Tipos de aparelho (celulares e tablets);
- Recursos de apoio testados, como leitor de tela, ampliação de tela e aumento do tamanho da fonte do sistema;
- Suporte parcial, quando houver.

## Limitações conhecidas

Estas são barreiras que já sabemos que existem, ou que ainda não foram tratadas:

- **O aplicativo não tem ajuste de tamanho de fonte próprio.** Alternativa: aumentar o tamanho da fonte nas configurações do aparelho, embora o resultado ainda não tenha sido testado em todas as telas;
- **Não há modo de alto contraste.** O contraste das cores foi pensado na criação da paleta, mas não foi medido formalmente;
- **O suporte a leitores de tela ainda não foi avaliado.** Não sabemos se todos os botões e campos são anunciados corretamente;
- **A navegação simplificada ainda não existe.** O fluxo atual tem várias telas e pode ser cansativo para algumas pessoas;
- **Os avisos de dose dependem de notificações visuais e sonoras.** Não há alternativa, como vibração configurável ou outras formas de lembrete.

Ajuste de fonte, alto contraste, leitor de tela e navegação simplificada estão no roadmap do [README.md](./README.md) como melhorias futuras e **não estão implementados** na versão atual.

Também ainda não fizemos testes com pessoas idosas ou com deficiência. Por isso, não afirmamos que o aplicativo não tem barreiras: apenas que ainda não as avaliamos por completo.

## Sugestões e melhorias

Quer sugerir uma melhoria neste documento ou nas nossas práticas de acessibilidade? Escreva para **amanda.db@uni9.edu.br** ou, se for da equipe, fale pelo grupo do WhatsApp do projeto.

Se você está enfrentando uma barreira agora, use o processo da seção [Relatando Problemas de Acessibilidade](#relatando-problemas-de-acessibilidade).

> O MedControl é uma ferramenta de organização e **não substitui orientação médica**.

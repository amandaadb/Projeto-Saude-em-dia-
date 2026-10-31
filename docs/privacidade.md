# Privacidade - MedControl

> Como o MedControl trata os dados pessoais e de saúde das pessoas que usam o aplicativo, com base na Lei Geral de Proteção de Dados (LGPD, Lei nº 13.709/2018).

## Por que isso importa?

O MedControl lida com informações sobre medicamentos, tratamentos, alergias e condições de saúde, que são **dados pessoais sensíveis** segundo a LGPD (dados referentes à saúde). Por isso, tratamos a privacidade como parte essencial do projeto, e não como um detalhe.

Este documento explica quais dados coletamos, para que usamos, onde ficam guardados, com quem podem ser compartilhados, quais são os seus direitos e como falar conosco.

> O MedControl é um projeto acadêmico em desenvolvimento. Este documento descreve o funcionamento previsto e as intenções da equipe, e **não é um parecer jurídico**. Na versão atual, o aplicativo ainda usa dados de teste e **não envia dados para a API**. Os lembretes por WhatsApp, as notificações do celular e a integração com agendas **ainda não existem**; as regras sobre eles valem para quando forem ativados.

## Quais dados coletamos?

| Categoria | Dados | Para que serve | Obrigatório? |
| :--- | :--- | :--- | :--- |
| **Conta** | Nome, e-mail, telefone, data de nascimento e senha | Criar a conta, fazer login e identificar o usuário | Sim |
| **Saúde (perfil)** | Tipo sanguíneo, alergias e condições crônicas | Manter as informações de saúde da pessoa à mão | Não |
| **Contato de emergência** | Nome e telefone | Ter um contato de confiança registrado | Não |
| **Medicamentos** | Nome, dosagem, quantidade por dose, tipo e instruções de uso, estoque e descrição | Organizar o tratamento e acompanhar o estoque | Nome, dosagem e quantidade |
| **Horários** | Horário e dias da semana de cada medicamento | Montar a lista de doses do dia | Sim, para aparecer em "Hoje" |
| **Histórico de doses** | Data e hora e se a dose foi tomada ou não | Mostrar o histórico e acompanhar a rotina | Sim, ao registrar uma dose |
| **Preferências de lembrete** *(planejado)* | Se a pessoa quer receber lembretes, por qual canal (WhatsApp, notificação do celular ou agenda), o número de WhatsApp e a data do consentimento | Enviar os avisos de dose e de estoque que a pessoa pediu | Não. Só é coletado se a pessoa ativar os lembretes |
| **Dados técnicos** | Token de login (JWT), com validade de 7 dias | Manter o usuário logado e garantir acesso apenas aos próprios dados | Sim |

**A senha nunca é guardada em texto puro.** A própria API do MedControl a transforma em *hash* (com bcrypt) antes de gravar no banco.

### Lembretes por WhatsApp (planejado)

Os lembretes de dose serão enviados por **mensagem de WhatsApp**, a partir do servidor do MedControl. Isso muda o que acontece com os seus dados em relação ao restante do app:

- O seu **número de WhatsApp** e as suas **preferências de lembrete** passam a ficar guardados no servidor, e não só no aparelho;
- O envio só ocorre se você **ativar os lembretes e consentir de forma separada** do cadastro da conta, com uma opção própria para isso;
- As mensagens usam **texto genérico**, por exemplo "Está na hora do seu medicamento", **sem citar o nome do remédio** nem a condição de saúde. Isso reduz o que aparece na tela bloqueada e no histórico de conversas do celular. **[CONFIRMAR: decisão final da equipe sobre o conteúdo da mensagem.]**
- Você pode **desativar os lembretes a qualquer momento** pelo aplicativo, e o envio é interrompido. **[CONFIRMAR: se também será possível parar respondendo à própria mensagem.]**

> Cuidado: uma mensagem de WhatsApp pode ser vista por quem tiver acesso ao seu celular ou ao aparelho em que o WhatsApp Web estiver aberto. Por isso a mensagem não traz dados de saúde detalhados.

### Notificações do celular e agendas (planejado)

- **Notificações do celular:** serão geradas pelo próprio aparelho, e as preferências relacionadas ficam no aparelho;
- **Google Agenda e calendário do celular:** a integração, quando existir, só será ativada com a sua autorização. **[CONFIRMAR: quais permissões serão pedidas, se o app apenas cria eventos ou também lê a agenda, e se o título do evento mostrará o nome do medicamento.]** Você poderá revogar o acesso a qualquer momento, no app e na sua conta Google.

### O que não coletamos

- Não coletamos localização, contatos do aparelho, fotos ou documentos;
- Não coletamos dados de pagamento;
- Não lemos as suas conversas de WhatsApp: o MedControl apenas **envia** lembretes **[CONFIRMAR: se o app for receber respostas, como "PARAR", atualize esta frase]**;
- Não usamos os seus dados para publicidade nem para criar perfis comerciais.

**[CONFIRMAR: se o app, no futuro ou já agora, usar câmera (código de barras/OCR), localização ou envio de push com identificador do aparelho, atualize esta seção.]**

## Por que tratamos esses dados?

Usamos os dados **somente** para fazer o aplicativo funcionar:

- Criar e manter a sua conta;
- Cadastrar e organizar os seus medicamentos e horários;
- Registrar e exibir o seu histórico de doses;
- Mostrar o selo de estoque baixo;
- Guardar as informações de saúde e o contato de emergência que você escolher informar;
- Enviar os lembretes que você ativar (planejado).

Os dados de saúde são tratados com base no **consentimento** da pessoa usuária, que ocorre ao criar a conta e ao preencher as informações. O envio de lembretes por WhatsApp exige um **consentimento próprio**, dado por você ao ativar essa opção, e que pode ser retirado quando quiser. Os campos de saúde, de contato de emergência e de lembretes são **opcionais**: informe apenas o que se sentir à vontade para informar. **[CONFIRMAR: o app exibe um aceite deste documento no cadastro? Se não, inclua um checkbox "Li e concordo com a Política de Privacidade".]**

## Onde os dados ficam?

Os dados são armazenados no **Supabase** (banco de dados e infraestrutura), acessado exclusivamente pela API do MedControl (FastAPI). O Supabase atua como fornecedor de infraestrutura e pode armazenar dados em servidores fora do Brasil. **[CONFIRMAR: região do projeto Supabase, no painel do projeto.]**

## Como protegemos os dados?

- **Autenticação por JWT:** as rotas da API exigem login;
- **Acesso restrito:** cada usuário acessa somente os próprios dados;
- **Senha com hash:** nunca em texto puro;
- **Segredos fora do repositório:** chaves, senhas, o segredo do JWT e os tokens dos provedores de WhatsApp e Google ficam em variáveis de ambiente (`.env`), que nunca são versionadas (veja [IGNORE.md](../IGNORE.md));
- **Mensagens sem dados de saúde detalhados:** o texto do lembrete é genérico (planejado);
- **Monitoramento do repositório:** o GitHub está configurado com alertas de dependências vulneráveis, detecção de segredos e relato privado de vulnerabilidades (veja [SECURITY.md](../SECURITY.md)).

Nenhum sistema é totalmente seguro. Por ser um projeto acadêmico mantido por uma equipe pequena, **não garantimos proteção absoluta** e recomendamos não cadastrar informações além das necessárias.

## Com quem compartilhamos?

**Não vendemos** os seus dados nem os compartilhamos com terceiros para fins comerciais.

Os dados são acessados apenas pelo próprio usuário e pelos serviços técnicos necessários ao funcionamento do app:

| Serviço | O que recebe | Quando |
| :--- | :--- | :--- |
| **Supabase** | Todos os dados do app, para armazenamento | Desde a integração do app com a API |
| **Provedor de WhatsApp** **[CONFIRMAR: qual será (por exemplo, WhatsApp Business Platform da Meta ou um intermediário)]** | O seu número de telefone e o texto do lembrete | Somente se você ativar os lembretes por WhatsApp (planejado) |
| **Google** (Google Agenda) | Os eventos criados na sua agenda | Somente se você autorizar a integração (planejado) |

Esses serviços têm as próprias políticas de privacidade e podem tratar dados em servidores fora do Brasil. Ao usar o WhatsApp, a **Meta** passa a tratar o conteúdo e os metadados da mensagem conforme os termos dela.

Se um dia o **Modo Cuidador** for implementado (veja o roadmap no [README.md](../README.md)), o compartilhamento com familiares e cuidadores só ocorrerá **mediante autorização expressa do usuário**, que poderá revogá-la a qualquer momento.

## Por quanto tempo guardamos?

Os dados ficam armazenados enquanto a conta existir.

**Como a exclusão funciona hoje:** ao excluir a conta, ela é **desativada** (exclusão lógica). A conta e os dados associados deixam de ser acessíveis pelo aplicativo, mas **permanecem no banco de dados**, marcados como inativos, até serem removidos manualmente. Para pedir a remoção definitiva, escreva para o e-mail de contato. **[CONFIRMAR: prazo e procedimento da remoção definitiva, e se o e-mail de uma conta desativada pode ser reutilizado.]**

Ao **desativar os lembretes** ou **excluir a conta**, o envio de mensagens e a criação de eventos na agenda devem ser interrompidos. **[CONFIRMAR: quando a integração existir, o que acontece com os eventos que já foram criados na agenda.]**

## Seus direitos

De acordo com a LGPD (art. 18), você pode, a qualquer momento:

| Direito | Como exercer |
| :--- | :--- |
| **Confirmar e acessar** os dados que temos sobre você | Pelo aplicativo (Ajustes, Medicamentos e Histórico) ou por e-mail |
| **Corrigir** dados incompletos ou incorretos | Editando o perfil, a conta e os medicamentos no aplicativo |
| **Excluir** os seus dados | Excluindo a conta no aplicativo (desativação) e pedindo a remoção definitiva por e-mail |
| **Revogar o consentimento** (inclusive o dos lembretes por WhatsApp) | Desativando os lembretes, excluindo a conta ou solicitando por e-mail |
| **Obter informações** sobre o tratamento e o compartilhamento | Por e-mail |
| **Portabilidade** dos dados | Ainda não disponível. A exportação do histórico em PDF está prevista no roadmap |

## Crianças e adolescentes

O MedControl não foi pensado para menores de idade usarem sozinhos. Se o app for usado por ou para uma criança ou adolescente, o cadastro deve ser feito por um responsável legal. O número de WhatsApp informado deve pertencer à pessoa que consentiu com os lembretes.

## Incidentes de segurança

Se houver um incidente que possa afetar os seus dados, a equipe irá investigar, corrigir a falha, trocar as chaves afetadas (Supabase, JWT e, quando existirem, as do WhatsApp e do Google) e comunicar as pessoas impactadas. Para relatar uma vulnerabilidade, use o canal descrito em [SECURITY.md](../SECURITY.md) e **não abra issue pública**.

## Cuidados para quem contribui

- Nunca use dados reais de pessoas em testes, prints, issues ou Pull Requests. Use dados fictícios, inclusive nos dados de teste do app (`frontend/src/mocks/`);
- **Nunca teste o envio de WhatsApp com o número de outra pessoa** sem o consentimento dela. Use apenas o seu próprio número ou o número de teste do provedor;
- Ao incluir prints de telas ou de conversas, confira se não aparecem nomes, e-mails, telefones, alergias ou medicamentos reais;
- Em testes de acessibilidade com pessoas, peça consentimento antes de gravar ou fotografar, e use contas e medicamentos fictícios;
- Mudanças que coletem novos dados, ou que mudem o compartilhamento, devem atualizar este documento e ser registradas no [CHANGELOG.md](../CHANGELOG.md).

## Contato

Para exercer seus direitos, tirar dúvidas ou fazer solicitações sobre privacidade:

**amanda.db@uni9.edu.br**

Responderemos em até 7 dias úteis.

## Atualizações deste documento

Este documento deve ser revisado a cada nova versão do aplicativo e sempre que o tratamento de dados mudar. A data da última revisão é registrada no [CHANGELOG.md](../CHANGELOG.md). Última revisão: 30/10/2026.

> O MedControl é uma ferramenta de organização e **não substitui orientação médica**.

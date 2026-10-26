# Privacidade - MedControl

> Como o MedControl trata os dados pessoais e de saúde das pessoas que usam o aplicativo, com base na Lei Geral de Proteção de Dados (LGPD, Lei nº 13.709/2018).

## Por que isso importa?

O MedControl lida com informações sobre medicamentos, tratamentos, alergias e condições de saúde, que são **dados pessoais sensíveis** segundo a LGPD (dados referentes à saúde). Por isso, tratamos a privacidade como parte essencial do projeto, e não como um detalhe.

Este documento explica quais dados coletamos, para que usamos, onde ficam guardados, quais são os seus direitos e como falar conosco.

> O MedControl é um projeto acadêmico em desenvolvimento. Este documento descreve o funcionamento previsto e as intenções da equipe, e **não é um parecer jurídico**. Na versão atual, o aplicativo ainda usa dados de teste e **não envia dados para a API**; as regras abaixo valem para quando a integração for ativada.

## Quais dados coletamos?

| Categoria | Dados | Para que serve | Obrigatório? |
| :--- | :--- | :--- | :--- |
| **Conta** | Nome, e-mail, telefone, data de nascimento e senha | Criar a conta, fazer login e identificar o usuário | Sim |
| **Saúde (perfil)** | Tipo sanguíneo, alergias e condições crônicas | Manter as informações de saúde da pessoa à mão | Não |
| **Contato de emergência** | Nome e telefone | Ter um contato de confiança registrado | Não |
| **Medicamentos** | Nome, dosagem, quantidade por dose, tipo e instruções de uso, estoque e descrição | Organizar o tratamento e acompanhar o estoque | Nome, dosagem e quantidade |
| **Horários** | Horário e dias da semana de cada medicamento | Montar a lista de doses do dia | Sim, para aparecer em "Hoje" |
| **Histórico de doses** | Data e hora e se a dose foi tomada ou não | Mostrar o histórico e acompanhar a rotina | Sim, ao registrar uma dose |
| **Dados técnicos** | Token de login (JWT), com validade de 7 dias | Manter o usuário logado e garantir acesso apenas aos próprios dados | Sim |

**A senha nunca é guardada em texto puro.** A própria API do MedControl a transforma em *hash* (com bcrypt) antes de gravar no banco.

As **preferências de notificação** (lembrete de dose e alerta de estoque) ficam somente no aparelho e não são enviadas ao servidor.

### O que não coletamos

- Não coletamos localização, contatos do aparelho, fotos ou documentos;
- Não coletamos dados de pagamento;
- Não usamos os seus dados para publicidade nem para criar perfis comerciais.

**[CONFIRMAR: se o app, no futuro ou já agora, usar câmera (código de barras/OCR), localização ou envio de push com identificador do aparelho, atualize esta seção.]**

## Por que tratamos esses dados?

Usamos os dados **somente** para fazer o aplicativo funcionar:

- Criar e manter a sua conta;
- Cadastrar e organizar os seus medicamentos e horários;
- Registrar e exibir o seu histórico de doses;
- Mostrar o selo de estoque baixo;
- Guardar as informações de saúde e o contato de emergência que você escolher informar.

Os dados de saúde são tratados com base no **consentimento** da pessoa usuária, que ocorre ao criar a conta e ao preencher as informações. Os campos de saúde e de contato de emergência são **opcionais**: informe apenas o que se sentir à vontade para informar. **[CONFIRMAR: o app exibe um aceite deste documento no cadastro? Se não, inclua um checkbox "Li e concordo com a Política de Privacidade".]**

## Onde os dados ficam?

Os dados são armazenados no **Supabase** (banco de dados e infraestrutura), acessado exclusivamente pela API do MedControl (FastAPI). O Supabase atua como fornecedor de infraestrutura e pode armazenar dados em servidores fora do Brasil. **[CONFIRMAR: região do projeto Supabase, no painel do projeto.]**

## Como protegemos os dados?

- **Autenticação por JWT:** as rotas da API exigem login;
- **Acesso restrito:** cada usuário acessa somente os próprios dados;
- **Senha com hash:** nunca em texto puro;
- **Segredos fora do repositório:** chaves, senhas e o segredo do JWT ficam em variáveis de ambiente (`.env`), que nunca são versionadas (veja [IGNORE.md](../IGNORE.md));
- **Monitoramento do repositório:** o GitHub está configurado com alertas de dependências vulneráveis, detecção de segredos e relato privado de vulnerabilidades (veja [SECURITY.md](../SECURITY.md)).

Nenhum sistema é totalmente seguro. Por ser um projeto acadêmico mantido por uma equipe pequena, **não garantimos proteção absoluta** e recomendamos não cadastrar informações além das necessárias.

## Com quem compartilhamos?

**Não vendemos nem compartilhamos** os seus dados com terceiros para fins comerciais.

Os dados são acessados apenas pelo próprio usuário e pelos serviços técnicos necessários ao funcionamento do app (como o Supabase). Se um dia o **Modo Cuidador** for implementado (veja o roadmap no [README.md](../README.md)), o compartilhamento com familiares e cuidadores só ocorrerá **mediante autorização expressa do usuário**, que poderá revogá-la a qualquer momento.

## Por quanto tempo guardamos?

Os dados ficam armazenados enquanto a conta existir.

**Como a exclusão funciona hoje:** ao excluir a conta, ela é **desativada** (exclusão lógica). A conta e os dados associados deixam de ser acessíveis pelo aplicativo, mas **permanecem no banco de dados**, marcados como inativos, até serem removidos manualmente. Para pedir a remoção definitiva, escreva para o e-mail de contato. **[CONFIRMAR: prazo e procedimento da remoção definitiva, e se o e-mail de uma conta desativada pode ser reutilizado.]**

## Seus direitos

De acordo com a LGPD (art. 18), você pode, a qualquer momento:

| Direito | Como exercer |
| :--- | :--- |
| **Confirmar e acessar** os dados que temos sobre você | Pelo aplicativo (Ajustes, Medicamentos e Histórico) ou por e-mail |
| **Corrigir** dados incompletos ou incorretos | Editando o perfil, a conta e os medicamentos no aplicativo |
| **Excluir** os seus dados | Excluindo a conta no aplicativo (desativação) e pedindo a remoção definitiva por e-mail |
| **Revogar o consentimento** | Excluindo a conta ou solicitando por e-mail |
| **Obter informações** sobre o tratamento e o compartilhamento | Por e-mail |
| **Portabilidade** dos dados | Ainda não disponível. A exportação do histórico em PDF está prevista no roadmap |

## Crianças e adolescentes

O MedControl não foi pensado para menores de idade usarem sozinhos. Se o app for usado por ou para uma criança ou adolescente, o cadastro deve ser feito por um responsável legal.

## Incidentes de segurança

Se houver um incidente que possa afetar os seus dados, a equipe irá investigar, corrigir a falha, trocar as chaves afetadas (Supabase e JWT) e comunicar as pessoas impactadas. Para relatar uma vulnerabilidade, use o canal descrito em [SECURITY.md](../SECURITY.md) e **não abra issue pública**.

## Cuidados para quem contribui

- Nunca use dados reais de pessoas em testes, prints, issues ou Pull Requests. Use dados fictícios, inclusive nos dados de teste do app (`frontend/src/mocks/`);
- Ao incluir prints de telas, confira se não aparecem nomes, e-mails, telefones, alergias ou medicamentos reais;
- Em testes de acessibilidade com pessoas, peça consentimento antes de gravar ou fotografar, e use contas e medicamentos fictícios;
- Mudanças que coletem novos dados, ou que mudem o compartilhamento, devem atualizar este documento e ser registradas no [CHANGELOG.md](../CHANGELOG.md).

## Contato

Para exercer seus direitos, tirar dúvidas ou fazer solicitações sobre privacidade:

**amanda.db@uni9.edu.br**

Responderemos em até 7 dias úteis.

## Atualizações deste documento

Este documento deve ser revisado a cada nova versão do aplicativo e sempre que o tratamento de dados mudar. A data da última revisão é registrada no [CHANGELOG.md](../CHANGELOG.md). Última revisão: 25/10/2026.

> O MedControl é uma ferramenta de organização e **não substitui orientação médica**.

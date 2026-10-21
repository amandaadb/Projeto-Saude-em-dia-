# Privacidade - MedControl

> Como o MedControl trata os dados pessoais e de saúde das pessoas que usam o aplicativo, com base na Lei Geral de Proteção de Dados (LGPD, Lei nº 13.709/2018).

## Por que isso importa?

O MedControl lida com informações sobre medicamentos e tratamentos, que são **dados pessoais sensíveis** segundo a LGPD (dados referentes à saúde). Por isso, tratamos a privacidade como parte essencial do projeto, e não como um detalhe.

Este documento explica quais dados coletamos, para que usamos, onde ficam guardados, quais são os seus direitos e como falar conosco.

> O MedControl é um projeto acadêmico em desenvolvimento. Este documento descreve o funcionamento atual e as intenções da equipe, e **não é um parecer jurídico**.

## Quais dados coletamos?

| Categoria | Dados | Para que serve |
| :--- | :--- | :--- |
| **Conta** | Nome, e-mail e senha | Criar a conta, fazer login e identificar o usuário |
| **Medicamentos** | Nome, dose, frequência, horários e estoque (atual e mínimo) | Organizar o tratamento, enviar lembretes e alertar sobre estoque baixo |
| **Histórico de doses** | Horário previsto, horário do registro e status (tomada, adiada ou perdida) | Mostrar o histórico e acompanhar a rotina |
| **Dados técnicos** | Token de login (JWT) | Manter o usuário logado e garantir acesso apenas aos próprios dados |

**A senha nunca é guardada em texto puro.** Ela é armazenada apenas na forma de *hash*. **[CONFIRMAR: o hash é feito pela nossa API ou pelo serviço de autenticação do Supabase?]**

### O que não coletamos

- Não coletamos localização, contatos, fotos ou documentos do aparelho;
- Não coletamos dados de pagamento;
- Não usamos os seus dados para publicidade nem para criar perfis comerciais.

**[CONFIRMAR: se o app, no futuro ou já agora, usar câmera (código de barras/OCR), localização ou envio de push com identificador do aparelho, atualize esta seção.]**

## Por que tratamos esses dados?

Usamos os dados **somente** para fazer o aplicativo funcionar:

- Criar e manter a sua conta;
- Cadastrar e organizar os seus medicamentos e horários;
- Enviar lembretes e avisos de estoque baixo;
- Registrar e exibir o seu histórico de doses.

Os dados de saúde são tratados com base no **consentimento** da pessoa usuária, que ocorre ao criar a conta e cadastrar os próprios medicamentos. **[CONFIRMAR: o app exibe um aceite deste documento no cadastro? Se não, vale incluir um checkbox "Li e concordo com a Política de Privacidade".]**

## Onde os dados ficam?

Os dados são armazenados no **Supabase** (banco de dados e infraestrutura), acessado exclusivamente pela API do MedControl (FastAPI). O Supabase atua como fornecedor de infraestrutura e pode armazenar dados em servidores fora do Brasil. **[CONFIRMAR: região do projeto Supabase.]**

## Como protegemos os dados?

- **Autenticação por JWT:** as rotas da API exigem login;
- **Acesso restrito:** cada usuário acessa somente os próprios dados;
- **Segredos fora do repositório:** chaves, senhas e o segredo do JWT ficam em variáveis de ambiente (`.env`), que nunca são versionadas (veja [IGNORE.md](../IGNORE.md));
- **Monitoramento do repositório:** o GitHub está configurado com alertas de dependências vulneráveis, detecção de segredos e relato privado de vulnerabilidades (veja [SECURITY.md](../SECURITY.md)).

Nenhum sistema é totalmente seguro. Por ser um projeto acadêmico mantido por uma equipe pequena, **não garantimos proteção absoluta** e recomendamos não cadastrar informações além das necessárias.

## Com quem compartilhamos?

**Não vendemos nem compartilhamos** os seus dados com terceiros para fins comerciais.

Os dados são acessados apenas pelo próprio usuário e pelos serviços técnicos necessários ao funcionamento do app (como o Supabase). Se um dia o **Modo Cuidador** for implementado (veja o roadmap no [README.md](../README.md)), o compartilhamento com familiares e cuidadores só ocorrerá **mediante autorização expressa do usuário**, que poderá revogá-la a qualquer momento.

## Por quanto tempo guardamos?

Os dados ficam armazenados enquanto a conta existir. Ao excluir a conta, os dados associados devem ser removidos. **[CONFIRMAR: a exclusão do usuário também apaga medicamentos, horários e registros de dose (exclusão em cascata)? Se não, ajustar o back-end ou descrever aqui o que permanece.]**

## Seus direitos

De acordo com a LGPD (art. 18), você pode, a qualquer momento:

| Direito | Como exercer |
| :--- | :--- |
| **Confirmar e acessar** os dados que temos sobre você | Pelo aplicativo (telas de perfil, medicamentos e histórico) ou por e-mail |
| **Corrigir** dados incompletos ou incorretos | Editando o perfil e os medicamentos no aplicativo |
| **Excluir** os seus dados | Excluindo a conta no aplicativo ou solicitando por e-mail |
| **Revogar o consentimento** | Excluindo a conta ou solicitando por e-mail |
| **Obter informações** sobre o tratamento e o compartilhamento | Por e-mail |
| **Portabilidade** dos dados | Ainda não disponível. A exportação do histórico em PDF está prevista no roadmap |

## Crianças e adolescentes

O MedControl não foi pensado para menores de idade usarem sozinhos. Se o app for usado por ou para uma criança ou adolescente, o cadastro deve ser feito por um responsável legal.

## Incidentes de segurança

Se houver um incidente que possa afetar os seus dados, a equipe irá investigar, corrigir a falha, trocar as chaves afetadas (Supabase e JWT) e comunicar as pessoas impactadas. Para relatar uma vulnerabilidade, use o canal descrito em [SECURITY.md](../SECURITY.md) e **não abra issue pública**.

## Cuidados para quem contribui

- Nunca use dados reais de pessoas em testes, prints, issues ou Pull Requests. Use dados fictícios;
- Ao incluir prints de telas, confira se não aparecem nomes, e-mails ou medicamentos reais;
- Mudanças que coletem novos dados, ou que mudem o compartilhamento, devem atualizar este documento e ser registradas no [CHANGELOG.md](../CHANGELOG.md).

## Contato

Para exercer seus direitos, tirar dúvidas ou fazer solicitações sobre privacidade:

**amanda.db@uni9.edu.br**

Responderemos em até 7 dias úteis.

## Atualizações deste documento

Este documento deve ser revisado a cada nova versão do aplicativo e sempre que o tratamento de dados mudar. A data da última revisão é registrada no [CHANGELOG.md](../CHANGELOG.md).

> O MedControl é uma ferramenta de organização e **não substitui orientação médica**.

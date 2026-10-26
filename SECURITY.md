# Segurança - MedControl

> Política de segurança do projeto: quais versões recebem atualizações de segurança, o que é considerado uma vulnerabilidade e como relatar.

## Versões suportadas

Versões do MedControl que atualmente recebem atualizações de segurança:

| Versão | Suportada |
| :--- | :--- |
| 1.x.x | Sim |
| < 1.0 | Não |

O projeto é acadêmico e está em desenvolvimento. Ainda não há versão publicada para o público.

## Relatando uma vulnerabilidade

Se você encontrar uma vulnerabilidade de segurança no MedControl, **não abra uma issue pública**. Use um dos canais abaixo:

- **GitHub (recomendado):** na aba **Security** do repositório, clique em **Report a vulnerability**. O relato fica privado e restrito à equipe;
- **E-mail:** **amanda.db@uni9.edu.br**.

Ao relatar, inclua sempre que possível:

- Uma descrição da vulnerabilidade e seu possível impacto;
- Passos para reproduzir o problema;
- Parte afetada (aplicativo, API ou banco) e versão;
- Sugestão de correção, se tiver uma.

## O que é considerado uma vulnerabilidade?

Por exemplo:

- Acesso aos dados de outra pessoa usuária;
- Contorno da autenticação ou do controle de acesso;
- Exposição de segredos (chaves do Supabase, segredo do JWT, senhas);
- Falhas que permitam alterar ou apagar dados de outras pessoas;
- Dados de saúde enviados ou guardados sem proteção.

Não são consideradas vulnerabilidades: problemas de acessibilidade (veja [ACCESSIBILITY.md](./ACCESSIBILITY.md)), bugs sem impacto de segurança (use o modelo de bug) e relatos sobre dados de teste do app.

## Se você encontrou um segredo no repositório

Avise a equipe imediatamente pelos canais acima. Os segredos afetados (chaves do Supabase e segredo do JWT) devem ser **trocados**, mesmo que o arquivo já tenha sido removido, porque o histórico do Git continua guardando o conteúdo.

### O que esperar?

- **Confirmação de recebimento:** em até 2 dias úteis;
- **Atualização sobre o andamento:** em até 7 dias úteis;
- **Se aceita:** trabalharemos em uma correção e você será avisado(a) quando for publicada, com crédito pelo reporte (caso deseje);
- **Se recusada:** explicaremos o motivo.

Por ser um projeto acadêmico mantido por uma equipe pequena, não prometemos prazo de correção. Veja também [docs/privacidade.md](./docs/privacidade.md).

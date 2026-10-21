# Contribuindo - MedControl

> Guia para quem quer colaborar com o projeto: como organizar o trabalho, escrever commits, enviar alterações e manter a documentação em dia.

## Antes de começar

O MedControl é um projeto acadêmico sob **licença proprietária**. Por isso:

- **Integrantes da equipe** podem contribuir livremente, seguindo este guia;
- **Pessoas de fora da equipe** precisam de autorização prévia e por escrito de todos os titulares antes de enviar qualquer alteração. Para solicitar, escreva para **amanda.db@uni9.edu.br**.

Ao participar, você concorda em seguir o [Código de Conduta](./CODE_OF_CONDUCT.md).

## Como contribuir?

1. Combine a tarefa com a equipe (grupo do WhatsApp) para evitar trabalho duplicado;
2. Atualize sua cópia local antes de começar;
3. Crie uma branch própria para a tarefa;
4. Faça as alterações e teste localmente;
5. Envie a branch e abra um Pull Request;
6. Aguarde a revisão de pelo menos um integrante antes de mesclar.

## Branches

Nunca trabalhe direto na `main`. Use nomes curtos, em minúsculas e com hífens, começando pelo tipo da alteração:

| Prefixo | Quando usar | Exemplo |
| :--- | :--- | :--- |
| `feat/` | Nova funcionalidade | `feat/alerta-estoque-baixo` |
| `fix/` | Correção de bug | `fix/login-token-expirado` |
| `docs/` | Documentação | `docs/code-of-conduct` |
| `refactor/` | Melhoria de código sem mudar o comportamento | `refactor/rotas-medicamentos` |
| `test/` | Criação ou ajuste de testes | `test/cadastro-usuario` |

## Mensagens de commit

Escreva em português, no imperativo e de forma objetiva, com o tipo no início:

```text
feat: adiciona listagem de medicamentos do usuário
fix: corrige desconto de estoque ao registrar dose
docs: cria CODE_OF_CONDUCT.md
```

Um commit deve representar uma mudança com um único propósito.

## Pull requests

Ao abrir um Pull Request, descreva:

- **O que** foi alterado e **por quê**;
- **Como testar** a alteração;
- Se há **mudanças no banco de dados** (o restante da equipe precisa saber);
- Prints das telas, quando a mudança for visual.

O repositório já traz um modelo de Pull Request (`.github/PULL_REQUEST_TEMPLATE.md`) com esses campos. Basta preenchê-lo ao abrir o PR.

Antes de pedir a revisão, confira se:

- [ ] O código roda localmente sem erros;
- [ ] Nenhum arquivo sensível foi incluído (veja a seção abaixo);
- [ ] A documentação afetada foi atualizada;
- [ ] O `CHANGELOG.md` recebeu uma entrada com a alteração.

## Segurança e segredos

- **Nunca** envie o `.env`, chaves do Supabase, segredo do JWT, senhas ou certificados para o repositório. Veja a lista completa em [IGNORE.md](./IGNORE.md);
- Se um segredo for enviado por engano, avise a equipe e **troque imediatamente** as chaves do Supabase e o segredo do JWT;
- Para relatar vulnerabilidades, siga o [SECURITY.md](./SECURITY.md). **Não abra issue pública.**

## Padrões do projeto

### Back-end (FastAPI)

- Proteja as rotas com a autenticação JWT: cada usuário só acessa os próprios dados;
- Valide os dados recebidos e retorne mensagens de erro claras;
- Qualquer mudança na estrutura do banco deve ser comunicada à equipe e refletida em `docs/diagramas.md`.

### Front-end

- Siga a identidade visual definida em [UI-UX.md](./UI-UX.md) (cores, fontes e componentes);
- Reutilize os componentes catalogados em [COMPONENTS.md](./COMPONENTS.md) antes de criar novos;
- Mantenha a acessibilidade: fontes legíveis, bom contraste e telas simples, pensando em idosos;
- Siga as expectativas de [ACCESSIBILITY.md](./ACCESSIBILITY.md) em toda mudança visual.

### Documentação

- Os documentos seguem o padrão visual dos já existentes: título, descrição em citação (`>`) e seções com `##`;
- Alterações em fluxos, telas ou dados devem atualizar `docs/diagramas.md` e `docs/proposta.md`;
- Mantenha o aviso de que o MedControl **não substitui orientação médica**.

## Registro de alterações

Toda alteração relevante deve ser registrada no [CHANGELOG.md](./CHANGELOG.md), no formato [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/), com a data no topo e as categorias `Adicionado`, `Alterado` ou `Corrigido`.

## Dúvidas

- **Equipe:** grupo do WhatsApp do projeto;
- **Demais pessoas:** **amanda.db@uni9.edu.br**. Veja também o [SUPPORT.md](./SUPPORT.md).

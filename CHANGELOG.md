# Registro de Alterações - MedControl

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

O formato segue o padrão [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).

---

## [2026-10-17]

### Alterado
- `README.md`: telas do aplicativo reorganizadas em tabela, com as versões horizontais em seção recolhível.

## [2026-10-16]

### Adicionado
- Ativados o Private vulnerability reporting e os recursos do Advanced Security (Dependabot alerts, Secret scanning e Push protection).
- Adicionada a imagem de pré-visualização social (Social preview) do repositório, no tamanho 1280×640 px.

### Alterado
- `SECURITY.md`: relato privado de vulnerabilidades pelo GitHub incluído como canal recomendado, mantendo o e-mail como alternativa.
- Detalhes do repositório (About) atualizados, com nova descrição e inclusão dos topics.
- Configurações do repositório ajustadas em Settings, nas seções General, Pull Requests e Branches.

## [2026-10-15]

### Adicionado
- Criados `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md` e `ACCESSIBILITY.md`.
- Criados os templates de Pull Request (`.github/PULL_REQUEST_TEMPLATE.md`) e de issue (`.github/ISSUE_TEMPLATE/bug_report.md`, `feature_request.md` e `accessibility_issue.md`).
- Criada a página inicial (`Home`) da wiki, com links para a documentação do repositório.

### Alterado
- `README.md`: adicionados os links para `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `ACCESSIBILITY.md` e para a wiki.
- `CONTRIBUTING.md`: adicionada a referência ao `ACCESSIBILITY.md` na seção de Front-end e ao modelo de Pull Request na seção de Pull Requests.

## [2026-10-14]

### Adicionado
- Criado `docs/diagramas.md` com fluxogramas e diagramas UML.

## [2026-10-13]

### Alterado
- `README.md`: adicionada a seção de Melhorias Futuras (Roadmap).

## [2026-10-06]

### Adicionado
- Criada a branch de desenvolvimento `develop`.

## [2026-10-05]

### Adicionado
- Criado `docs/proposta.md`.

## [2026-09-30]

### Alterado
- `.gitignore`, `LICENSE`, `IGNORE.md` e `LICENSED.md`: padronização visual.

## [2026-09-29]

### Adicionado
- Criados `.gitignore`, `LICENSE`, `IGNORE.md` e `LICENSED.md`.

### Alterado
- `README.md`: adicionados os links para `IGNORE.md` e `LICENSED.md`.

## [2026-09-22]

### Alterado
- `README.md`: adicionadas mais informações gerais do projeto.

## [2026-09-18]

### Alterado
- `README.md`: adicionada a parte que faltava dos protótipos das telas do aplicativo.

## [2026-09-16]

### Adicionado
- Inserido o protótipo de logo do MedControl em `UI-UX.md`.

### Alterado
- `README.md`: adicionada parte dos protótipos das telas do aplicativo.

## [2026-09-14]

### Alterado
- `README.md` e `CHANGELOG.md`: padronização visual.

## [2026-09-13]

### Adicionado
- Criado `SECURITY.md`.

### Alterado
- `UI-UX.md`, `SUPPORT.md` e `COMPONENTS.md`: padronização visual.

## [2026-09-12]

### Alterado
- `README.md`: adicionadas mais informações gerais do projeto, incluindo as funções dos membros da equipe e o copyright.

## [2026-09-11]

### Adicionado
- Criados `UI-UX.md`, `COMPONENTS.md` e `SUPPORT.md`.

### Alterado
- `README.md`: adicionadas mais informações gerais do projeto, incluindo os membros da equipe e seus RAs.

## [2026-09-10]

### Alterado
- `README.md`: adicionadas informações gerais e detalhadas sobre o projeto, abrangendo as telas do sistema, as funcionalidades principais, as diretrizes de acessibilidade e o fluxo de navegação do usuário.

## [2026-09-09]

### Alterado
- `README.md`: adicionadas informações gerais do projeto.

## [2026-09-07]

### Adicionado
- Adicionada a rota de medicamentos (cadastro, atualização, exclusão e listagem).

### Alterado
- Estrutura do banco de dados atualizada.

### Corrigido
- Cadastro de usuários (atualização e exclusão).
- Ajuste para a conta permanecer logada.

## [2026-09-04]

### Adicionado
- Estrutura inicial do backend com FastAPI, autenticação JWT e integração com Supabase.

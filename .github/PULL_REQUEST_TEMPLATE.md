# Pull Request - MedControl

> Modelo para descrever alterações enviadas ao projeto, facilitando a revisão pela equipe.

## O que foi alterado e por quê

<!-- Explique de forma objetiva a mudança e o motivo dela. -->

## Tipo de alteração

- [ ] `feat`: nova funcionalidade
- [ ] `fix`: correção de bug
- [ ] `docs`: documentação
- [ ] `refactor`: melhoria de código sem mudar o comportamento
- [ ] `test`: criação ou ajuste de testes

## Como testar

<!-- Passo a passo para quem for revisar. -->

1.
2.
3.

## Mudanças no banco de dados

- [ ] Não há mudanças no banco de dados
- [ ] Há mudanças (descreva abaixo e atualize `docs/diagramas.md`)

<!-- Descreva as tabelas ou campos alterados, se houver. -->

## Prints (se a mudança for visual)

<!-- Inclua prints de antes e depois. Se testou com fonte aumentada, tela pequena ou leitor de tela, conte aqui. -->

## Checklist

- [ ] O Pull Request aponta para a `develop`
- [ ] O código roda localmente sem erros
- [ ] `npm run lint` e `npx tsc --noEmit` passam (front-end)
- [ ] Nenhum arquivo sensível foi incluído (`.env`, chaves do Supabase, segredo do JWT, senhas)
- [ ] Não há dados reais de pessoas em prints, testes ou dados de teste
- [ ] A documentação afetada foi atualizada (`COMPONENTS.md`, `docs/diagramas.md`, `docs/privacidade.md` etc.)
- [ ] O `CHANGELOG.md` recebeu uma entrada com a alteração
- [ ] Em mudanças visuais, as expectativas do `ACCESSIBILITY.md` foram seguidas

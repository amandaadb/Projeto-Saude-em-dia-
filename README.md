# Leia-me - MedControl

> O **MedControl** é um aplicativo que ajuda os usuários a organizar medicamentos, horários e tratamentos, reduzindo o risco de esquecimentos ou de uso fora do horário recomendado.

<img width="1254" height="1254" alt="Logo" src="https://github.com/user-attachments/assets/2dbb2cc5-7597-4df6-a664-2821c9ec5589" />

Documentação relacionada: [Proposta](./docs/proposta.md) · [Diagramas](./docs/diagramas.md) · [Protótipo](./docs/prototipo.md) · [UI/UX](./UI-UX.md) · [Componentes](./COMPONENTS.md) · [Acessibilidade](./ACCESSIBILITY.md) · [Front-end](./frontend/README.md) · [Back-end](./backend/README.md) · [Changelog](./CHANGELOG.md) · [Suporte](./SUPPORT.md) · [Segurança](./SECURITY.md) · [Privacidade](./docs/privacidade.md) · [Código de Conduta](./CODE_OF_CONDUCT.md) · [Contribuindo](./CONTRIBUTING.md) · [Licença](./LICENSE) · [Licenciados](./LICENSED.md) · [Ignorados](./IGNORE.md) · [Wiki](https://github.com/amandaadb/Projeto-Saude-em-dia-/wiki)

> **Sobre o nome:** o produto se chama **MedControl**. O nome do repositório e o título da API ("Saúde em Dia") vêm de uma fase anterior do projeto.

---

## Situação do projeto

O projeto é acadêmico e está em desenvolvimento. O back-end e o front-end existem, mas **ainda não estão integrados**: o aplicativo funciona com dados de teste (`frontend/src/mocks/`).

| Funcionalidade | Back-end | Front-end | Integrado |
| :--- | :--- | :--- | :--- |
| Cadastro, login e perfil | Sim | Perfil e conta em Ajustes; tela de login **[CONFIRMAR]** | Não |
| Medicamentos (cadastrar, editar, excluir) | Sim | Sim | Não |
| Horários dos medicamentos (rotinas) | Sim | Sim | Não |
| Registro de dose (tomei / não tomei) e histórico | Sim | Sim | Não |
| Estoque | Campo no banco | Ajuste manual (+/-) e selo de estoque baixo | Não |
| Lembretes por WhatsApp | Não | Não (o interruptor em Ajustes ainda não tem efeito) | Não |
| Notificações do celular | Não | Não | Não |
| Integração com Google Agenda e calendário do celular | Não | Não | Não |

Observações importantes:

- O estoque **não é descontado automaticamente** ao registrar uma dose;
- O limite de "estoque baixo" é fixo em 5 unidades no app;
- Os lembretes estão no roadmap e **não funcionam** na versão atual. O canal inicial será o **WhatsApp** (enviado pelo servidor); depois virão as notificações do celular e a integração com agendas;
- Telas de Consultas e receitas, Recompensas e Modo Cuidador estão fora do MVP.

## Tecnologias

| Camada | Tecnologias |
| :--- | :--- |
| Front-end | React Native, Expo (SDK 57), Expo Router, TypeScript |
| Back-end | Python, FastAPI, autenticação JWT, bcrypt |
| Banco de dados | Supabase (PostgreSQL) |
| Lembretes (planejado) | Provedor de WhatsApp (a definir), notificações do celular e Google Agenda |

## Estrutura do repositório

```text
.
├── backend/      API em FastAPI e script do banco (tables.sql)
├── frontend/     Aplicativo React Native + Expo
├── docs/         Proposta, diagramas, protótipo e privacidade
├── .github/      Modelos de issue e de Pull Request
└── *.md          Documentos do projeto (acessibilidade, UI/UX etc.)
```

## Como rodar

- **Back-end:** veja [backend/README.md](./backend/README.md);
- **Front-end:** veja [frontend/README.md](./frontend/README.md).

## Equipe

| RA | Integrante | GitHub |
| :--- | :--- | :--- |
| `3024104773` | Amanda Dias Barreto | [@amandaadb](https://github.com/amandaadb) |
| `3024100161` | Daniela Rosa | [@Mrsdanielar](https://github.com/Mrsdanielar) |
| `3024103168` | Gabriel Cruz Sanchez | [@gabrielcruzsz](https://github.com/gabrielcruzsz) |
| `3024105062` | Guilherme Alves Galeano | [@Guigalean006](https://github.com/Guigalean006) |
| `3024103605` | Luana Marcelino Andrade | [@Luana-Andrad](https://github.com/Luana-Andrad) |
| `3024107159` | Lucas Gomes Barboza | [@oLucasGBo](https://github.com/oLucasGBo) |
| `3024106574` | Renan Abreu Cerqueira de Lima | [@RenanAbreuC](https://github.com/RenanAbreuC) |

## Responsabilidades

### Gestão e análise - *Amanda*

- Organização do cronograma e das entregas;
- Acompanhamento das tarefas da equipe;
- Levantamento de requisitos;
- Definição de objetivos, público-alvo e regras de negócio;
- Recebimento dos relatos de usuários (suporte, acessibilidade e privacidade).

### UX/UI, protótipo e GitHub - *Gabriel*

- Criação da identidade visual (cores, fontes e componentes);
- Prototipação das telas e fluxo de navegação;
- Acessibilidade de design (contraste, tamanhos e estados visuais);
- Organização do repositório e da documentação no GitHub.

### Front-end e telas - *Daniela e Luana*

- Desenvolvimento e estilização das telas;
- Implementação da responsividade e da acessibilidade visual;
- Configuração das rotas de navegação;
- Integração com os endpoints da API fornecida pelo Back-end.

### Back-end e banco de dados - *Lucas e Renan*

- Modelagem do banco de dados;
- Criação de tabelas e entidades;
- Implementação de CRUD;
- Autenticação e regras de acesso;
- Disponibilização dos endpoints da API para o Front-end.

### Testes e documentação - *Guilherme*

- Criação e execução de casos de teste;
- Registro e acompanhamento de bugs;
- Elaboração da documentação técnica;
- Criação dos diagramas UML.

## Para quem este aplicativo é voltado?

O MedControl é voltado para o público geral, com foco na gestão da saúde e no acompanhamento de tratamentos contínuos. Público-alvo principal:

- **Pacientes em tratamento:** pessoas que fazem uso diário de medicamentos ou possuem condições de saúde que exigem acompanhamento contínuo;
- **Familiares e cuidadores:** pessoas responsáveis por gerenciar, organizar e acompanhar a rotina de medicação de entes queridos ou pacientes sob seus cuidados (o vínculo entre contas ainda é uma funcionalidade planejada).

## Telas do aplicativo

O aplicativo implementado tem quatro abas e um formulário:

| Tela | O que faz |
| :--- | :--- |
| Hoje | Próximas doses do dia, com status e registro de "Tomei" ou "Não tomei" |
| Medicamentos | Lista, ajuste de estoque e acesso ao formulário |
| Formulário de medicamento | Cadastro, edição e exclusão, com horários |
| Histórico | Doses registradas, agrupadas por dia, com filtro |
| Ajustes | Perfil, dados de saúde, conta, preferências de notificação, sair e excluir conta |

Abaixo, uma prévia do **protótipo visual**, que pode diferir do app implementado. Todas as telas, em tamanho maior, estão em [docs/prototipo.md](./docs/prototipo.md).

<!-- manter aqui as duas tabelas de imagens atuais da seção "Telas do aplicativo" -->

## Melhorias futuras (roadmap)

O **MedControl** foi desenvolvido para facilitar a organização de medicamentos e o acompanhamento de tratamentos contínuos. Nas próximas versões, planejamos ampliar suas funcionalidades, acessibilidade, segurança e praticidade, com foco em **suporte familiar**, **automação** e **facilidade de uso**.

- [ ] **Integração do app com a API:** trocar os dados de teste pelas chamadas reais.
- [ ] **Lembretes de dose por WhatsApp:** mensagem no horário da dose, com consentimento próprio e opção de desativar.
- [ ] **Notificações do celular:** avisos gerados pelo aparelho, com opção de vibração e de adiar.
- [ ] **Integração com Google Agenda e calendário do celular:** criar os horários dos medicamentos na agenda, mediante autorização.
- [ ] **Alertas inteligentes:** aviso de doses atrasadas e de estoque baixo pelos canais acima.
- [ ] **Desconto automático de estoque** ao registrar uma dose, com limite de alerta configurável.
- [ ] **Modo Cuidador:** vínculo entre contas, sempre mediante autorização do usuário.
- [ ] **Gestão de consultas e receitas:** registro, com lembretes de retorno e renovação.
- [ ] **Cadastro facilitado de medicamentos:** código de barras, QR Code ou OCR.
- [ ] **Relatórios e estatísticas:** gráficos de adesão e exportação do histórico em PDF.
- [ ] **Acessibilidade aprimorada:** ajuste de fonte, alto contraste, leitor de tela e navegação simplificada (veja [ACCESSIBILITY.md](./ACCESSIBILITY.md)).
- [ ] **Segurança e privacidade:** autenticação em dois fatores e controles de compartilhamento, em conformidade com a LGPD.
- [ ] **Modo offline-first:** funcionamento sem internet, com sincronização automática.
- [ ] **Testes automatizados:** testes unitários e de interface.

> As melhorias serão avaliadas conforme a viabilidade técnica, as necessidades dos usuários e a evolução do projeto. As funcionalidades listadas são possibilidades futuras e **não estão implementadas** na versão atual.

---

> O MedControl é uma ferramenta de organização e **não substitui orientação médica**.

---

© 2026 MedControl. Todos os direitos reservados.

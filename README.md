# Leia-me - MedControl

O **MedControl** é um aplicativo desenvolvido com o objetivo de ajudar os usuários a organizar medicamentos, horários, consultas e tratamentos, reduzindo o risco de esquecimentos ou de uso fora do horário recomendado.

<img width="1254" height="1254" alt="Logo" src="https://github.com/user-attachments/assets/2dbb2cc5-7597-4df6-a664-2821c9ec5589" />

Documentação relacionada: [Proposta](./docs/proposta.md) · [Diagramas](./docs/diagramas.md) · [Protótipo](./docs/prototipo.md) · [UI/UX](./UI-UX.md) · [Componentes](./COMPONENTS.md) · [Acessibilidade](./ACCESSIBILITY.md) · [Changelog](./CHANGELOG.md) · [Suporte](./SUPPORT.md) · [Segurança](./SECURITY.md) · [Privacidade](./docs/privacidade.md) · [Código de Conduta](./CODE_OF_CONDUCT.md) · [Contribuindo](./CONTRIBUTING.md) · [Licença](./LICENSE) · [Licenciados](./LICENSED.md) · [Ignorados](./IGNORE.md) · [Wiki](https://github.com/amandaadb/Projeto-Saude-em-dia-/wiki)

---

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

### Gestão e Análise - *Amanda*
- Organização do cronograma e das entregas
- Acompanhamento das tarefas da equipe
- Levantamento de requisitos
- Definição de objetivos, público-alvo e regras de negócio

### UX/UI e Protótipo - *Gabriel*
- Criação da identidade visual (cores, fontes e componentes)
- Prototipação das telas
- Elaboração do fluxo de navegação
- Elaboração do README com apresentação visual do projeto

### Front-end e Telas - *Daniela e Luana*
- Desenvolvimento e estilização das telas de login, cadastro, início etc
- Implementação da responsividade e acessibilidade visual
- Configuração das rotas de navegação entre as telas do aplicativo
- Consumo dos endpoints da API fornecida pelo Back-end

### Back-end e Banco de Dados - *Lucas e Renan*
- Modelagem do banco de dados
- Criação de tabelas e entidades
- Implementação de CRUD
- Autenticação e regras de acesso
- Disponibilização dos endpoints da API para o Front-end

### Testes e Documentação - *Guilherme*
- Criação e execução de casos de teste
- Registro e acompanhamento de bugs
- Elaboração da documentação técnica
- Criação dos diagramas UML

## Para Quem Este Aplicativo é Voltado?

O MedControl é voltado para o público geral, com foco na gestão da saúde e no acompanhamento de tratamentos contínuos. Público-alvo principal:

- **Pacientes em tratamento:** pessoas que fazem uso diário de medicamentos ou possuem condições de saúde que exigem acompanhamento contínuo;
- **Familiares e cuidadores:** pessoas responsáveis por gerenciar, organizar e acompanhar a rotina de medicação de entes queridos ou pacientes sob seus cuidados.

## Telas do Aplicativo

| Login e Cadastro | Início | Resumo do Dia | Menu Principal | Controle de Estoque |
| :---: | :---: | :---: | :---: | :---: |
| <img width="160" alt="Tela de Login e Cadastro" src="https://github.com/user-attachments/assets/7a5fbd88-3e3e-4865-8728-049e16e3a15e" /> | <img width="160" alt="Tela de Início" src="https://github.com/user-attachments/assets/30784122-c897-426d-9442-ad8b7272855a" /> | <img width="160" alt="Tela de Resumo do Dia" src="https://github.com/user-attachments/assets/5f317120-1b94-4ac9-bcc9-06c9f2c82b31" /> | <img width="160" alt="Tela do Menu Principal" src="https://github.com/user-attachments/assets/38dd3ca0-05f7-435a-89e9-654cf4561749" /> | <img width="160" alt="Tela de Controle de Estoque" src="https://github.com/user-attachments/assets/67336fbe-8fc8-4c88-b051-c3a3a4d1e1d0" /> |

| Histórico | Consultas e Receitas | Perfil | Acessibilidade | Recompensas |
| :---: | :---: | :---: | :---: | :---: |
| <img width="160" alt="Tela de Histórico" src="https://github.com/user-attachments/assets/503584d8-d4af-4c29-8cb2-e77fbd851817" /> | <img width="160" alt="Tela de Consultas e Receitas" src="https://github.com/user-attachments/assets/cda53cc6-e459-4638-b156-4b9de5c55cf7" /> | <img width="160" alt="Tela de Perfil" src="https://github.com/user-attachments/assets/5a02c69f-4f70-4170-b42b-e15e7eb448b9" /> | <img width="160" alt="Tela de Acessibilidade" src="https://github.com/user-attachments/assets/d632254a-0e1d-4d59-843a-19a817d96957" /> | <img width="160" alt="Tela de Recompensas" src="https://github.com/user-attachments/assets/6bb4a966-13ba-41d5-8e38-c62cc29f884e" /> |

Veja todas as telas em tamanho maior, com as versões de apresentação e o fluxo de navegação, em [docs/prototipo.md](./docs/prototipo.md).

## Melhorias Futuras (Roadmap)

O **MedControl** foi desenvolvido para facilitar a organização de medicamentos e o acompanhamento de tratamentos contínuos. Nas próximas versões, planejamos ampliar suas funcionalidades, acessibilidade, segurança e praticidade, com foco em **suporte familiar**, **automação** e **facilidade de uso**.

### Funcionalidades Planejadas

- [ ] **Modo Cuidador:** vínculo entre contas para que familiares e cuidadores acompanhem a rotina de medicação, sempre mediante autorização do usuário.
- [ ] **Notificações Inteligentes:** lembretes personalizáveis, alertas de doses atrasadas e opção de adiar notificações.
- [ ] **Controle Avançado de Estoque:** estimativa de duração dos medicamentos disponíveis e aviso de reposição.
- [ ] **Gestão de Consultas e Receitas:** registro de consultas e receitas, com lembretes de retorno e de renovação.
- [ ] **Cadastro Facilitado de Medicamentos:** leitura de código de barras, QR Code ou OCR da embalagem para agilizar o cadastro.
- [ ] **Relatórios e Estatísticas:** gráficos de adesão ao tratamento e exportação do histórico de doses em PDF para levar às consultas.
- [ ] **Acessibilidade Aprimorada:** ajuste de fonte, alto contraste, suporte a leitores de tela e navegação simplificada.
- [ ] **Segurança e Privacidade:** autenticação em dois fatores, controles de compartilhamento e proteção adicional dos dados, em conformidade com a LGPD.
- [ ] **Modo Offline-First:** funcionamento sem internet, com sincronização automática via Supabase.
- [ ] **Testes Automatizados:** testes unitários (Pytest) e de interface para maior estabilidade.

> As melhorias serão avaliadas conforme a viabilidade técnica, as necessidades dos usuários e a evolução do projeto. As funcionalidades listadas são possibilidades futuras e **não estão implementadas** na versão atual.

---

> **Aviso:** o MedControl é uma ferramenta de organização e acompanhamento e **não substitui a orientação de médicos ou outros profissionais de saúde**.

---

© 2026 MedControl. Todos os direitos reservados.

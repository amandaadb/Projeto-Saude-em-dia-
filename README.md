# MedControl 💊

O **MedControl** é um aplicativo desenvolvido com o objetivo de ajudar os usuários a organizar medicamentos, horários, consultas e tratamentos, reduzindo o risco de esquecimentos ou de uso fora do horário recomendado.

<img width="1254" height="1254" alt="Logo" src="https://github.com/user-attachments/assets/2dbb2cc5-7597-4df6-a664-2821c9ec5589" />

📄 Documentação relacionada: [UI/UX](./UI-UX.md) · [Componentes](./COMPONENTS.md) · [Suporte](./SUPPORT.md) · [Segurança](./SECURITY.md) · [Changelog](./CHANGELOG.md)

---

## 👥 Equipe

| RA | Integrante | GitHub |
| :--- | :--- | :--- |
| `3024104773` | Amanda Dias Barreto | [@amandaadb](https://github.com/amandaadb) |
| `3024100161` | Daniela Rosa | [@Mrsdanielar](https://github.com/Mrsdanielar) |
| `3024103168` | Gabriel Cruz Sanchez | [@gabrielcruzsz](https://github.com/gabrielcruzsz) |
| `3024105062` | Guilherme Alves Galeano | [@Guigalean006](https://github.com/Guigalean006) |
| `3024103605` | Luana Marcelino Andrade | [@Luana-Andrad](https://github.com/Luana-Andrad) |
| `3024107159` | Lucas Gomes Barboza | [@oLucasGBo](https://github.com/oLucasGBo) |
| `3024106574` | Renan Abreu Cerqueira de Lima | [@RenanAbreuC](https://github.com/RenanAbreuC) |

## 🧩 Responsabilidades

### 📋 Gestão e Análise - *Amanda*
- Organização do cronograma e das entregas
- Acompanhamento das tarefas da equipe
- Levantamento de requisitos
- Definição de objetivos, público-alvo e regras de negócio

### 🎨 UX/UI e Protótipo - *Amanda e Gabriel*
- Criação da identidade visual (cores, fontes e componentes)
- Prototipação das telas
- Elaboração do fluxo de navegação
- Foco em usabilidade, com atenção especial ao público idoso

### 💻 Front-end - Telas e Medicamentos - *Daniela e Luana*
- Telas de login, cadastro, dashboard, perfil e navegação principal
- Integração das telas com o sistema
- Cadastro de medicamentos, horários e tratamentos
- Registro de doses e tela de histórico

### 🗄️ Back-end e Banco de Dados - *Lucas e Renan*
- Modelagem do banco de dados
- Criação de tabelas e entidades
- Implementação de CRUD
- Autenticação e regras de acesso
- Integração entre aplicativo e banco de dados

### 🧪 Testes e Documentação - *Guilherme*
- Criação e execução de casos de teste
- Registro e acompanhamento de bugs
- Elaboração do README e da documentação técnica
- Apoio na criação dos diagramas UML

## 🎯 Para quem este aplicativo é voltado?

O MedControl é voltado para o público geral, com foco na gestão da saúde e no acompanhamento de tratamentos contínuos. Público-alvo principal:

- **Pacientes em tratamento:** pessoas que fazem uso diário de medicamentos ou possuem condições de saúde que exigem acompanhamento contínuo;
- **Familiares e cuidadores:** pessoas responsáveis por gerenciar, organizar e acompanhar a rotina de medicação de entes queridos ou pacientes sob seus cuidados.

## 📱 Telas do aplicativo

### Tela inicial

<img width="853" height="1843" alt="Tela Inicial" src="https://github.com/user-attachments/assets/c30618dd-ccf6-4a56-b3fc-95ea82420f6a" />

### Resumo do dia

<img width="853" height="1844" alt="Resumo do Dia" src="https://github.com/user-attachments/assets/2edf7236-0f3f-4c45-8c5b-30e1161571b2" />

### Menu principal

Navegação inferior sempre visível:

`🏠 Início` · `💊 Medicamentos` · `📊 Histórico` · `📅 Consultas` · `👤 Perfil`

### Tela de histórico

| Dia | Horário | Medicamento | Status |
|---|---|---|---|
| Segunda-feira | 08:00 | Losartana | ✅ Tomado |
| Segunda-feira | 20:00 | Losartana | ✅ Tomado |
| Terça-feira | 08:00 | Losartana | ✅ Tomado |
| Terça-feira | 20:00 | Losartana | ❌ Não tomado |
| Quarta-feira | 08:00 | Losartana | ✅ Tomado |
| Quarta-feira | 20:00 | Losartana | ⏰ Aguardando |

### Controle de estoque

Cadastro de medicamento via assistente guiado passo a passo.

- 💊 Losartana 50 mg
- **Quantidade atual:** 32 comprimidos
- **Consumo:** 2 por dia
- **Previsão:** 16 dias
- ⚠️ Alerta: "Seu medicamento pode acabar em aproximadamente 16 dias."
- Notificação: `Configurar alerta`

### Consultas e receitas

**Próxima consulta**
- 📅 18 de setembro, 🕐 14:30
- 🏥 Cardiologista
- Lembrar-me: 1 dia antes / 2 horas antes

**Receita**
- 💊 Losartana 50 mg
- Renovação prevista: 25/09

## ✨ Funcionalidades extras

- **Modo cuidador inteligente:** envia alertas automáticos se o paciente não confirmar a dose;
- **Relatórios exportáveis:** PDF simples com adesão ao tratamento, para levar ao médico;
- **Modo offline:** lembretes funcionam mesmo sem internet.

## ♿ Acessibilidade

- Botões grandes e ícones intuitivos (💊, ⏰, ✅);
- Modo "alto contraste" e "texto ampliado" (avaliar deixar como padrão);
- Tutorial inicial com voz explicando cada função;
- Feedback sonoro suave para confirmar ações.

## 🏅 Recompensas

- Medalhas por adesão (ex.: "7 dias sem esquecer!");
- Ranking pessoal de consistência;
- Recompensas simbólicas (ex.: "Você está cuidando bem da sua saúde!").

## 🔄 Fluxo do aplicativo

1. Abrir app
2. Login / Cadastro
3. Configurar perfil
4. Adicionar medicamento (nome, dosagem, quantidade, forma de uso, horários)
5. Salvar
6. MedControl gera os horários automaticamente
7. Notificação: *"Hora do medicamento!"*
8. Usuário escolhe: `✅ Tomei` · `⏰ Lembrar depois` · `❌ Não tomei`
9. Registro salvo no histórico
10. Acompanhamento contínuo

---

© 2026 MedControl. Todos os direitos reservados.

# Projeto-Saude-em-dia-
O Medcontrol é um aplicativo desenvolvido com o objetivo de ajudar os usuários a organizar medicamentos, horários, consultas e tratamentos, reduzindo o risco de esquecimentos ou de uso fora do horário recomendado.

# Equipe

| RA | Integrante | GitHub |
| :--- | :--- | :--- |
| `3024104773` | Amanda Dias Barreto | [@amandaadb](https://github.com/amandaadb) |
| `3024100161` | Daniela Rosa | [@Mrsdanielar](https://github.com/Mrsdanielar) |
| `3024103168` | Gabriel Cruz Sanchez | [@gabrielcruzsz](https://github.com/gabrielcruzsz) |
| `3024105062` | Guilherme Alves Galeano | [@Guigalean006](https://github.com/Guigalean006) |
| `3024103605` | Luana Marcelino Andrade | [@Luana-Andrad](https://github.com/Luana-Andrad) |
| `3024107159` | Lucas Gomes Barboza | [@oLucasGBo](https://github.com/oLucasGBo) |
| `3024106574` | Renan Abeu Cerqueira de Lima | [@RenanAbreuC](https://github.com/RenanAbreuC) |

# Responsabilidades

### Gestão e Análise - *Amanda*
Responsável pelo planejamento e acompanhamento do projeto:
- Organização do cronograma e das entregas
- Acompanhamento das tarefas da equipe
- Levantamento de requisitos
- Definição de objetivos, público-alvo e regras de negócio

### UX/UI e Protótipo - *Amanda e Gabriel*
Responsáveis pela experiência e identidade visual do aplicativo:
- Criação da identidade visual (cores, fontes e componentes)
- Prototipação das telas
- Elaboração do fluxo de navegação
- Foco em usabilidade, com atenção especial ao público idoso

### Front-end — Telas e Medicamentos - *Daniela e Luana*
Responsáveis pelo desenvolvimento das interfaces do aplicativo:
- Telas de login, cadastro, dashboard, perfil e navegação principal
- Integração das telas com o sistema
- Cadastro de medicamentos, horários e tratamentos
- Registro de doses e tela de histórico

### Back-end e Banco de Dados - *Lucas e Renan*
Responsáveis pela estrutura de dados e lógica do sistema:
- Modelagem do banco de dados
- Criação de tabelas e entidades
- Implementação de CRUD
- Autenticação e regras de acesso
- Integração entre aplicativo e banco de dados

### Testes e Documentação - *Guilherme*
Responsável pela qualidade e documentação do projeto:
- Criação e execução de casos de teste
- Registro e acompanhamento de bugs
- Elaboração do README e da documentação técnica
- Apoio na criação dos diagramas UML

# Para quem este aplicativo é voltado?

O Medcontrol é um aplicativo voltado para o público geral, com foco na gestão da saúde e no acompanhamento de tratamentos contínuos. O nosso público-alvo principal inclui:

Pacientes em tratamento: Pessoas que fazem uso diário de medicamentos ou que possuem condições de saúde que exigem acompanhamento contínuo.

Familiares e cuidadores: Pessoas responsáveis por gerenciar, organizar e acompanhar a rotina de medicação de entes queridos ou pacientes sob seus cuidados.

# Tela inicial

Exemplo:

                                                            Bom dia, Maria!

                                                          Próximo medicamento

                                                         💊 Losartana 50 mg
                                                             1 comprimido
                                                             Hoje às 08:00

                                                             [ ✅ Tomei ]

                                                        [ ⏰ Lembrar depois ]

                                                           [ ❌ Não tomei ]

# Resumo do dia

                                                                 Hoje

                                                        ✅ 08:00 — Losartana
                                                        ✅ 14:00 — Dipirona
                                                        ⏰ 20:00 — Losartana

                                                     Medicamentos: 2 de 3 tomados

# Menu principal

Navegação:

                                        Início | Medicamentos | Histórico | Consultas | Perfil

                                                            🏠 Início
                                                         💊 Medicamentos
                                                           📊 Histórico
                                                           📅 Consultas
                                                            👤 Perfil

Manter o menu inferior sempre visível (Exemplo Duolingo, Instagram ou Clash Royale)

# Tela de histórico

                                                             Histórico

                                                           Segunda-feira

                                                  ✅ 08:00 — Losartana — Tomado
                                                  ✅ 20:00 — Losartana — Tomado

                                                            Terça-feira

                                                  ✅ 08:00 — Losartana — Tomado
                                                  ❌ 20:00 — Losartana — Não tomado
 
                                                            Quarta-feira
 
                                                  ✅ 08:00 — Losartana — Tomado
                                                  ⏰ 20:00 — Aguardando

# Controle de estoque

Cadastro de medicamento: assistente guiado passo a passo

                                                               Estoque

                                                         💊 Losartana 50 mg

                                                           Quantidade atual:

                                                            32 comprimidos

                                                               Consumo:

                                                              2 por dia

                                                               Previsão:

                                                               16 dias

                                      ⚠️ Seu medicamento pode acabar em aproximadamente 16 dias.

Podemos enviar uma notificação

                                                        [ Configurar alerta ]

# Consultas e receitas

                                                           Próxima consulta

                                                          📅 18 de setembro
                                                              🕐 14:30
                                                          🏥 Cardiologista

                                                             Lembrar-me:
                                                             1 dia antes
                                                             2 horas antes

                                                               Receita

                                                         💊 Losartana 50 mg
                                                      Renovação prevista: 25/09

# Funcionalidades extras

*Reconhecimento por voz:* o usuário pode dizer “Copilot, tomei meu remédio” e o app registra (Acho que é pago, peguei de exemplo o app da onde eu trabalho)

*Modo cuidador inteligente:* envia alertas automáticos se o paciente não confirmar a dose

*Integração com calendário médico (Google, Microsoft etc):* sincroniza consultas e exames no calendário pessoal do usuário

*Relatórios exportáveis:* PDF com adesão ao tratamento para levar ao médico (Algo mais simples mesmo, não precisa ser cheio de detalhes)

*Modo offline:* lembretes funcionam mesmo sem internet

# Acessibilidade

Botões grandes e ícones intuitivos (💊, ⏰, ✅)

Modo “alto contraste” e “texto ampliado” (Ou já deixar por padrão aplicado)

Tutorial inicial com voz explicando cada função

Feedback sonoro suave para confirmar ações

# Recompensas

Medalhas por adesão (“7 dias sem esquecer!”)

Ranking pessoal de consistência (Exemplo sequência do Duolingo)

Recompensas simbólicas (ex.: “Você está cuidando bem da sua saúde!”)

# Fluxo

                                                           ABRIR APP
                                                               ↓
                                                        LOGIN / CADASTRO
                                                               ↓
                                                       CONFIGURAR PERFIL
                                                               ↓
                                                     ADICIONAR MEDICAMENTO
                                                               ↓
                                                              Nome
                                                            Dosagem
                                                           Quantidade
                                                          Forma de uso
                                                            Horários
                                                               ↓
                                                             SALVAR
                                                               ↓
                                                   MEDCONTROL GERA OS HORÁRIOS
                                                               ↓
                                                           NOTIFICAÇÃO
                                                               ↓
                                                     "Hora do medicamento!"
                                                               ↓
                                      ┌──────────────┬──────────────────┬────────────────┐
                                      │   ✅ Tomei   │ ⏰ Lembrar depois │ ❌ Não tomei │
                                      └──────────────┴──────────────────┴────────────────┘
                                                               ↓
                                                           HISTÓRICO
                                                               ↓
                                                        ACOMPANHAMENTO

---

© 2026 MedControl. Todos os direitos reservados.

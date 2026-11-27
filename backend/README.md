# Back-end - MedControl

> API do MedControl, desenvolvida em **FastAPI**, com autenticação **JWT** e banco de dados **Supabase** (PostgreSQL).

Documentação relacionada: [Leia-me principal](../README.md) · [Front-end](../frontend/README.md) · [Diagramas](../docs/diagramas.md) · [Privacidade](../docs/privacidade.md) · [Segurança](../SECURITY.md) · [Contribuindo](../CONTRIBUTING.md)

---

## ✨ NOVIDADES (Outubro 2026)

Foram implementados **6 ajustes importantes**:

1. ✅ **Campo de limite de estoque** (`stock_limit`) - Customizável por medicamento
2. ✅ **Controle de notificações** (`notification_enabled`) - Habilitar/desabilitar alertas
3. ✅ **Desconto automático de estoque** - Quando registra dose (`fl_taken: true`)
4. ✅ **Desativação de rotinas** - Ao deletar medicamento, rotinas são desativadas
5. ✅ **Validação de números** - Campos numéricos não aceitam valores inválidos
6. ✅ **Documentação melhorada** - Código com comentários explicativos

📚 **Documentação completa:**
- [`ANALISE_BACKEND.md`](./ANALISE_BACKEND.md) - Análise técnica completa
- [`ENDPOINTS_ATUALIZADOS.md`](./ENDPOINTS_ATUALIZADOS.md) - Todos os endpoints
- [`MIGRATION_GUIDE.md`](./MIGRATION_GUIDE.md) - Passo a passo da migração do banco
- [`RESUMO_AJUSTES.md`](./RESUMO_AJUSTES.md) - Resumo visual dos ajustes
- [`TESTE_APIS.sh`](./TESTE_APIS.sh) - Script para testar todas as APIs

---

## Como rodar?

### Pré-requisitos

- Python 3 instalado;
- Um projeto no Supabase, com as tabelas criadas (veja a seção Banco de dados).

### Passo a passo

```bash
cd backend
python -m venv .venv
source .venv/bin/activate        # no Windows: .venv\Scripts\activate
pip install -r requirements.txt
# Crie .env com as variáveis da seção abaixo.
python main.py                   # ou: uvicorn main:app --reload
```

Rode sempre de dentro da pasta `backend/`, porque os arquivos se importam diretamente (`from config import settings`).

Com a API no ar, a documentação interativa (Swagger) fica em `http://localhost:8000/docs`.

## Variáveis de ambiente

Crie um arquivo `.env` na pasta `backend/`. **Nunca envie o `.env` ao repositório** (veja [IGNORE.md](../IGNORE.md)).

| Variável | Para que serve | Observação |
| :--- | :--- | :--- |
| `SUPABASE_URL` | Endereço do projeto no Supabase | Obrigatória |
| `SUPABASE_KEY` | Chave pública (anon) | Definida no `config.py` |
| `SUPABASE_SERVICE_KEY` | Chave de administrador | Obrigatória. **Segredo**: nunca no front-end |
| `SECRET_KEY` | Segredo usado para assinar o JWT | Obrigatória. Use um valor longo e aleatório |
| `ALGORITHM` | Algoritmo do JWT | Padrão `HS256` |
| `DEBUG` | Recarrega a API ao salvar arquivos | Padrão `True`. Use `False` fora do desenvolvimento |
| `HOST` | Endereço do servidor | Padrão `0.0.0.0` |
| `PORT` | Porta do servidor | Padrão `8000` |
| `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `GOOGLE_REDIRECT_URI` | Reservadas para login com Google e para a integração com o Google Agenda | **Ainda não usadas** por nenhuma rota |
| `REMINDERS_ENABLED` | Liga o agendador nesta instância da API | Padrão `False` |
| `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN` | Credenciais da conta Twilio | Necessárias se o agendador estiver ligado; token é segredo |
| `TWILIO_SMS_FROM` | Número Twilio habilitado para SMS, em E.164 | Necessário com o agendador ligado |
| `TWILIO_TRIAL_MODE` | Usa o modelo de SMS predefinido da conta de teste | Padrão `False`; use `True` na conta de teste |

Modelo para o `.env.example` (sem valores reais):

```text
SUPABASE_URL=
SUPABASE_KEY=
SUPABASE_SERVICE_KEY=
SECRET_KEY=
ALGORITHM=HS256
DEBUG=True
HOST=0.0.0.0
PORT=8000
REMINDERS_ENABLED=False
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_SMS_FROM=
TWILIO_TRIAL_MODE=False
```

## Estrutura

```text
backend/
├── main.py           cria a API e registra as rotas
├── config.py         lê as variáveis de ambiente
├── database.py       funções de acesso ao Supabase
├── models.py         modelos de entrada e saída (Pydantic)
├── routes/           auth, medicines, routines e history
├── tables.sql        script de criação das tabelas
├── migration_sms_reliability.sql  migração de retentativas e histórico
├── reminders.py      agendador e integração com Twilio
└── requirements.txt  dependências
```

## Endpoints

Todos os endpoints, exceto cadastro, login e as rotas `/` e `/health`, exigem o cabeçalho `Authorization: Bearer <token>`. Cada usuário acessa apenas os próprios dados.

### Autenticação (`/api/auth`)

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| POST | `/register` | Cria a conta e retorna o token |
| POST | `/login` | Faz login e retorna o token (validade de 7 dias) |
| GET | `/me` | Dados do usuário logado |
| PUT | `/me` | Atualiza os dados do usuário (senha opcional) |
| DELETE | `/delete-account` | Desativa a conta (exclusão lógica) |
| POST | `/logout` | Apenas informativo: não invalida o token |

### Medicamentos (`/api/medicines`)

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| GET | `` | Lista os medicamentos ativos |
| POST | `` | Cadastra (recusa nome e dosagem repetidos) |
| GET | `/{id}` | Busca um medicamento |
| PUT | `/{id}` | Atualiza um medicamento |
| DELETE | `/{id}` | Desativa o medicamento (exclusão lógica) |

### Rotinas, ou horários (`/api/routines`)

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| GET | `` | Lista as rotinas ativas |
| POST | `` | Cria a rotina de um medicamento (`medicine_id`, `time`, `days_of_week`) |
| GET | `/{id}` | Busca uma rotina |
| PUT | `/{id}` | Atualiza horário ou dias |
| DELETE | `/{id}` | Desativa a rotina (exclusão lógica) |

### Histórico (`/api/history`)

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| GET | `` | Lista o histórico do usuário, do mais recente ao mais antigo |
| POST | `` | Registra se a dose foi tomada (`routine_id`, `fl_taken`, `dt_hour` opcional) |
| GET | `/{id}` | Busca um registro |

### Preferências de lembretes (`/api/reminders`)

As três rotas exigem JWT. O número usado para lembretes é independente do telefone do cadastro.

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| GET | `/api/reminders` | Consulta a preferência; retorna `enabled: false` se não estiver cadastrada |
| PUT | `/api/reminders` | Ativa ou altera o número de SMS, exigindo novo consentimento |
| DELETE | `/api/reminders` | Desativa os lembretes |

Exemplo de corpo para o PUT (use somente um número de teste seu):

```json
{
  "channel": "sms",
  "phone": "+5511999999999",
  "consent": true
}
```

O canal aceito no PUT é somente `sms`; o telefone deve estar no formato internacional E.164. Para revogar, use DELETE, não `consent: false`. O consentimento deve ser solicitado separadamente do cadastro e específico para o número e canal informados. Preferências antigas de WhatsApp continuam visíveis no GET, mas não geram envios: para receber SMS, o usuário deve ativá-lo explicitamente com um novo PUT e consentimento.

Códigos de erro comuns: `400` (dado duplicado), `401` (token ausente, inválido ou expirado), `404` (item não encontrado) e `500` (erro ao gravar).

## Banco de dados

Pare a API antes de alterar o banco. Para um banco novo, execute `tables.sql` e depois `migration_sms_reliability.sql` no editor SQL do Supabase. Para um banco existente que já tenha as tabelas e funções de lembretes de `tables.sql`, execute apenas `migration_sms_reliability.sql`. Faça backup antes e aplique a migração **uma única vez**, antes de reiniciar a API com a nova versão. Se as tabelas de lembretes ainda não existirem em um banco existente, primeiro aplique somente a seção de lembretes de `tables.sql` (a partir de `CREATE TABLE public.reminder_preferences`), não o arquivo inteiro.

A migração adiciona o contador de tentativas, substitui as funções de reserva e cria `record_dose_history`. Sem ela, o registro de histórico e os lembretes da nova versão não funcionarão corretamente.

Regras do banco que o front-end também precisa respeitar:

- `medicines.quantity` precisa ser maior que zero, e `medicines.stock` não pode ser negativo;
- `users.email` é único;
- As exclusões feitas pela API são **lógicas** (`fl_active = false`). Nenhuma linha é apagada;
- O banco **não guarda "pendente"**: a dose pendente é calculada no app, a partir das rotinas e do histórico.

## Lembretes por SMS com Twilio

1. Confirme que as tabelas e funções de lembretes existem no Supabase e instale as dependências.
2. Na Twilio, obtenha um número remetente habilitado para SMS e para o país de destino. Configure `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_SMS_FROM` e `REMINDERS_ENABLED=True` no `.env`. Use `TWILIO_TRIAL_MODE=True` para a conta de teste.
3. Reinicie a API e ative o SMS por `PUT /api/reminders`, com consentimento explícito. A API falha ao iniciar se o agendador estiver ligado e faltar alguma das três configurações Twilio.
4. Cadastre uma rotina para o minuto seguinte em horário de Brasília e acompanhe os logs. Para estoque, use `stock <= stock_limit` e `notification_enabled=true`. O alerta de estoque é reservado uma vez enquanto estiver baixo; só é rearmado quando o estoque passa **acima** do limite, inclusive após alteração do limite.

Os textos genéricos de dose e estoque ficam no dicionário `TEXTS` em `reminders.py` e podem ser editados pela equipe. Não inclua nomes de medicamentos ou outros dados de saúde. Com `TWILIO_TRIAL_MODE=True`, a API envia o modelo predefinido `sms_appointment_reminders` nos dois tipos de alerta; a mensagem recebida é a do provedor. Para enviar os textos próprios, atualize a conta se necessário e use `TWILIO_TRIAL_MODE=False`; podem existir custos e outras exigências do provedor.

O agendador verifica na inicialização e a cada minuto com o fuso `America/Sao_Paulo`; os segundos da rotina são ignorados. Ele procura doses vencidas há até 15 minutos, inclusive do dia anterior; doses mais antigas não são enviadas. Em `days_of_week`, use `Todos` ou `seg,ter,qua,qui,sex,sab,dom` (apenas os dias desejados). Valores antigos fora desse formato são ignorados com erro nos logs e devem ser corrigidos. Para doses, a rotina, o medicamento e a conta devem estar ativos; para estoque também é respeitado `notification_enabled`, que controla apenas o alerta de estoque. Falhas de banco de um usuário são registradas e não interrompem os demais.

Uma reserva no banco evita que duas instâncias enviem a mesma ocorrência. Os registros em `reminder_attempts` têm `attempt_count` e os estados `claimed` (reservada), `accepted` (Twilio aceitou, não significa entregue), `failed` (Twilio recusou), `unknown` (erro de comunicação, HTTP 408, 409 ou 5xx) e `cancelled` (preferência mudou).

Uma recusa confirmada é repetida até **três vezes**, com intervalo mínimo de cinco minutos, além da tentativa inicial. As doses só são repetidas dentro da janela de 15 minutos; assim, podem ter menos de três retentativas. Cancelamentos podem ser reavaliados se a preferência for ativada novamente. Quando o limite de tentativas de estoque é atingido, esse alerta só é rearmado quando o estoque ultrapassa o limite. `unknown` e `claimed` não são repetidos automaticamente, pois podem já ter sido enviados; investigue antes de qualquer reenvio.

**Limitações importantes:** a API precisa ficar ligada para enviar; doses com mais de 15 minutos de atraso não são recuperadas. Processamento lento ou falhas prolongadas também podem ultrapassar essa janela. A verificação de consentimento acontece imediatamente antes do envio, mas não consegue cancelar uma chamada que já iniciou. Não há webhook para acompanhar entrega ou processar respostas de cancelamento. Para uso real, configure monitoramento e um agendador/processador persistente, avalie privacidade e custos e atualize a política de privacidade antes de ativar o serviço. O front-end ainda não está integrado.

Referências: [SMS de teste na Twilio](https://www.twilio.com/docs/usage/trials/try-out-sms) · [Política de privacidade](../docs/privacidade.md).

Para executar os testes locais, de dentro de `backend/`: `python -m unittest discover -s tests -v`. Eles usam simulações e não enviam mensagens reais.

## Pendências conhecidas

- Registros repetidos de uma mesma dose ainda podem descontar estoque mais de uma vez.
- A documentação principal e a política de privacidade ainda precisam ser revisadas pela equipe antes do uso real dos novos lembretes.

Questões de segurança devem ser tratadas pelo canal privado descrito em [SECURITY.md](../SECURITY.md).

---

> O MedControl é uma ferramenta de organização e **não substitui orientação médica**.

---

© 2026 MedControl. Todos os direitos reservados.

# Back-end - MedControl

> API do MedControl, desenvolvida em **FastAPI**, com autenticação **JWT** e banco de dados **Supabase** (PostgreSQL).

Documentação relacionada: [Leia-me principal](../README.md) · [Front-end](../frontend/README.md) · [Diagramas](../docs/diagramas.md) · [Privacidade](../docs/privacidade.md) · [Segurança](../SECURITY.md) · [Contribuindo](../CONTRIBUTING.md)

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
cp .env.example .env             # depois preencha os valores
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
| `WHATSAPP_TOKEN` | Chave de acesso do provedor de WhatsApp | **Planejada.** Segredo: nunca no front-end |
| `WHATSAPP_PHONE_ID` | Identificador do número remetente | **Planejada** |
| `WHATSAPP_VERIFY_TOKEN` | Valida o webhook do provedor | **Planejada**, se houver webhook |

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

Códigos de erro comuns: `400` (dado duplicado), `401` (token ausente, inválido ou expirado), `404` (item não encontrado) e `500` (erro ao gravar).

## Banco de dados

O script `tables.sql` cria quatro tabelas: `users`, `medicines`, `routines` e `history`. O modelo completo está em [docs/diagramas.md](../docs/diagramas.md). Para criar o banco, execute o script no editor SQL do Supabase.

Regras do banco que o front-end também precisa respeitar:

- `medicines.quantity` precisa ser maior que zero, e `medicines.stock` não pode ser negativo;
- `users.email` é único;
- As exclusões feitas pela API são **lógicas** (`fl_active = false`). Nenhuma linha é apagada;
- O banco **não guarda "pendente"**: a dose pendente é calculada no app, a partir das rotinas e do histórico.

## Lembretes (planejado)

Os lembretes de dose serão enviados por **WhatsApp**, a partir do servidor. **Nada disto existe ainda** no código nem em `tables.sql`.

O que será necessário:

- **Banco:** campos para número de WhatsApp, indicação de que a pessoa consentiu com os lembretes, data do consentimento e canal escolhido. Hoje a tabela `users` não os tem. Qualquer mudança deve ser refletida em `models.py`, `frontend/src/types/api.ts` e `docs/diagramas.md`;
- **Endpoints:** ativar e desativar os lembretes e consultar as preferências;
- **Agendador:** uma rotina que verifica, a cada minuto, as rotinas que vencem e dispara os envios. Hoje não há nenhuma tarefa agendada;
- **Provedor de WhatsApp:** escolha, conta e custo **[CONFIRMAR]**. Mensagens iniciadas pela empresa costumam exigir modelos de mensagem aprovados e consentimento prévio;
- **Conteúdo:** texto genérico, sem nome de medicamento nem dado de saúde (veja [docs/privacidade.md](../docs/privacidade.md)).

Depois, em etapas separadas: notificações do celular (tratadas no app) e integração com o Google Agenda (usa as variáveis `GOOGLE_*`).

## Pendências conhecidas

- A exclusão de um medicamento não desativa as rotinas dele;
- O banco não tem campo de limite de estoque (sugestão: `stock_alert` em `medicines`);
- O formato dos valores de `days_of_week` ainda não foi definido (hoje só existe `Todos`);
- Não há testes automatizados.
- Os lembretes por WhatsApp não existem: faltam campos no banco, endpoints, agendador e provedor;

Questões de segurança devem ser tratadas pelo canal privado descrito em [SECURITY.md](../SECURITY.md).

---

> O MedControl é uma ferramenta de organização e **não substitui orientação médica**.

---

© 2026 MedControl. Todos os direitos reservados.

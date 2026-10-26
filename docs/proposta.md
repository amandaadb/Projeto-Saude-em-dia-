# Proposta - MedControl

> Resumo do problema que o MedControl resolve, da solução proposta, do escopo do MVP e da situação de cada funcionalidade.

## Problema

Pessoas em tratamento contínuo, principalmente idosos e pacientes com várias medicações, esquecem horários, tomam doses em duplicidade ou deixam o estoque acabar. Cuidadores têm dificuldade de acompanhar essa rotina.

**Validação:** **[PREENCHER: como o problema foi validado]**

## Solução

Aplicativo que organiza medicamentos e horários, mostra a cada dia o que precisa ser tomado e registra o histórico de doses, reduzindo esquecimentos e uso fora do horário. Os lembretes por notificação são o próximo passo.

## Escopo do MVP

| # | Funcionalidade |
| :--- | :--- |
| 1 | Cadastro e login |
| 2 | Gestão de medicamentos e horários |
| 3 | Doses do dia e registro de dose (tomei ou não tomei) |
| 4 | Histórico de doses |
| 5 | Controle de estoque com selo de estoque baixo |
| 6 | Perfil com dados de saúde e contato de emergência |

> **Fora do MVP:** consultas e receitas, recompensas, modo cuidador e lembretes por notificação.

## Situação das funcionalidades

Em 25/10/2026. O app funciona com dados de teste; a integração com a API é a próxima etapa.

| Funcionalidade | Back-end | Front-end | Integrado |
| :--- | :--- | :--- | :--- |
| Cadastro e login | Pronto | Tela de login **[CONFIRMAR]** | Não |
| Medicamentos e horários | Pronto | Pronto (dados de teste) | Não |
| Doses do dia e registro | Pronto | Pronto (dados de teste) | Não |
| Histórico | Pronto | Pronto (dados de teste) | Não |
| Estoque | Campo no banco | Ajuste manual e selo (limite fixo de 5) | Não |
| Perfil e dados de saúde | Pronto | Pronto (dados de teste) | Não |
| Lembretes por notificação | Não | Não | Não |
| Desconto automático de estoque | Não | Não | Não |

## Requisitos

### Funcionais

- Criar conta, fazer login e permanecer logado;
- Cadastrar, editar e excluir medicamentos, com dose, quantidade, estoque e horários;
- Ver as doses do dia, com status **pendente**, **tomada** ou **não tomada**;
- Registrar uma dose como **tomada** ou **não tomada**;
- Consultar o histórico de doses, com filtro;
- Ajustar o estoque e ver um selo quando ele estiver baixo;
- Editar o perfil, os dados de saúde e o contato de emergência;
- Excluir a conta.

Regras de negócio:

- A dose é **pendente** quando não há registro dela no dia; o back-end não guarda esse estado, o app o calcula;
- Uma dose já registrada não pode ser registrada de novo no app;
- Não pode haver dois medicamentos com o mesmo nome e a mesma dosagem;
- O estoque nunca fica negativo.

### Planejados (fora da versão atual)

- Receber aviso no horário de cada dose;
- Adiar uma dose;
- Descontar o estoque ao registrar a dose e avisar por notificação.

### Não funcionais

- Interface acessível, pensando em idosos (veja [ACCESSIBILITY.md](../ACCESSIBILITY.md));
- Acesso restrito aos dados do próprio usuário;
- Tratamento cuidadoso dos dados de saúde (veja [privacidade.md](./privacidade.md));
- Aviso de que o app **não substitui orientação médica**.

> O MedControl é uma ferramenta de organização e **não substitui orientação médica**.

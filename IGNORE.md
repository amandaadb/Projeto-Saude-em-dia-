# Arquivos Ignorados - MedControl

> Lista dos arquivos e pastas que não devem ser versionados no Git, com o motivo de cada grupo.

## Como usar?

O repositório tem **três** arquivos `.gitignore`, cada um com um papel:

| Arquivo | Papel |
| :--- | :--- |
| `.gitignore` (raiz) | Regras gerais: segredos, Python, Node, editores e sistema operacional. O bloco abaixo é a cópia de referência |
| `backend/.gitignore` | Regras do back-end (`.env`, `__pycache__`, ambientes virtuais) |
| `frontend/.gitignore` | Regras do front-end (Expo, `node_modules`, `/ios` e `/android` gerados, `.env*.local`) |

Para o Git aplicar as regras da raiz, copie o conteúdo do bloco abaixo para um arquivo chamado `.gitignore` na raiz do repositório. Este documento serve como referência para a equipe.

Ao alterar um dos três arquivos, confira se a lista de segredos continua igual nos três (`.env`, `*.pem`, `*.key`, `*.jks`, `*.p8`, `*.p12` e `*.mobileprovision`).

Antes do primeiro commit de qualquer arquivo novo de configuração, rode `git status` e confira se nenhum `.env` aparece na lista.

## O que é ignorado e por quê?

| Grupo | Motivo |
| :--- | :--- |
| Variáveis de ambiente (`.env`, `.env.*`) | Contêm chaves do Supabase, segredo do JWT e senhas. O modelo `.env.example` **é versionado**, sem valores reais |
| Certificados e chaves (`*.pem`, `*.key`, `*.jks`, `*.p8`, `*.p12`) | Dão acesso a contas e assinatura do aplicativo |
| Ambientes virtuais e dependências | São gerados localmente e ocupam muito espaço |
| Caches e arquivos compilados | São gerados automaticamente |
| Pastas nativas geradas (`/ios`, `/android`) | O Expo as recria; não são editadas à mão |
| Configurações de editor | São pessoais de cada integrante |
| Arquivos do sistema operacional | Não fazem parte do projeto |
| Logs e builds | São gerados durante execução e publicação |

> **Nunca** envie o `.env` para o repositório. Se isso acontecer, troque imediatamente as chaves do Supabase e o segredo do JWT: remover o arquivo depois não apaga o conteúdo do histórico do Git.

> **Atenção:** o `frontend/.gitignore` tem uma linha solta escrita `example`. Se não for intencional, remova.

```gitignore
# ===== Segredos e variáveis de ambiente =====
.env
.env.*
!.env.example
*.pem
*.key
secrets/

# ===== Python / FastAPI =====
__pycache__/
*.py[cod]
*.pyo
*.pyd
.venv/
venv/
env/
ENV/
*.egg-info/
.pytest_cache/
.mypy_cache/
.ruff_cache/
.coverage
htmlcov/
.python-version

# ===== Supabase =====
supabase/.temp/
supabase/.branches/
.supabase/

# ===== Node / Front-end =====
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
.expo/
.expo-shared/
.next/
dist/
build/
web-build/
.cache/
.parcel-cache/
*.tsbuildinfo

# ===== Mobile (Android / iOS) =====
android/app/build/
android/.gradle/
android/local.properties
ios/Pods/
ios/build/
*.apk
*.aab
*.ipa
*.jks
*.keystore

# ===== Logs e temporários =====
*.log
logs/
tmp/
temp/
*.tmp

# ===== Editores e IDEs =====
.vscode/
.idea/
*.swp
*.swo

# ===== Sistema operacional =====
.DS_Store
Thumbs.db
desktop.ini

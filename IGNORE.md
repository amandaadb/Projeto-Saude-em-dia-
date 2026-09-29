# Arquivos Ignorados - MedControl

> Lista dos arquivos e pastas que não devem ser versionados no Git, com o motivo de cada grupo.

## Como Usar

Para o Git aplicar essas regras, copie o conteúdo do bloco abaixo para um arquivo chamado `.gitignore` na raiz do repositório. Este documento serve como referência para a equipe.

## O Que é Ignorado e Por Quê

| Grupo | Motivo |
| :--- | :--- |
| Variáveis de ambiente (`.env`) | Contêm chaves do Supabase, segredo do JWT e senhas |
| Ambientes virtuais e dependências | São gerados localmente e ocupam muito espaço |
| Caches e arquivos compilados | São gerados automaticamente |
| Configurações de editor | São pessoais de cada integrante |
| Arquivos do sistema operacional | Não fazem parte do projeto |
| Logs e builds | São gerados durante execução e publicação |

> **Nunca** envie o `.env` para o repositório. Se isso acontecer, troque imediatamente as chaves do Supabase e o segredo do JWT.

## Conteúdo do `.gitignore`

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
```

---

© 2026 MedControl. Todos os direitos reservados.

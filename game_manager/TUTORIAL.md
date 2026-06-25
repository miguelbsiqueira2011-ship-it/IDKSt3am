# 📘 TUTORIAL DE INSTALAÇÃO E USO - GAME MANAGER

## 📋 Índice

1. [Pré-requisitos](#pré-requisitos)
2. [Instalação Passo a Passo](#instalação-passo-a-passo)
3. [Configuração das Ferramentas](#configuração-das-ferramentas)
4. [Primeiro Uso](#primeiro-uso)
5. [Funcionalidades Principais](#funcionalidades-principais)
6. [Solução de Problemas](#solução-de-problemas)

---

## 🔧 Pré-requisitos

### Sistema Operacional
- ✅ Windows 10/11
- ✅ macOS 10.15+
- ✅ Linux (Ubuntu, Fedora, Arch, etc.)

### Software Necessário
- **Python 3.8 ou superior**
  - Verificar: `python --version`
  - Download: https://www.python.org/downloads/

### Ferramentas Requeridas (Instaladas no PC)

#### 1. Steam Client
O Steam deve estar instalado para gerenciamento da biblioteca.

**Verificar instalação:**
```bash
# Windows
tasklist | findstr steam.exe

# Linux
pgrep -x steam

# macOS
pgrep -x Steam
```

**Se NÃO estiver instalado:**

1. Acesse: https://store.steampowered.com/about/
2. Clique em "Instalar Steam"
3. Execute o instalador baixado
4. Siga o assistente de instalação
5. Faça login na sua conta

#### 2. Lua Runtime
Lua é necessário para execução de scripts e automações.

**Verificar instalação:**
```bash
lua -v
```

**Se NÃO estiver instalado:**

**Windows:**
```powershell
# Opção 1: Usando winget (recomendado)
winget install -e --id Lua.Lua.5.4

# Opção 2: Manual
# 1. Acesse: https://www.lua.org/download.html
# 2. Baixe o instalador para Windows
# 3. Execute e siga as instruções
```

**macOS:**
```bash
# Usando Homebrew
brew install lua

# Se não tiver Homebrew, instale primeiro:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install lua5.4

# Fedora
sudo dnf install lua

# Arch Linux
sudo pacman -S lua
```

---

## 📦 Instalação Passo a Passo

### Passo 1: Baixar o Projeto

```bash
# Clone o repositório ou baixe o arquivo ZIP
git clone <URL_DO_REPOSITORIO>
cd game_manager
```

### Passo 2: Instalar Dependências Python

```bash
# Instale todas as dependências necessárias
pip install -r requirements.txt
```

**Ou instale manualmente:**
```bash
pip install customtkinter
pip install Pillow
pip install requests
pip install psutil
```

### Passo 3: Verificar Instalação

```bash
# Execute o script de verificação
./start.sh  # Linux/macOS

# Ou no Windows (PowerShell):
.\start.ps1
```

### Passo 4: Executar a Aplicação

```bash
# Método 1: Usando o script
python main.py

# Método 2: Diretamente
python backend/main.py
```

---

## ⚙️ Configuração das Ferramentas

### Verificando Status das Ferramentas

Ao iniciar a aplicação:

1. Clique no botão **⚙️ Configurações** (canto superior direito)
2. Vá para a aba **"Ferramentas"**
3. Visualize o status de cada ferramenta:
   - ✓ Instalado (verde)
   - ✗ Não instalado (vermelho)

### Instalando Ferramentas pela Interface

Se alguma ferramenta não estiver instalada:

1. Na aba **Ferramentas**, localize a ferramenta
2. Clique no botão **"Instalar"**
3. Siga as instruções:
   - **Steam**: A página de download será aberta
   - **Lua**: Instalação automática (quando possível) ou manual

### Pós-Instalação

Após instalar as ferramentas:

1. Reinicie a aplicação Game Manager
2. Verifique novamente o status na aba Ferramentas
3. Os indicadores devem mostrar "✓ Instalado"

---

## 🎮 Primeiro Uso

### Tela Inicial

Ao abrir o Game Manager, você verá:

```
┌─────────────────────────────────────┐
│  Game Manager                    ⚙️ │
├─────────────────────────────────────┤
│                                     │
│     Qual jogo deseja adicionar?     │
│                                     │
│  🔍 [Pesquisar jogo...]             │
│                                     │
│  [      Selecionar Jogo      ]      │
│                                     │
├─────────────────────────────────────┤
│  Steam        ● Online              │
│  Integração 1 ● Online              │
│  Integração 2 ● Online              │
│                        📜 Histórico │
└─────────────────────────────────────┘
```

### Adicionando seu Primeiro Jogo

#### Passo 1: Pesquisar
1. Digite o nome do jogo no campo de pesquisa
2. Pressione **Enter** ou clique em **"Selecionar Jogo"**

#### Passo 2: Selecionar
1. Os resultados aparecerão abaixo
2. Clique no card do jogo desejado
3. O card ficará destacado (borda azul)

#### Passo 3: Confirmar
1. As informações do jogo serão exibidas
2. Verifique se é o jogo correto
3. Clique em **"Adicionar à Biblioteca"**

#### Passo 4: Aguardar Processamento
```
Processando...
[████████████░░░░░░░░] 70%
Adicionando ao Steam shortcuts...
```

#### Passo 5: Conclusão
```
         ✓
Operação concluída com sucesso.

[ Reiniciar Steam ]  [ Fazer Depois ]
```

**Recomendação:** Clique em **"Reiniciar Steam"** para garantir que a biblioteca seja atualizada corretamente.

---

## 🎯 Funcionalidades Principais

### 1. Pesquisa de Jogos
- Busca em tempo real
- Resultados com capa, nome e gêneros
- Rating visível (estrelas)

### 2. Seleção Visual
- Cards interativos
- Feedback visual ao selecionar
- Informações detalhadas

### 3. Progresso em Tempo Real
- Barra de progresso animada
- Mensagens de status
- Tempo estimado

### 4. Painel de Status
- Monitoramento contínuo
- Indicadores online/offline
- Atualização automática

### 5. Histórico de Operações
- Clique em **📜 Histórico**
- Últimas 10 operações
- Status (✓ ou ✗)
- Data e hora

### 6. Configurações

#### Aba Preferências
- Iniciar com o sistema
- Configurações gerais

#### Aba Ferramentas
- Status de Steam e Lua
- Botões de instalação
- Informações detalhadas

#### Aba Logs
- Diagnóstico do sistema
- Logs de operação
- Informações de debug

---

## 🐛 Solução de Problemas

### Problema: Steam não detectado

**Sintoma:** Indicador mostra "Offline" ou "Não instalado"

**Soluções:**

1. **Verifique se o Steam está instalado:**
   - Windows: `C:\Program Files (x86)\Steam\steam.exe`
   - macOS: `/Applications/Steam.app`
   - Linux: `~/.steam/steam`

2. **Execute como administrador** (Windows):
   - Clique direito no Game Manager
   - "Executar como administrador"

3. **Reinicie o Steam** antes de usar o Game Manager

### Problema: Lua não detectado

**Sintoma:** Mensagem "Lua not installed"

**Soluções:**

1. **Instale Lua:**
   ```bash
   # Windows (winget)
   winget install -e --id Lua.Lua.5.4
   
   # macOS
   brew install lua
   
   # Linux
   sudo apt-get install lua5.4
   ```

2. **Adicione ao PATH** (se necessário):
   - Windows: Adicione `C:\Program Files\Lua\5.4\` ao PATH
   - Reinicie o terminal após alterar o PATH

3. **Verifique a instalação:**
   ```bash
   lua -v
   ```

### Problema: Erro ao adicionar jogo

**Sintoma:** Mensagem de erro durante o processamento

**Soluções:**

1. **Verifique as integrações:**
   - Abra Configurações → Ferramentas
   - Certifique-se de que todas estão "Online"

2. **Reinicie a aplicação**

3. **Tente novamente**

### Problema: Interface não abre

**Sintoma:** Erro do tkinter ou tela preta

**Soluções:**

1. **Instale o tkinter:**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install python3-tk
   
   # Fedora
   sudo dnf install python3-tkinter
   
   # macOS (já vem com Python)
   
   # Windows (já vem com Python)
   ```

2. **Reinstale as dependências:**
   ```bash
   pip uninstall customtkinter
   pip install customtkinter
   ```

### Problema: Dependências faltando

**Sintoma:** Erros de importação

**Solução:**
```bash
# Reinstale todas as dependências
pip install -r requirements.txt --force-reinstall
```

---

## 📞 Suporte Adicional

### Logs de Diagnóstico

Para obter logs detalhados:

1. Abra **Configurações** → **Logs**
2. Copie o conteúdo
3. Inclua ao reportar problemas

### Reportando Problemas

Ao reportar um problema, inclua:

1. Sistema operacional e versão
2. Versão do Python (`python --version`)
3. Status das ferramentas (aba Ferramentas)
4. Logs da aplicação
5. Passos para reproduzir o erro

---

## ✅ Checklist de Instalação

Use esta checklist para garantir que tudo está configurado:

- [ ] Python 3.8+ instalado
- [ ] Dependências Python instaladas
- [ ] Steam instalado e funcionando
- [ ] Lua instalado e no PATH
- [ ] Game Manager inicia sem erros
- [ ] Todas as integrações mostram "Online"
- [ ] Consegue pesquisar jogos
- [ ] Consegue adicionar um jogo à biblioteca

---

**Parabéns!** 🎉

Você completou a configuração do Game Manager. Agora você pode gerenciar sua biblioteca de jogos de forma moderna e eficiente!

Para mais informações, consulte o README.md ou abra uma issue no repositório.

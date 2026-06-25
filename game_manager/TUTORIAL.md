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

#### 2. Lua Tools
Lua Tools é necessário para execução de scripts e automações.

**Verificar instalação:**
```bash
lua -v
```

**Se NÃO estiver instalado:**

**Windows (PowerShell como Administrador):**
```powershell
# ⚠️ IMPORTANTE: Abra o PowerShell COMO ADMINISTRADOR
# Clique direito no ícone do PowerShell → Executar como Administrador
# Depois execute este comando:

irm "https://ps.lua.tools/install-plugin-legacy.ps1" | iex
```

> ⚠️ **Importante:** O PowerShell DEVE ser executado como Administrador. Se não tiver permissões administrativas, a instalação falhará.

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

### Passo 3: Executar a Aplicação

**Windows (Método Recomendado - SEM CMD VISÍVEL):**
- Basta clicar **duas vezes** no arquivo `run.bat`
- A aplicação abrirá sem mostrar a janela do CMD
- Se ocorrer algum erro, o CMD aparecerá automaticamente para mostrar a mensagem de erro

**Windows (Alternativo via CMD/PowerShell):**
```bash
python main.py
```

**Linux/macOS:**
```bash
python main.py
```

---

## ⚙️ Configuração das Ferramentas

### Verificação Automática ao Iniciar

Ao iniciar o Game Manager pela primeira vez:

1. O sistema **verifica automaticamente** se Steam e Lua estão instalados
2. Se alguma ferramenta estiver faltando, uma janela aparecerá IMEDIATAMENTE:

```
┌─────────────────────────────────────┐
│   ⚠️ Ferramentas Necessárias        │
├─────────────────────────────────────┤
│ As seguintes ferramentas precisam  │
│ ser instaladas:                     │
│                                     │
│ ✗ Steam                             │
│   Steam client for game management  │
│                    [ Instalar ]     │
│                                     │
│ ✗ Lua Tools                         │
│   Lua runtime for script execution  │
│                    [ Instalar ]     │
│                                     │
│     [ Continuar Mesmo Assim ]       │
└─────────────────────────────────────┘
```

3. Clique em **"Instalar"** para cada ferramenta necessária
4. Uma barra de progresso mostrará o status da instalação
5. **IMPORTANTE:** Você DEVE instalar as ferramentas antes de usar o programa!

### Instalando Ferramentas pela Interface

Se precisar instalar ferramentas após o início:

1. Clique no botão **⚙️ Configurações** (canto superior direito)
2. Vá para a aba **"Ferramentas"**
3. Visualize o status de cada ferramenta:
   - ✓ Instalado (verde)
   - ✗ Não instalado (vermelho)
4. Clique em **"Instalar"** para instalar a ferramenta faltante

### Processo de Instalação

**Para Steam:**
- A página oficial de download será aberta no navegador
- Siga o assistente de instalação do site
- Após instalar, reinicie o Game Manager

**Para Lua Tools (Windows):**
- O instalador PowerShell será executado automaticamente
- Comando usado: `irm "https://ps.lua.tools/install-plugin-legacy.ps1" | iex`
- Aguarde a conclusão (pode levar alguns segundos)
- Mensagem de sucesso aparecerá
- **Nota:** Se a instalação automática falhar, você será redirecionado para a página de download manual

**Para Lua (macOS/Linux):**
- Tentativa de instalação automática via gerenciador de pacotes
- Se falhar, instruções manuais serão fornecidas

### Pós-Instalação

Após instalar as ferramentas:

1. **Reinicie a aplicação** Game Manager
2. Verifique novamente o status na aba Ferramentas
3. Os indicadores devem mostrar "✓ Instalado"
4. Todas as integrações devem estar "Online"

---

## 🎮 Primeiro Uso

### Tela Inicial

Ao abrir o Game Manager (via `run.bat` no Windows), você verá:

```
┌─────────────────────────────────────┐
│  Game Manager                    ⚙️ │
├─────────────────────────────────────┤
│                                     │
│     Qual jogo deseja adicionar?     │
│                                     │
│  🔍 [Filtrar jogos...]              │
│                                     │
│  ┌───────────────────────────────┐  │
│  │ 🎮 Baldur's Gate 3            │  │
│  │    RPG • Strategy  ★ 96       │  │
│  │                  [Adicionar]  │  │
│  ├───────────────────────────────┤  │
│  │ 🎮 Battlefield 2042           │  │
│  │    FPS • Action  ★ 78         │  │
│  │                  [Adicionar]  │  │
│  ├───────────────────────────────┤  │
│  │ 🎮 Counter-Strike 2           │  │
│  │    FPS • Competitive  ★ 92    │  │
│  │                  [Adicionar]  │  │
│  └───────────────────────────────┘  │
│                                     │
├─────────────────────────────────────┤
│  Steam        ● Online              │
│  Lua Tools    ● Online              │
│                        📜 Histórico │
└─────────────────────────────────────┘
```

### Adicionando seu Primeiro Jogo

#### Método Rápido (RECOMENDADO)

1. **Todos os jogos já aparecem listados** na tela inicial
2. Cada card tem um botão **"Adicionar"** no canto inferior direito
3. Basta **clicar em "Adicionar"** no jogo que você deseja
4. Pronto! O processo começará imediatamente

#### Passo a Passo Detalhado

**Passo 1: Escolher o Jogo**
- Role a lista de jogos (todos em ordem alfabética)
- Use o filtro "Filtrar jogos..." se quiser buscar rapidamente
- Clique no botão **"Adicionar"** do jogo desejado

**Passo 2: Aguardar Processamento**
```
Processando...
[████████████░░░░░░░░] 70%
Adicionando ao Steam shortcuts...
```

**Passo 3: Conclusão**
```
         ✓
Operação concluída com sucesso.

[ Reiniciar Steam ]  [ Fazer Depois ]
```

**Recomendação:** Clique em **"Reiniciar Steam"** para garantir que a biblioteca seja atualizada corretamente.

### Lista Completa de Jogos Disponíveis

A aplicação já inclui **21 jogos populares** prontos para seleção:

- Baldur's Gate 3
- Battlefield 2042
- Call of Duty: Modern Warfare II
- Counter-Strike 2
- Cyberpunk 2077
- Destiny 2
- Elden Ring
- FIFA 23
- Forza Horizon 5
- God of War
- Grand Theft Auto V
- Hogwarts Legacy
- Left 4 Dead 2
- Minecraft
- Red Dead Redemption 2
- Resident Evil 4
- Rocket League
- Spider-Man Remastered
- Starfield
- The Witcher 3: Wild Hunt
- Valorant

> 💡 **Dica:** Não é necessário digitar o nome do jogo! Cada card já tem seu próprio botão "Adicionar". Use o filtro apenas se desejar buscar um jogo específico rapidamente.

---

## 🎯 Funcionalidades Principais

### 1. Lista de Jogos com Botão Direto
- Todos os jogos visíveis imediatamente
- Botão "Adicionar" em cada card
- Layout horizontal moderno
- Informações completas (nome, gêneros, rating)

### 2. Filtro de Busca
- Digite para filtrar a lista em tempo real
- Resultados atualizados instantaneamente

### 3. Progresso em Tempo Real
- Barra de progresso animada
- Mensagens de status detalhadas
- Feedback visual constante

### 4. Painel de Status
- Monitoramento contínuo das integrações
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

### Problema: Janela abre e fecha imediatamente

**Sintoma:** Ao clicar no run.bat, a janela pisca e some

**Soluções:**

1. **Execute manualmente para ver o erro:**
   ```cmd
   python main.py
   ```

2. **Verifique se Python está instalado:**
   ```cmd
   python --version
   ```

3. **Instale as dependências:**
   ```cmd
   pip install -r requirements.txt
   ```

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

**Sintoma:** Mensagem "Lua not installed" ou indicador vermelho

**Soluções:**

1. **Instale Lua Tools (Windows):**
   ```powershell
   # ⚠️ ABRA O POWERSHELL COMO ADMINISTRADOR!
   # Clique direito → Executar como Administrador
   
   # Execute o comando oficial:
   irm "https://ps.lua.tools/install-plugin-legacy.ps1" | iex
   ```

2. **Instale Lua (macOS/Linux):**
   ```bash
   # macOS
   brew install lua
   
   # Linux (Ubuntu/Debian)
   sudo apt-get install lua5.4
   
   # Linux (Fedora)
   sudo dnf install lua
   ```

3. **Adicione ao PATH** (se necessário):
   - Windows: Adicione `C:\Program Files\Lua\5.4\` ao PATH do sistema
   - Reinicie o terminal/aplicação após alterar o PATH

4. **Verifique a instalação:**
   ```bash
   lua -v
   ```
   Deve mostrar algo como: `Lua 5.4.x  Copyright (C) ...`

### Problema: Erro ao adicionar jogo

**Sintoma:** Mensagem de erro durante o processamento

**Soluções:**

1. **Verifique as integrações:**
   - Abra Configurações → Ferramentas
   - Certifique-se de que todas estão "Online"

2. **Reinicie a aplicação**

3. **Tente novamente**

### Problema: Interface não abre / Erro do tkinter

**Sintoma:** Erro sobre tkinter ou tela preta

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
- [ ] Dependências Python instaladas (`pip install -r requirements.txt`)
- [ ] Steam instalado e funcionando
- [ ] Lua instalado e no PATH
- [ ] Game Manager inicia sem erros (clique duplo em run.bat)
- [ ] Todas as integrações mostram "Online"
- [ ] Consegue ver a lista de jogos
- [ ] Consegue adicionar um jogo à biblioteca

---

**Parabéns!** 🎉

Você completou a configuração do Game Manager. Agora você pode gerenciar sua biblioteca de jogos de forma moderna e eficiente!

**Resumo rápido:**
1. Clique duas vezes em `run.bat` (Windows) ou execute `python main.py`
2. Se faltar alguma ferramenta, instale usando os botões na janela que aparecer
3. Clique em "Adicionar" no jogo que você quer
4. Aguarde o processamento
5. Clique em "Reiniciar Steam" quando concluir

Para mais informações, consulte o README.md.

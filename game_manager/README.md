# 🎮 Game Manager

Uma aplicação desktop moderna, profissional e extremamente intuitiva para gerenciamento de jogos.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)

## ✨ Características

- **Interface Premium**: Design moderno inspirado em Discord, Steam e VS Code
- **Dark Mode**: Tema escuro elegante para conforto visual
- **Simplicidade**: Poucos cliques, experiência fluida
- **Velocidade**: Resposta rápida e animações suaves
- **Status em Tempo Real**: Monitoramento automático de integrações
- **Histórico**: Acompanhamento de todas as operações

## 🚀 Funcionalidades

### Tela Principal
- Campo de pesquisa intuitivo
- Seleção de jogos com visualização de capa
- Informações básicas do jogo
- Status da seleção

### Operação Principal
- Botão "Adicionar à Biblioteca" destacado
- Barra de progresso em tempo real
- Feedback visual constante
- Mensagem de sucesso elegante

### Pós-Processamento
- Opção de reiniciar Steam (recomendado)
- Alternativa "Fazer Depois"
- Histórico de operações com data/hora

### Painel de Status
- Monitoramento de conexões:
  - Steam ● Online
  - Integração 1 ● Online
  - Integração 2 ● Online

### Configurações
- Preferências da aplicação
- Opções de inicialização
- Logs e diagnóstico
- Gerenciamento de integrações

## 🔧 Ferramentas Requeridas

O sistema requer as seguintes ferramentas instaladas:

### 1. Steam Tools
Cliente Steam para gerenciamento de biblioteca de jogos.

**Verificação:**
```bash
# Windows
tasklist | findstr steam.exe

# Linux
pgrep -x steam

# macOS
pgrep -x Steam
```

**Instalação:**
- Baixe em: https://store.steampowered.com/about/
- Siga o assistente de instalação

### 2. Lua Tools
Runtime Lua para execução de scripts.

**Verificação:**
```bash
lua -v
```

**Instalação:**

#### Windows
```powershell
# Usando winget
winget install -e --id Lua.Lua.5.4

# Ou baixe manualmente em: https://www.lua.org/download.html
```

#### macOS
```bash
# Usando Homebrew
brew install lua
```

#### Linux
```bash
# Ubuntu/Debian
sudo apt-get install lua5.4

# Fedora
sudo dnf install lua

# Arch
sudo pacman -S lua
```

## 📦 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos

1. **Clone o repositório:**
```bash
git clone <repository-url>
cd game_manager
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Execute a aplicação:**
```bash
python main.py
```

ou

```bash
python backend/main.py
```

## 🎨 Interface

A interface foi projetada com foco em:

1. **Beleza**: Visual moderno e tecnológico
2. **Rapidez**: Respostas instantâneas
3. **Intuitividade**: Fluxo natural de uso
4. **Minimalismo**: Apenas botões essenciais
5. **Feedback**: Indicadores visuais constantes

### Paleta de Cores

- **Background Primário**: `#1a1b26` (Dark)
- **Background Secundário**: `#24283b` (Cards)
- **Accent Primary**: `#7aa2f7` (Blue)
- **Success**: `#9ece6a` (Green)
- **Error**: `#f7768e` (Red)

## 🏗️ Arquitetura

```
game_manager/
├── backend/
│   ├── integrations/
│   │   ├── __init__.py
│   │   ├── steam.py        # Integração Steam
│   │   ├── lua.py          # Integração Lua
│   │   └── manager.py      # Gerenciador de integrações
│   ├── tools_manager.py    # Gerenciamento de ferramentas
│   ├── game_service.py     # Serviço de jogos
│   ├── status_monitor.py   # Monitor de status
│   └── __init__.py
├── frontend/
│   ├── __init__.py
│   ├── main_window.py      # Janela principal
│   ├── theme.py            # Gerenciador de tema
│   └── components.py       # Componentes UI
├── assets/                 # Recursos (imagens, ícones)
├── utils/                  # Utilitários
├── main.py                 # Entry point
├── requirements.txt        # Dependências Python
├── package.json            # Metadados do projeto
└── README.md               # Este arquivo
```

## 🔌 Integrações

### Steam Integration
- Detecção automática de instalação
- Verificação de status online/offline
- Reinício do cliente
- Adição de jogos não-Steam

### Lua Integration
- Execução de scripts
- Snippets de código
- Verificação de versão
- Suporte multiplataforma

## 📝 Uso

### Adicionando um Jogo

1. Digite o nome do jogo no campo de pesquisa
2. Clique em "Selecionar Jogo" ou pressione Enter
3. Selecione o jogo desejado nos resultados
4. Clique em "Adicionar à Biblioteca"
5. Aguarde o processamento
6. Escolha entre "Reiniciar Steam" ou "Fazer Depois"

### Verificando Histórico

- Clique no botão "📜 Histórico" no painel inferior
- Visualize as últimas 10 operações
- Status indicado por ✓ (sucesso) ou ✗ (falha)

### Configurando Preferências

1. Clique em ⚙️ no canto superior direito
2. Navegue pelas abas:
   - **Preferências**: Configurações gerais
   - **Ferramentas**: Status e instalação de tools
   - **Logs**: Diagnóstico do sistema

## 🛠️ Desenvolvimento

### Estrutura Modular

O código segue princípios de:
- **Separação de responsabilidades**: Frontend e Backend separados
- **Escalabilidade**: Fácil adição de novas integrações
- **Manutenibilidade**: Código organizado e documentado
- **Reusabilidade**: Componentes UI modulares

### Adicionando Novas Integrações

1. Crie uma nova classe em `backend/integrations/`
2. Implemente os métodos necessários:
   - `is_online()`: Verifica status
   - `get_status()`: Retorna informações
3. Registre no `IntegrationManager`

### Customizando o Tema

Edite `frontend/theme.py` para modificar:
- Cores
- Fontes
- Espaçamento
- Estilos de componentes

## 🐛 Troubleshooting

### Steam não detectado
- Verifique se o Steam está instalado
- Execute como administrador (Windows)
- Verifique permissões (Linux/macOS)

### Lua não detectado
- Instale Lua usando o gerenciador de pacotes
- Adicione ao PATH do sistema
- Reinicie a aplicação

### Erros de dependência
```bash
pip install --upgrade -r requirements.txt
```

## 📄 Licença

MIT License - Veja o arquivo LICENSE para detalhes.

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor:

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📞 Suporte

Para issues e suporte, abra uma issue no repositório.

---

**Desenvolvido com ❤️ para gamers**

*Game Manager - Simplificando o gerenciamento da sua biblioteca de jogos*

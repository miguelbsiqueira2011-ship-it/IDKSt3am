#!/bin/bash
# Game Manager - Quick Start Script
# This script helps you get started quickly

echo "======================================"
echo "  🎮 Game Manager - Quick Start"
echo "======================================"
echo ""

# Check Python version
echo "📌 Checking Python installation..."
python_version=$(python3 --version 2>&1)
if [ $? -eq 0 ]; then
    echo "✓ $python_version"
else
    echo "✗ Python 3.8+ is required"
    exit 1
fi

# Check and install dependencies
echo ""
echo "📦 Checking dependencies..."
pip3 show customtkinter > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✓ customtkinter installed"
else
    echo "⚠ Installing customtkinter..."
    pip3 install customtkinter
fi

pip3 show Pillow > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✓ Pillow installed"
else
    echo "⚠ Installing Pillow..."
    pip3 install Pillow
fi

pip3 show requests > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✓ requests installed"
else
    echo "⚠ Installing requests..."
    pip3 install requests
fi

pip3 show psutil > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✓ psutil installed"
else
    echo "⚠ Installing psutil..."
    pip3 install psutil
fi

# Check required tools
echo ""
echo "🔧 Checking required tools..."

# Check Steam
steam_installed=false
if command -v steam &> /dev/null; then
    echo "✓ Steam CLI found"
    steam_installed=true
elif [ -f "$HOME/.steam/steam" ]; then
    echo "✓ Steam installation found"
    steam_installed=true
elif [ -f "/Applications/Steam.app" ]; then
    echo "✓ Steam installation found (macOS)"
    steam_installed=true
elif [ -f "C:/Program Files (x86)/Steam/steam.exe" ] || [ -f "C:/Program Files/Steam/steam.exe" ]; then
    echo "✓ Steam installation found (Windows)"
    steam_installed=true
else
    echo "⚠ Steam not detected"
    echo "  Download from: https://store.steampowered.com/about/"
fi

# Check Lua
lua_installed=false
if command -v lua &> /dev/null; then
    lua_version=$(lua -v 2>&1)
    echo "✓ $lua_version"
    lua_installed=true
else
    echo "⚠ Lua not detected"
    echo "  Install with:"
    echo "    - Windows: winget install Lua.Lua.5.4"
    echo "    - macOS:   brew install lua"
    echo "    - Linux:   sudo apt-get install lua5.4"
fi

# Run the application
echo ""
echo "======================================"
echo "  Starting Game Manager..."
echo "======================================"
echo ""

cd "$(dirname "$0")"
python3 main.py

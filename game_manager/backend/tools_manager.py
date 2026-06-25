"""
Tools Manager - Handles installation and management of required tools
"""

import subprocess
import os
import platform
from typing import Dict, Any, Optional, Callable


class ToolsManager:
    """Manages installation and verification of required tools"""
    
    def __init__(self):
        self.system = platform.system()
        self.install_callbacks: Dict[str, Callable] = {
            "steam": self._install_steam_instructions,
            "lua": self._install_lua
        }
    
    def check_tool_installed(self, tool_name: str) -> bool:
        """Check if a specific tool is installed"""
        if tool_name.lower() == "steam":
            return self._check_steam_installed()
        elif tool_name.lower() == "lua":
            return self._check_lua_installed()
        return False
    
    def _check_steam_installed(self) -> bool:
        """Check if Steam is installed"""
        if self.system == "Windows":
            paths = [
                r"C:\Program Files (x86)\Steam\steam.exe",
                r"C:\Program Files\Steam\steam.exe"
            ]
            return any(os.path.exists(p) for p in paths)
        elif self.system == "Darwin":
            return os.path.exists("/Applications/Steam.app")
        else:  # Linux
            paths = [
                os.path.expanduser("~/.steam/steam"),
                "/usr/games/steam"
            ]
            return any(os.path.exists(p) for p in paths)
    
    def _check_lua_installed(self) -> bool:
        """Check if Lua is installed"""
        try:
            cmd = ["which", "lua"] if self.system != "Windows" else ["where", "lua"]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                return True
            
            # Check common paths
            if self.system == "Windows":
                paths = [
                    r"C:\Program Files\Lua\5.4\lua.exe",
                    r"C:\Program Files (x86)\Lua\5.4\lua.exe"
                ]
                return any(os.path.exists(p) for p in paths)
            else:
                paths = ["/usr/bin/lua", "/usr/local/bin/lua"]
                return any(os.path.exists(p) for p in paths)
        except Exception:
            return False
    
    def install_tool(self, tool_name: str, progress_callback: Optional[Callable] = None) -> Dict[str, Any]:
        """Install a specific tool"""
        if tool_name.lower() not in self.install_callbacks:
            return {
                "success": False,
                "error": f"Unknown tool: {tool_name}"
            }
        
        try:
            callback = self.install_callbacks[tool_name.lower()]
            return callback(progress_callback)
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def _install_steam_instructions(self, progress_callback: Optional[Callable] = None) -> Dict[str, Any]:
        """Provide Steam installation instructions"""
        if progress_callback:
            progress_callback(10, "Opening Steam download page...")
        
        # Open Steam download page in browser
        try:
            import webbrowser
            webbrowser.open("https://store.steampowered.com/about/")
            
            if progress_callback:
                progress_callback(100, "Steam download page opened. Please follow the installation wizard.")
            
            return {
                "success": True,
                "message": "Steam download page opened. Please complete the installation manually.",
                "manual_install": True
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to open browser: {str(e)}"
            }
    
    def _install_lua(self, progress_callback: Optional[Callable] = None) -> Dict[str, Any]:
        """Install Lua based on platform"""
        try:
            if progress_callback:
                progress_callback(10, "Starting Lua installation...")
            
            if self.system == "Windows":
                return self._install_lua_windows(progress_callback)
            elif self.system == "Darwin":
                return self._install_lua_macos(progress_callback)
            else:  # Linux
                return self._install_lua_linux(progress_callback)
                
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def _install_lua_windows(self, progress_callback: Optional[Callable] = None) -> Dict[str, Any]:
        """Install Lua on Windows using PowerShell"""
        try:
            if progress_callback:
                progress_callback(30, "Downloading and installing Lua Tools...")
            
            # Use the official Lua Tools PowerShell installer
            powershell_cmd = 'irm "https://ps.lua.tools/install-plugin-legacy.ps1" | iex'
            
            result = subprocess.run(
                ["powershell", "-ExecutionPolicy", "Bypass", "-Command", powershell_cmd],
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if result.returncode == 0:
                if progress_callback:
                    progress_callback(100, "Lua Tools installed successfully!")
                return {"success": True, "message": "Lua Tools installed successfully"}
            else:
                # Fallback to manual installation
                import webbrowser
                webbrowser.open("https://www.lua.org/download.html")
                if progress_callback:
                    progress_callback(100, "Please download and install Lua manually from the opened page.")
                return {
                    "success": True,
                    "message": "Lua download page opened. Please complete installation manually.",
                    "manual_install": True
                }
        except Exception:
            # Fallback to manual installation
            import webbrowser
            webbrowser.open("https://www.lua.org/download.html")
            return {
                "success": True,
                "message": "Lua download page opened. Please complete installation manually.",
                "manual_install": True
            }
    
    def _install_lua_macos(self, progress_callback: Optional[Callable] = None) -> Dict[str, Any]:
        """Install Lua on macOS using Homebrew"""
        try:
            if progress_callback:
                progress_callback(20, "Checking Homebrew...")
            
            # Check if Homebrew is installed
            brew_check = subprocess.run(["which", "brew"], capture_output=True)
            
            if brew_check.returncode != 0:
                # Homebrew not installed, provide manual instructions
                import webbrowser
                webbrowser.open("https://brew.sh")
                if progress_callback:
                    progress_callback(100, "Please install Homebrew first, then run: brew install lua")
                return {
                    "success": False,
                    "error": "Homebrew not installed",
                    "manual_install": True
                }
            
            if progress_callback:
                progress_callback(40, "Installing Lua via Homebrew...")
            
            result = subprocess.run(
                ["brew", "install", "lua"],
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if result.returncode == 0:
                if progress_callback:
                    progress_callback(100, "Lua installed successfully!")
                return {"success": True, "message": "Lua installed successfully"}
            else:
                return {"success": False, "error": result.stderr}
                
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _install_lua_linux(self, progress_callback: Optional[Callable] = None) -> Dict[str, Any]:
        """Install Lua on Linux"""
        try:
            if progress_callback:
                progress_callback(20, "Detecting package manager...")
            
            # Try different package managers
            package_managers = [
                (["apt-get", "-v"], "apt-get", ["sudo", "apt-get", "install", "-y", "lua5.4"]),
                (["dnf", "-v"], "dnf", ["sudo", "dnf", "install", "-y", "lua"]),
                (["yum", "-v"], "yum", ["sudo", "yum", "install", "-y", "lua"]),
                (["pacman", "-V"], "pacman", ["sudo", "pacman", "-S", "--noconfirm", "lua"]),
            ]
            
            for check_cmd, name, install_cmd in package_managers:
                check = subprocess.run(check_cmd, capture_output=True)
                if check.returncode == 0:
                    if progress_callback:
                        progress_callback(50, f"Installing Lua via {name}...")
                    
                    result = subprocess.run(
                        install_cmd,
                        capture_output=True,
                        text=True,
                        timeout=120
                    )
                    
                    if result.returncode == 0:
                        if progress_callback:
                            progress_callback(100, "Lua installed successfully!")
                        return {"success": True, "message": "Lua installed successfully"}
                    else:
                        return {"success": False, "error": result.stderr}
            
            # No package manager found
            return {
                "success": False,
                "error": "No supported package manager found. Please install Lua manually."
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_all_tools_status(self) -> Dict[str, Dict[str, Any]]:
        """Get status of all required tools"""
        return {
            "steam": {
                "installed": self._check_steam_installed(),
                "name": "Steam",
                "description": "Steam client for game management"
            },
            "lua": {
                "installed": self._check_lua_installed(),
                "name": "Lua Tools",
                "description": "Lua runtime for script execution"
            }
        }

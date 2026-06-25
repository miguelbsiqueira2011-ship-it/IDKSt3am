"""
Lua Integration - Handles Lua runtime and script execution
"""

import subprocess
import os
import platform
from typing import Optional, Dict, Any


class LuaIntegration:
    """Manages Lua runtime integration for game scripting"""
    
    def __init__(self):
        self.lua_path = self._find_lua_path()
        self.is_installed = self.lua_path is not None
        
    def _find_lua_path(self) -> Optional[str]:
        """Find Lua installation path"""
        try:
            # Try to find lua executable in PATH
            result = subprocess.run(
                ["which", "lua"] if platform.system() != "Windows" 
                else ["where", "lua"],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip().split('\n')[0]
                
            # Common installation paths
            system = platform.system()
            if system == "Windows":
                paths = [
                    r"C:\Program Files\Lua\5.4\lua.exe",
                    r"C:\Program Files (x86)\Lua\5.4\lua.exe",
                    r"C:\Lua\lua.exe"
                ]
                for path in paths:
                    if os.path.exists(path):
                        return path
                        
            elif system == "Darwin":  # macOS
                mac_paths = [
                    "/usr/local/bin/lua",
                    "/opt/homebrew/bin/lua",
                    "/usr/bin/lua"
                ]
                for path in mac_paths:
                    if os.path.exists(path):
                        return path
                        
            elif system == "Linux":
                linux_paths = [
                    "/usr/bin/lua",
                    "/usr/local/bin/lua",
                    os.path.expanduser("~/.luarocks/bin/lua")
                ]
                for path in linux_paths:
                    if os.path.exists(path):
                        return path
        except Exception:
            pass
            
        return None
    
    def is_online(self) -> bool:
        """Check if Lua is available and working"""
        try:
            result = subprocess.run(
                [self.lua_path or "lua", "-v"],
                capture_output=True,
                timeout=5
            )
            return result.returncode == 0
        except Exception:
            return False
    
    def get_version(self) -> Optional[str]:
        """Get Lua version string"""
        try:
            result = subprocess.run(
                [self.lua_path or "lua", "-v"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                return result.stderr.strip() or result.stdout.strip()
        except Exception:
            pass
        return None
    
    def execute_script(self, script_path: str, args: list = None) -> Dict[str, Any]:
        """Execute a Lua script"""
        if not self.is_installed:
            return {
                "success": False,
                "error": "Lua not installed",
                "output": ""
            }
        
        try:
            cmd = [self.lua_path, script_path]
            if args:
                cmd.extend(args)
                
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            return {
                "success": result.returncode == 0,
                "output": result.stdout,
                "error": result.stderr,
                "return_code": result.returncode
            }
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "error": "Script execution timed out",
                "output": ""
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "output": ""
            }
    
    def run_snippet(self, code: str) -> Dict[str, Any]:
        """Run a Lua code snippet"""
        if not self.is_installed:
            return {
                "success": False,
                "error": "Lua not installed",
                "output": ""
            }
        
        try:
            result = subprocess.run(
                [self.lua_path or "lua", "-e", code],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            return {
                "success": result.returncode == 0,
                "output": result.stdout,
                "error": result.stderr
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "output": ""
            }
    
    def get_status(self) -> Dict[str, Any]:
        """Get current Lua status"""
        return {
            "name": "Lua Tools",
            "online": self.is_online(),
            "installed": self.is_installed,
            "path": self.lua_path,
            "version": self.get_version() if self.is_installed else None
        }

"""
Steam Integration - Handles Steam API and client interactions
"""

import subprocess
import os
import platform
from typing import Optional, Dict, Any


class SteamIntegration:
    """Manages Steam integration for game management"""
    
    def __init__(self):
        self.steam_path = self._find_steam_path()
        self.is_installed = self.steam_path is not None
        
    def _find_steam_path(self) -> Optional[str]:
        """Find Steam installation path based on OS"""
        system = platform.system()
        
        if system == "Windows":
            paths = [
                r"C:\Program Files (x86)\Steam\steam.exe",
                r"C:\Program Files\Steam\steam.exe"
            ]
            for path in paths:
                if os.path.exists(path):
                    return path
                    
        elif system == "Darwin":  # macOS
            mac_path = "/Applications/Steam.app"
            if os.path.exists(mac_path):
                return mac_path
                
        elif system == "Linux":
            linux_paths = [
                os.path.expanduser("~/.steam/steam"),
                "/usr/games/steam"
            ]
            for path in linux_paths:
                if os.path.exists(path):
                    return path
                    
        return None
    
    def is_online(self) -> bool:
        """Check if Steam is running and online"""
        try:
            if platform.system() == "Windows":
                result = subprocess.run(
                    ["tasklist"], 
                    capture_output=True, 
                    text=True
                )
                return "steam.exe" in result.stdout.lower()
            elif platform.system() == "Darwin":
                result = subprocess.run(
                    ["pgrep", "-x", "Steam"],
                    capture_output=True
                )
                return result.returncode == 0
            else:  # Linux
                result = subprocess.run(
                    ["pgrep", "-x", "steam"],
                    capture_output=True
                )
                return result.returncode == 0
        except Exception:
            return False
    
    def restart(self) -> bool:
        """Restart Steam client"""
        try:
            # First, close Steam
            self._close_steam()
            
            # Then reopen
            if self.steam_path:
                if platform.system() == "Windows":
                    subprocess.Popen([self.steam_path])
                elif platform.system() == "Darwin":
                    subprocess.Popen(["open", self.steam_path])
                else:  # Linux
                    subprocess.Popen([self.steam_path])
                return True
            return False
        except Exception as e:
            print(f"Error restarting Steam: {e}")
            return False
    
    def _close_steam(self) -> None:
        """Force close Steam client"""
        try:
            if platform.system() == "Windows":
                subprocess.run(["taskkill", "/F", "/IM", "steam.exe"], 
                             capture_output=True)
            elif platform.system() == "Darwin":
                subprocess.run(["pkill", "-9", "Steam"], capture_output=True)
            else:  # Linux
                subprocess.run(["pkill", "-9", "steam"], capture_output=True)
        except Exception:
            pass
    
    def get_library_games(self) -> list:
        """Get list of games from Steam library"""
        # This would normally use Steam Web API
        # For now, return mock data structure
        return []
    
    def add_game_to_shortcuts(self, game_name: str, game_path: str) -> bool:
        """Add a non-Steam game to Steam shortcuts"""
        # Implementation would modify Steam's shortcut files
        # This is a placeholder for the actual implementation
        print(f"Adding {game_name} to Steam shortcuts")
        return True
    
    def get_status(self) -> Dict[str, Any]:
        """Get current Steam status"""
        return {
            "name": "Steam",
            "online": self.is_online(),
            "installed": self.is_installed,
            "path": self.steam_path
        }

"""
Integration Manager - Manages all backend integrations
"""

from typing import Dict, Any, List
from .steam import SteamIntegration
from .lua import LuaIntegration


class IntegrationManager:
    """Central manager for all service integrations"""
    
    def __init__(self):
        self.steam = SteamIntegration()
        self.lua = LuaIntegration()
        self._integrations: Dict[str, Any] = {
            "steam": self.steam,
            "lua": self.lua
        }
    
    def get_all_statuses(self) -> List[Dict[str, Any]]:
        """Get status of all integrations"""
        statuses = []
        for name, integration in self._integrations.items():
            try:
                status = integration.get_status()
                statuses.append(status)
            except Exception as e:
                statuses.append({
                    "name": name.title(),
                    "online": False,
                    "error": str(e)
                })
        return statuses
    
    def is_all_online(self) -> bool:
        """Check if all integrations are online"""
        return all(
            integration.is_online() 
            for integration in self._integrations.values()
        )
    
    def get_integration(self, name: str) -> Any:
        """Get a specific integration by name"""
        return self._integrations.get(name.lower())
    
    def check_dependencies(self) -> Dict[str, bool]:
        """Check which dependencies are installed"""
        return {
            "steam": self.steam.is_installed,
            "lua": self.lua.is_installed
        }
    
    def get_missing_dependencies(self) -> List[str]:
        """Get list of missing dependencies"""
        missing = []
        if not self.steam.is_installed:
            missing.append("Steam")
        if not self.lua.is_installed:
            missing.append("Lua")
        return missing

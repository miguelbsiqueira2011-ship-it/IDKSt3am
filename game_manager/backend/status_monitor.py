"""
Status Monitor - Monitors all integrations and provides real-time status updates
"""

import threading
import time
from typing import Dict, Any, List, Callable, Optional
from datetime import datetime


class StatusMonitor:
    """Monitors and reports status of all integrations"""
    
    def __init__(self, integration_manager):
        self.integration_manager = integration_manager
        self._running = False
        self._update_interval = 5.0  # seconds
        self._thread: Optional[threading.Thread] = None
        self._callbacks: List[Callable] = []
        self._last_status: Dict[str, Any] = {}
    
    def start(self) -> None:
        """Start the status monitoring thread"""
        if self._running:
            return
            
        self._running = True
        self._thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self._thread.start()
    
    def stop(self) -> None:
        """Stop the status monitoring thread"""
        self._running = False
        if self._thread:
            self._thread.join(timeout=2.0)
            self._thread = None
    
    def add_callback(self, callback: Callable) -> None:
        """Add a callback to be called on status updates"""
        if callback not in self._callbacks:
            self._callbacks.append(callback)
    
    def remove_callback(self, callback: Callable) -> None:
        """Remove a status update callback"""
        if callback in self._callbacks:
            self._callbacks.remove(callback)
    
    def _monitor_loop(self) -> None:
        """Main monitoring loop"""
        while self._running:
            try:
                current_status = self.get_current_status()
                
                # Only notify if status changed
                if current_status != self._last_status:
                    self._last_status = current_status
                    self._notify_callbacks(current_status)
                    
            except Exception as e:
                print(f"Status monitor error: {e}")
            
            time.sleep(self._update_interval)
    
    def _notify_callbacks(self, status: Dict[str, Any]) -> None:
        """Notify all registered callbacks"""
        for callback in self._callbacks:
            try:
                callback(status)
            except Exception as e:
                print(f"Callback error: {e}")
    
    def get_current_status(self) -> Dict[str, Any]:
        """Get current status of all integrations"""
        statuses = self.integration_manager.get_all_statuses()
        
        all_online = all(s.get("online", False) for s in statuses)
        
        return {
            "timestamp": datetime.now().isoformat(),
            "all_online": all_online,
            "integrations": statuses,
            "summary": {
                "total": len(statuses),
                "online": sum(1 for s in statuses if s.get("online", False)),
                "offline": sum(1 for s in statuses if not s.get("online", False))
            }
        }
    
    def get_status_summary(self) -> str:
        """Get a human-readable status summary"""
        status = self.get_current_status()
        online_count = status["summary"]["online"]
        total_count = status["summary"]["total"]
        
        if online_count == total_count:
            return f"All systems operational ({online_count}/{total_count})"
        else:
            return f"{online_count}/{total_count} systems online"
    
    def is_ready(self) -> bool:
        """Check if all integrations are ready"""
        return self.integration_manager.is_all_online()

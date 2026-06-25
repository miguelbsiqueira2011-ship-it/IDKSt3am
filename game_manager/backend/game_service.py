"""
Game Service - Handles game search, selection, and library management
"""

import requests
from typing import Optional, Dict, Any, List
from datetime import datetime


class GameService:
    """Manages game search and library operations"""
    
    def __init__(self):
        self.api_base = "https://api.igdb.com/v4"
        self.selected_game: Optional[Dict[str, Any]] = None
        
    def search_games(self, query: str) -> List[Dict[str, Any]]:
        """Search for games using IGDB API (mock implementation)"""
        # In production, this would use the actual IGDB API
        # For now, return mock data for demonstration
        
        mock_games = [
            {
                "id": 1,
                "name": "Cyberpunk 2077",
                "cover_url": "https://images.igdb.com/igdb/image/upload/t_cover_big/co2lye.jpg",
                "release_date": "2020-12-10",
                "genres": ["RPG", "Action"],
                "rating": 86
            },
            {
                "id": 2,
                "name": "The Witcher 3: Wild Hunt",
                "cover_url": "https://images.igdb.com/igdb/image/upload/t_cover_big/co2rhz.jpg",
                "release_date": "2015-05-19",
                "genres": ["RPG", "Adventure"],
                "rating": 93
            },
            {
                "id": 3,
                "name": "Elden Ring",
                "cover_url": "https://images.igdb.com/igdb/image/upload/t_cover_big/co3p8l.jpg",
                "release_date": "2022-02-25",
                "genres": ["RPG", "Action"],
                "rating": 96
            },
            {
                "id": 4,
                "name": "Red Dead Redemption 2",
                "cover_url": "https://images.igdb.com/igdb/image/upload/t_cover_big/co2afw.jpg",
                "release_date": "2018-10-26",
                "genres": ["Action", "Adventure"],
                "rating": 97
            },
            {
                "id": 5,
                "name": "God of War",
                "cover_url": "https://images.igdb.com/igdb/image/upload/t_cover_big/co2i4n.jpg",
                "release_date": "2018-04-20",
                "genres": ["Action", "Adventure"],
                "rating": 94
            }
        ]
        
        if not query:
            return mock_games[:3]
        
        # Filter mock games by query
        query_lower = query.lower()
        filtered = [
            game for game in mock_games 
            if query_lower in game["name"].lower()
        ]
        
        return filtered if filtered else mock_games[:3]
    
    def get_game_details(self, game_id: int) -> Optional[Dict[str, Any]]:
        """Get detailed information about a specific game"""
        # Mock implementation
        games = {
            1: {
                "id": 1,
                "name": "Cyberpunk 2077",
                "cover_url": "https://images.igdb.com/igdb/image/upload/t_cover_big/co2lye.jpg",
                "release_date": "2020-12-10",
                "genres": ["RPG", "Action"],
                "rating": 86,
                "description": "An open-world, action-adventure story set in Night City.",
                "developer": "CD Projekt Red",
                "publisher": "CD Projekt"
            },
            2: {
                "id": 2,
                "name": "The Witcher 3: Wild Hunt",
                "cover_url": "https://images.igdb.com/igdb/image/upload/t_cover_big/co2rhz.jpg",
                "release_date": "2015-05-19",
                "genres": ["RPG", "Adventure"],
                "rating": 93,
                "description": "You are Geralt of Rivia, mercenary monster slayer.",
                "developer": "CD Projekt Red",
                "publisher": "CD Projekt"
            },
            3: {
                "id": 3,
                "name": "Elden Ring",
                "cover_url": "https://images.igdb.com/igdb/image/upload/t_cover_big/co3p8l.jpg",
                "release_date": "2022-02-25",
                "genres": ["RPG", "Action"],
                "rating": 96,
                "description": "Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring.",
                "developer": "FromSoftware",
                "publisher": "Bandai Namco"
            }
        }
        
        return games.get(game_id)
    
    def select_game(self, game: Dict[str, Any]) -> bool:
        """Select a game for addition to library"""
        try:
            self.selected_game = game
            return True
        except Exception:
            return False
    
    def get_selected_game(self) -> Optional[Dict[str, Any]]:
        """Get the currently selected game"""
        return self.selected_game
    
    def clear_selection(self) -> None:
        """Clear the current game selection"""
        self.selected_game = None
    
    def add_to_library(self, game: Dict[str, Any], callback: Optional[callable] = None) -> Dict[str, Any]:
        """Add a game to the library with progress tracking"""
        try:
            steps = [
                (10, "Validating game data..."),
                (30, "Preparing installation files..."),
                (50, "Configuring integration..."),
                (70, "Adding to Steam shortcuts..."),
                (90, "Finalizing setup..."),
                (100, "Complete!")
            ]
            
            for progress, message in steps:
                if callback:
                    callback(progress, message)
                # Simulate processing time
                import time
                time.sleep(0.3)
            
            return {
                "success": True,
                "game": game,
                "timestamp": datetime.now().isoformat(),
                "message": f"{game['name']} added to library successfully"
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def download_cover_image(self, url: str, save_path: str) -> bool:
        """Download and save a game cover image"""
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                with open(save_path, 'wb') as f:
                    f.write(response.content)
                return True
            return False
        except Exception:
            return False

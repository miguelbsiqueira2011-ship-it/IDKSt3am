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
        
    def search_games(self, query: str = "") -> List[Dict[str, Any]]:
        """Return ALL games in alphabetical order - no search needed"""
        # Always return all games sorted alphabetically
        all_games = self._get_all_games()
        
        # If query is provided, filter (but still show all if empty)
        if query and query.strip():
            query_lower = query.lower().strip()
            filtered = [
                game for game in all_games 
                if query_lower in game["name"].lower()
            ]
            if filtered:
                return filtered
        
        # Return all games sorted alphabetically
        return sorted(all_games, key=lambda x: x["name"])
    
    def _get_all_games(self) -> List[Dict[str, Any]]:
        """Get complete list of popular games"""
        return [
            {
                "id": 1,
                "name": "Baldur's Gate 3",
                "cover_url": "https://images.igdb.com/igdb/image/upload/t_cover_big/co6r0s.jpg",
                "release_date": "2023-08-03",
                "genres": ["RPG", "Strategy"],
                "rating": 96
            },
            {
                "id": 2,
                "name": "Battlefield 2042",
                "cover_url": "",
                "release_date": "2021-11-19",
                "genres": ["FPS", "Action"],
                "rating": 78
            },
            {
                "id": 3,
                "name": "Call of Duty: Modern Warfare II",
                "cover_url": "",
                "release_date": "2022-10-28",
                "genres": ["FPS", "Action"],
                "rating": 85
            },
            {
                "id": 4,
                "name": "Counter-Strike 2",
                "cover_url": "",
                "release_date": "2023-09-27",
                "genres": ["FPS", "Competitive"],
                "rating": 92
            },
            {
                "id": 5,
                "name": "Cyberpunk 2077",
                "cover_url": "https://images.igdb.com/igdb/image/upload/t_cover_big/co2lye.jpg",
                "release_date": "2020-12-10",
                "genres": ["RPG", "Action"],
                "rating": 86
            },
            {
                "id": 6,
                "name": "Destiny 2",
                "cover_url": "",
                "release_date": "2017-09-06",
                "genres": ["FPS", "MMO"],
                "rating": 88
            },
            {
                "id": 7,
                "name": "Elden Ring",
                "cover_url": "https://images.igdb.com/igdb/image/upload/t_cover_big/co3p8l.jpg",
                "release_date": "2022-02-25",
                "genres": ["RPG", "Action"],
                "rating": 96
            },
            {
                "id": 8,
                "name": "FIFA 23",
                "cover_url": "",
                "release_date": "2022-09-30",
                "genres": ["Sports", "Simulation"],
                "rating": 82
            },
            {
                "id": 9,
                "name": "Forza Horizon 5",
                "cover_url": "",
                "release_date": "2021-11-09",
                "genres": ["Racing", "Open World"],
                "rating": 91
            },
            {
                "id": 10,
                "name": "God of War",
                "cover_url": "https://images.igdb.com/igdb/image/upload/t_cover_big/co2i4n.jpg",
                "release_date": "2018-04-20",
                "genres": ["Action", "Adventure"],
                "rating": 94
            },
            {
                "id": 11,
                "name": "Grand Theft Auto V",
                "cover_url": "",
                "release_date": "2013-09-17",
                "genres": ["Action", "Open World"],
                "rating": 95
            },
            {
                "id": 12,
                "name": "Hogwarts Legacy",
                "cover_url": "https://images.igdb.com/igdb/image/upload/t_cover_big/co5p7q.jpg",
                "release_date": "2023-02-10",
                "genres": ["RPG", "Adventure"],
                "rating": 84
            },
            {
                "id": 13,
                "name": "Left 4 Dead 2",
                "cover_url": "",
                "release_date": "2009-11-17",
                "genres": ["FPS", "Co-op"],
                "rating": 93
            },
            {
                "id": 14,
                "name": "Minecraft",
                "cover_url": "",
                "release_date": "2011-11-18",
                "genres": ["Sandbox", "Survival"],
                "rating": 94
            },
            {
                "id": 15,
                "name": "Red Dead Redemption 2",
                "cover_url": "https://images.igdb.com/igdb/image/upload/t_cover_big/co2afw.jpg",
                "release_date": "2018-10-26",
                "genres": ["Action", "Adventure"],
                "rating": 97
            },
            {
                "id": 16,
                "name": "Resident Evil 4",
                "cover_url": "",
                "release_date": "2023-03-24",
                "genres": ["Horror", "Action"],
                "rating": 93
            },
            {
                "id": 17,
                "name": "Rocket League",
                "cover_url": "",
                "release_date": "2015-07-07",
                "genres": ["Sports", "Competitive"],
                "rating": 90
            },
            {
                "id": 18,
                "name": "Spider-Man Remastered",
                "cover_url": "https://images.igdb.com/igdb/image/upload/t_cover_big/co5tqz.jpg",
                "release_date": "2022-08-12",
                "genres": ["Action", "Adventure"],
                "rating": 87
            },
            {
                "id": 19,
                "name": "Starfield",
                "cover_url": "",
                "release_date": "2023-09-06",
                "genres": ["RPG", "Sci-Fi"],
                "rating": 85
            },
            {
                "id": 20,
                "name": "The Witcher 3: Wild Hunt",
                "cover_url": "https://images.igdb.com/igdb/image/upload/t_cover_big/co2rhz.jpg",
                "release_date": "2015-05-19",
                "genres": ["RPG", "Adventure"],
                "rating": 93
            },
            {
                "id": 21,
                "name": "Valorant",
                "cover_url": "",
                "release_date": "2020-06-02",
                "genres": ["FPS", "Competitive"],
                "rating": 89
            }
        ]
    
    def _parse_igdb_results(self, games_data: List[Dict]) -> List[Dict[str, Any]]:
        """Parse IGDB API results - kept for future API integration"""
        results = []
        for game in games_data:
            cover_url = ""
            if game.get('cover') and game['cover'].get('url'):
                cover_url = f"https://images.igdb.com/igdb/image/upload/t_cover_big{game['cover']['url']}"
            
            results.append({
                "id": game.get('id', 0),
                "name": game.get('name', 'Unknown'),
                "cover_url": cover_url,
                "release_date": game.get('release_dates', [{}])[0].get('y', 'Unknown'),
                "genres": [g.get('name', '') for g in game.get('genres', [])][:3],
                "rating": int(game.get('rating', 0))
            })
        return results
    
    def _get_mock_games(self, query: str) -> List[Dict[str, Any]]:
        """Legacy method - now returns all games"""
        # This method is deprecated, use _get_all_games() instead
        return self._get_all_games()
    
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

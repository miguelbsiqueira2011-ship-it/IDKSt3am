"""
Frontend Module - Modern UI for Game Manager
"""

from .main_window import MainWindow
from .theme import ThemeManager
from .components import (
    SearchBox,
    GameCard,
    StatusIndicator,
    ProgressBar,
    ActionButton
)

__all__ = [
    'MainWindow',
    'ThemeManager',
    'SearchBox',
    'GameCard',
    'StatusIndicator',
    'ProgressBar',
    'ActionButton'
]

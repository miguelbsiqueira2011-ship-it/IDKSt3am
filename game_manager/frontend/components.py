"""
UI Components - Reusable UI elements for the Game Manager
"""

import customtkinter as ctk
from tkinter import Event
from typing import Callable, Optional
from .theme import ThemeManager


class SearchBox(ctk.CTkFrame):
    """Modern search input box with icon"""
    
    def __init__(self, master, placeholder: str = "Pesquisar jogo...", 
                 command: Optional[Callable] = None, **kwargs):
        super().__init__(master, **kwargs)
        
        self.theme = ThemeManager()
        self.command = command
        self.placeholder = placeholder
        
        self.configure(
            fg_color=self.theme.COLORS["bg_tertiary"],
            corner_radius=self.theme.SPACING["button_corner"]
        )
        
        # Search icon (using text for simplicity)
        self.icon_label = ctk.CTkLabel(
            self,
            text="🔍",
            font=(self.theme.FONTS["family"], 16),
            text_color=self.theme.COLORS["text_muted"]
        )
        self.icon_label.pack(side="left", padx=(12, 0), pady=8)
        
        # Entry widget
        self.entry = ctk.CTkEntry(
            self,
            placeholder_text=placeholder,
            font=(self.theme.FONTS["family"], self.theme.FONTS["size_body"]),
            text_color=self.theme.COLORS["text_primary"],
            fg_color="transparent",
            border_width=0
        )
        self.entry.pack(side="left", fill="x", expand=True, padx=8, pady=8)
        
        # Bind events
        self.entry.bind("<Return>", lambda e: self._on_search())
        self.entry.bind("<KeyRelease>", lambda e: self._on_key_release())
    
    def _on_search(self) -> None:
        """Handle search action"""
        if self.command:
            self.command(self.get())
    
    def _on_key_release(self) -> None:
        """Handle key release for live search"""
        pass  # Can be used for live search
    
    def get(self) -> str:
        """Get current search text"""
        return self.entry.get()
    
    def clear(self) -> None:
        """Clear search text"""
        self.entry.delete(0, "end")
    
    def focus(self) -> None:
        """Focus the search entry"""
        self.entry.focus()


class GameCard(ctk.CTkFrame):
    """Card component for displaying game information with Add button"""
    
    def __init__(self, master, game_data: dict, on_add: Optional[Callable] = None, **kwargs):
        super().__init__(master, **kwargs)
        
        self.theme = ThemeManager()
        self.game_data = game_data
        self.on_add = on_add
        self.is_selected = False
        
        self.configure(
            fg_color=self.theme.COLORS["bg_secondary"],
            corner_radius=self.theme.SPACING["corner_radius"],
            border_width=0
        )
        
        self._setup_ui()
        
    def _setup_ui(self) -> None:
        """Setup the card UI with horizontal layout"""
        # Main horizontal layout
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=16, pady=16)
        
        # Left side - Cover image
        self.cover_frame = ctk.CTkFrame(
            main_frame,
            fg_color=self.theme.COLORS["bg_tertiary"],
            corner_radius=8,
            height=120,
            width=90
        )
        self.cover_frame.pack(side="left", padx=(0, 16))
        
        self.cover_label = ctk.CTkLabel(
            self.cover_frame,
            text="🎮",
            font=(self.theme.FONTS["family"], 32),
            text_color=self.theme.COLORS["text_muted"]
        )
        self.cover_label.place(relx=0.5, rely=0.5, anchor="center")
        
        # Right side - Info and button
        info_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        info_frame.pack(side="left", fill="both", expand=True)
        
        # Game name
        self.name_label = ctk.CTkLabel(
            info_frame,
            text=self.game_data.get("name", "Unknown Game"),
            font=(self.theme.FONTS["family"], self.theme.FONTS["size_heading"], "bold"),
            text_color=self.theme.COLORS["text_primary"],
            anchor="w"
        )
        self.name_label.pack(anchor="w", pady=(0, 4))
        
        # Genres
        genres = self.game_data.get("genres", [])
        if genres:
            self.genres_label = ctk.CTkLabel(
                info_frame,
                text=" • ".join(genres),
                font=(self.theme.FONTS["family"], self.theme.FONTS["size_small"]),
                text_color=self.theme.COLORS["text_secondary"],
                anchor="w"
            )
            self.genres_label.pack(anchor="w")
        
        # Rating
        rating = self.game_data.get("rating", 0)
        self.rating_label = ctk.CTkLabel(
            info_frame,
            text=f"★ {rating}",
            font=(self.theme.FONTS["family"], self.theme.FONTS["size_small"], "bold"),
            text_color=self.theme.COLORS["accent_warning"],
            anchor="w"
        )
        self.rating_label.pack(anchor="w", pady=(4, 0))
        
        # Add button at bottom right
        btn_frame = ctk.CTkFrame(info_frame, fg_color="transparent")
        btn_frame.pack(side="bottom", fill="x", pady=(8, 0))
        
        from .components import ActionButton
        self.add_btn = ActionButton(
            btn_frame,
            text="Adicionar",
            command=self._on_add_click,
            style="primary",
            height=32,
            width=100
        )
        self.add_btn.pack(side="right")
    
    def _on_add_click(self) -> None:
        """Handle add button click"""
        if self.on_add:
            self.on_add(self.game_data)


class StatusIndicator(ctk.CTkFrame):
    """Status indicator with dot and label"""
    
    def __init__(self, master, name: str, is_online: bool = True, **kwargs):
        super().__init__(master, **kwargs)
        
        self.theme = ThemeManager()
        self.name = name
        self.is_online = is_online
        
        self.configure(fg_color="transparent")
        self._setup_ui()
    
    def _setup_ui(self) -> None:
        """Setup the indicator UI"""
        # Status dot
        self.dot = ctk.CTkLabel(
            self,
            text="●",
            font=(self.theme.FONTS["family"], 10),
            text_color=self.theme.COLORS["status_online"] if self.is_online 
                       else self.theme.COLORS["status_offline"]
        )
        self.dot.pack(side="left", padx=(0, 6))
        
        # Label
        self.label = ctk.CTkLabel(
            self,
            text=self.name,
            font=(self.theme.FONTS["family"], self.theme.FONTS["size_small"]),
            text_color=self.theme.COLORS["text_secondary"]
        )
        self.label.pack(side="left")
    
    def update_status(self, is_online: bool) -> None:
        """Update the status indicator"""
        self.is_online = is_online
        self.dot.configure(
            text_color=self.theme.COLORS["status_online"] if is_online 
                       else self.theme.COLORS["status_offline"]
        )


class ProgressBar(ctk.CTkProgressBar):
    """Custom progress bar with modern styling"""
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.theme = ThemeManager()
        
        self.configure(
            fg_color=self.theme.COLORS["bg_tertiary"],
            progress_color=self.theme.COLORS["accent_primary"],
            corner_radius=self.theme.SPACING["button_corner"],
            height=8
        )
    
    def set_progress(self, value: float, text: str = "") -> None:
        """Set progress value and optionally update label"""
        self.set(value / 100.0)


class ActionButton(ctk.CTkButton):
    """Styled action button"""
    
    def __init__(self, master, text: str, command: Optional[Callable] = None,
                 style: str = "primary", **kwargs):
        super().__init__(master, text=text, command=command, **kwargs)
        
        self.theme = ThemeManager()
        self.theme.configure_button(self, style)

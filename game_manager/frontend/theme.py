"""
Theme Manager - Defines the modern dark theme for the application
Inspired by Discord, Steam, and VS Code
"""

import customtkinter as ctk


class ThemeManager:
    """Manages the application theme and styling"""
    
    # Color palette - Dark mode inspired by Discord/VS Code
    COLORS = {
        # Background colors
        "bg_primary": "#1a1b26",      # Main background (dark)
        "bg_secondary": "#24283b",    # Secondary background (cards, panels)
        "bg_tertiary": "#2f3549",     # Tertiary background (inputs, hover)
        "bg_accent": "#7aa2f7",       # Accent background
        
        # Text colors
        "text_primary": "#c0caf5",    # Primary text
        "text_secondary": "#a9b1d6",  # Secondary text
        "text_muted": "#565f89",      # Muted/disabled text
        
        # Accent colors
        "accent_primary": "#7aa2f7",  # Blue accent
        "accent_success": "#9ece6a",  # Green success
        "accent_warning": "#e0af68",  # Yellow warning
        "accent_error": "#f7768e",    # Red error
        "accent_purple": "#bb9af7",   # Purple accent
        
        # Status colors
        "status_online": "#9ece6a",
        "status_offline": "#f7768e",
        "status_away": "#e0af68",
        
        # Border colors
        "border": "#414868",
        "border_focus": "#7aa2f7",
    }
    
    # Font settings
    FONTS = {
        "family": "Segoe UI",
        "size_title": 24,
        "size_heading": 18,
        "size_body": 14,
        "size_small": 12,
        "size_button": 14,
    }
    
    # Spacing
    SPACING = {
        "padding_small": 8,
        "padding_medium": 16,
        "padding_large": 24,
        "corner_radius": 12,
        "button_corner": 8,
    }
    
    def __init__(self):
        self.setup_theme()
    
    def setup_theme(self) -> None:
        """Configure customtkinter theme"""
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
    
    def get_color(self, name: str) -> str:
        """Get a color by name"""
        return self.COLORS.get(name, "#ffffff")
    
    def get_font(self, size_type: str = "body") -> tuple:
        """Get font tuple for a given size type"""
        size = self.FONTS.get(f"size_{size_type}", self.FONTS["size_body"])
        return (self.FONTS["family"], size)
    
    def get_spacing(self, name: str) -> int:
        """Get spacing value by name"""
        return self.SPACING.get(name, 16)
    
    def configure_button(self, button: ctk.CTkButton, style: str = "primary") -> None:
        """Configure button with predefined styles"""
        if style == "primary":
            button.configure(
                fg_color=self.COLORS["accent_primary"],
                hover_color="#5d84d4",
                text_color="#ffffff",
                corner_radius=self.SPACING["button_corner"],
                height=44,
                font=(self.FONTS["family"], self.FONTS["size_button"], "bold")
            )
        elif style == "secondary":
            button.configure(
                fg_color="transparent",
                border_color=self.COLORS["border"],
                border_width=2,
                hover_color=self.COLORS["bg_tertiary"],
                text_color=self.COLORS["text_primary"],
                corner_radius=self.SPACING["button_corner"],
                height=44,
                font=(self.FONTS["family"], self.FONTS["size_button"])
            )
        elif style == "success":
            button.configure(
                fg_color=self.COLORS["accent_success"],
                hover_color="#8bc35a",
                text_color="#ffffff",
                corner_radius=self.SPACING["button_corner"],
                height=44,
                font=(self.FONTS["family"], self.FONTS["size_button"], "bold")
            )
        elif style == "danger":
            button.configure(
                fg_color=self.COLORS["accent_error"],
                hover_color="#d6657a",
                text_color="#ffffff",
                corner_radius=self.SPACING["button_corner"],
                height=44,
                font=(self.FONTS["family"], self.FONTS["size_button"], "bold")
            )
    
    def get_frame_style(self, style: str = "card") -> dict:
        """Get frame styling dictionary"""
        if style == "card":
            return {
                "fg_color": self.COLORS["bg_secondary"],
                "corner_radius": self.SPACING["corner_radius"],
                "border_width": 1,
                "border_color": self.COLORS["border"]
            }
        elif style == "input":
            return {
                "fg_color": self.COLORS["bg_tertiary"],
                "corner_radius": self.SPACING["button_corner"],
                "border_width": 0
            }
        else:
            return {
                "fg_color": "transparent",
                "corner_radius": 0
            }

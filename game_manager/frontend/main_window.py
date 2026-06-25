"""
Main Window - Primary application window for Game Manager
"""

import customtkinter as ctk
from tkinter import messagebox
from typing import Optional, Dict, Any
import threading

from .theme import ThemeManager
from .components import SearchBox, GameCard, StatusIndicator, ProgressBar, ActionButton

# Backend imports
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from backend.integrations import IntegrationManager
from backend.tools_manager import ToolsManager
from backend.game_service import GameService
from backend.status_monitor import StatusMonitor


class MainWindow(ctk.CTk):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        
        self.theme = ThemeManager()
        self.integration_manager = IntegrationManager()
        self.tools_manager = ToolsManager()
        self.game_service = GameService()
        self.status_monitor = StatusMonitor(self.integration_manager)
        
        self.selected_game: Optional[Dict[str, Any]] = None
        self.history = []
        self.missing_tools = []
        
        self._setup_window()
        self._check_dependencies()  # Check dependencies first
        self._setup_ui()
        self._start_status_monitor()
    
    def _check_dependencies(self) -> None:
        """Check for missing dependencies and show installation dialog"""
        tools_status = self.tools_manager.get_all_tools_status()
        
        self.missing_tools = [
            name for name, info in tools_status.items() 
            if not info["installed"]
        ]
        
        if self.missing_tools:
            # Schedule dialog to appear after window is shown
            self.after(500, self._show_missing_tools_dialog)
    
    def _show_missing_tools_dialog(self) -> None:
        """Show dialog for missing tools"""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Ferramentas Necessárias")
        dialog.geometry("500x400")
        dialog.attributes('-topmost', True)
        dialog.transient(self)
        
        # Make dialog modal
        dialog.grab_set()
        
        # Content
        content_frame = ctk.CTkFrame(dialog, fg_color=self.theme.COLORS["bg_primary"])
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        title_label = ctk.CTkLabel(
            content_frame,
            text="⚠️ Ferramentas Necessárias",
            font=(self.theme.FONTS["family"], self.theme.FONTS["size_heading"], "bold"),
            text_color=self.theme.COLORS["text_primary"]
        )
        title_label.pack(pady=(0, 10))
        
        subtitle_label = ctk.CTkLabel(
            content_frame,
            text="As seguintes ferramentas precisam ser instaladas:",
            font=(self.theme.FONTS["family"], self.theme.FONTS["size_body"]),
            text_color=self.theme.COLORS["text_secondary"]
        )
        subtitle_label.pack(pady=(0, 20))
        
        # Tools list with install buttons
        tools_frame = ctk.CTkScrollableFrame(content_frame, fg_color="transparent")
        tools_frame.pack(fill="both", expand=True, pady=(0, 20))
        
        tools_status = self.tools_manager.get_all_tools_status()
        
        for tool_name in self.missing_tools:
            tool_info = tools_status.get(tool_name, {})
            tool_display_name = tool_info.get("name", tool_name.title())
            tool_desc = tool_info.get("description", "")
            
            tool_frame = ctk.CTkFrame(
                tools_frame,
                fg_color=self.theme.COLORS["bg_secondary"],
                corner_radius=self.theme.SPACING["corner_radius"]
            )
            tool_frame.pack(fill="x", pady=10)
            
            info_frame = ctk.CTkFrame(tool_frame, fg_color="transparent")
            info_frame.pack(side="left", fill="both", expand=True, padx=15, pady=15)
            
            name_label = ctk.CTkLabel(
                info_frame,
                text=f"✗ {tool_display_name}",
                font=(self.theme.FONTS["family"], self.theme.FONTS["size_body"], "bold"),
                text_color=self.theme.COLORS["accent_error"]
            )
            name_label.pack(anchor="w")
            
            desc_label = ctk.CTkLabel(
                info_frame,
                text=tool_desc,
                font=(self.theme.FONTS["family"], self.theme.FONTS["size_small"]),
                text_color=self.theme.COLORS["text_secondary"]
            )
            desc_label.pack(anchor="w")
            
            install_btn = ActionButton(
                tool_frame,
                text="Instalar",
                command=lambda t=tool_name, d=dialog: self._install_tool(t, d),
                style="primary",
                width=100
            )
            install_btn.pack(side="right", padx=15, pady=15)
        
        # Continue button
        continue_btn = ActionButton(
            content_frame,
            text="Continuar Mesmo Assim",
            command=dialog.destroy,
            style="secondary"
        )
        continue_btn.pack(fill="x")
    
    def _setup_window(self) -> None:
        """Configure main window properties"""
        self.title("Game Manager")
        self.geometry("1000x700")
        self.minsize(800, 600)
        
        # Configure appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        
        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
    
    def _setup_ui(self) -> None:
        """Setup the main UI"""
        # Main container
        self.main_frame = ctk.CTkFrame(self, fg_color=self.theme.COLORS["bg_primary"])
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=40, pady=40)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        
        # Header
        self._setup_header()
        
        # Content area
        self._setup_content()
        
        # Status panel
        self._setup_status_panel()
    
    def _setup_header(self) -> None:
        """Setup the header section"""
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        
        # Title
        title_label = ctk.CTkLabel(
            header_frame,
            text="Game Manager",
            font=(self.theme.FONTS["family"], self.theme.FONTS["size_title"], "bold"),
            text_color=self.theme.COLORS["text_primary"]
        )
        title_label.pack(side="left")
        
        # Settings button
        settings_btn = ctk.CTkButton(
            header_frame,
            text="⚙️",
            width=40,
            height=40,
            fg_color="transparent",
            hover_color=self.theme.COLORS["bg_tertiary"],
            text_color=self.theme.COLORS["text_secondary"],
            command=self._open_settings
        )
        settings_btn.pack(side="right")
    
    def _setup_content(self) -> None:
        """Setup the main content area"""
        content_frame = ctk.CTkScrollableFrame(
            self.main_frame,
            fg_color="transparent"
        )
        content_frame.grid(row=1, column=0, sticky="nsew")
        content_frame.grid_columnconfigure(0, weight=1)
        
        # Search section
        self._setup_search_section(content_frame)
        
        # Results section (hidden initially)
        self._setup_results_section(content_frame)
        
        # Selected game section (hidden initially)
        self._setup_selected_game_section(content_frame)
        
        # Progress section (hidden initially)
        self._setup_progress_section(content_frame)
        
        # Success section (hidden initially)
        self._setup_success_section(content_frame)
    
    def _setup_search_section(self, parent) -> None:
        """Setup the search section"""
        search_frame = ctk.CTkFrame(parent, fg_color="transparent")
        search_frame.grid(row=0, column=0, sticky="ew", pady=40)
        
        # Main question
        question_label = ctk.CTkLabel(
            search_frame,
            text="Qual jogo deseja adicionar?",
            font=(self.theme.FONTS["family"], self.theme.FONTS["size_heading"]),
            text_color=self.theme.COLORS["text_primary"]
        )
        question_label.pack(pady=(0, 20))
        
        # Search box
        self.search_box = SearchBox(
            search_frame,
            placeholder="Pesquisar jogo...",
            command=self._on_search,
            height=50
        )
        self.search_box.pack(fill="x", pady=(0, 20))
        
        # Select button
        self.select_btn = ActionButton(
            search_frame,
            text="Selecionar Jogo",
            command=self._on_select_game,
            style="secondary"
        )
        self.select_btn.pack(fill="x")
    
    def _setup_results_section(self, parent) -> None:
        """Setup the search results section"""
        self.results_frame = ctk.CTkFrame(parent, fg_color="transparent")
        self.results_frame.grid(row=1, column=0, sticky="ew", pady=20)
        self.results_frame.grid_columnconfigure(0, weight=1)
        
        self.results_label = ctk.CTkLabel(
            self.results_frame,
            text="Resultados da pesquisa:",
            font=(self.theme.FONTS["family"], self.theme.FONTS["size_body"]),
            text_color=self.theme.COLORS["text_secondary"]
        )
        self.results_label.pack(anchor="w", pady=(0, 10))
        
        self.results_container = ctk.CTkFrame(self.results_frame, fg_color="transparent")
        self.results_container.pack(fill="x")
        
        # Hide initially
        self.results_frame.grid_remove()
    
    def _setup_selected_game_section(self, parent) -> None:
        """Setup the selected game display section"""
        self.selected_frame = ctk.CTkFrame(parent, fg_color="transparent")
        self.selected_frame.grid(row=2, column=0, sticky="ew", pady=20)
        
        # Game info card
        self.selected_card = ctk.CTkFrame(
            self.selected_frame,
            fg_color=self.theme.COLORS["bg_secondary"],
            corner_radius=self.theme.SPACING["corner_radius"]
        )
        self.selected_card.pack(fill="x", pady=(0, 20))
        
        # Cover placeholder
        cover_frame = ctk.CTkFrame(
            self.selected_card,
            fg_color=self.theme.COLORS["bg_tertiary"],
            corner_radius=8,
            height=150
        )
        cover_frame.pack(fill="x", padx=20, pady=20)
        
        self.cover_icon = ctk.CTkLabel(
            cover_frame,
            text="🎮",
            font=(self.theme.FONTS["family"], 64),
            text_color=self.theme.COLORS["text_muted"]
        )
        self.cover_icon.place(relx=0.5, rely=0.5, anchor="center")
        
        # Game details
        details_frame = ctk.CTkFrame(self.selected_card, fg_color="transparent")
        details_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        self.selected_name = ctk.CTkLabel(
            details_frame,
            text="",
            font=(self.theme.FONTS["family"], self.theme.FONTS["size_heading"], "bold"),
            text_color=self.theme.COLORS["text_primary"]
        )
        self.selected_name.pack(anchor="w", pady=(0, 8))
        
        self.selected_info = ctk.CTkLabel(
            details_frame,
            text="",
            font=(self.theme.FONTS["family"], self.theme.FONTS["size_small"]),
            text_color=self.theme.COLORS["text_secondary"]
        )
        self.selected_info.pack(anchor="w")
        
        # Status badge
        self.status_badge = ctk.CTkLabel(
            details_frame,
            text="✓ Selecionado",
            font=(self.theme.FONTS["family"], self.theme.FONTS["size_small"]),
            text_color=self.theme.COLORS["accent_success"]
        )
        self.status_badge.pack(anchor="w", pady=(8, 0))
        
        # Add to library button
        self.add_btn = ActionButton(
            self.selected_frame,
            text="Adicionar à Biblioteca",
            command=self._on_add_to_library,
            style="primary"
        )
        self.add_btn.pack(fill="x", pady=(10, 0))
        
        # Hide initially
        self.selected_frame.grid_remove()
    
    def _setup_progress_section(self, parent) -> None:
        """Setup the progress section"""
        self.progress_frame = ctk.CTkFrame(parent, fg_color="transparent")
        self.progress_frame.grid(row=3, column=0, sticky="ew", pady=20)
        
        # Progress label
        self.progress_label = ctk.CTkLabel(
            self.progress_frame,
            text="Processando...",
            font=(self.theme.FONTS["family"], self.theme.FONTS["size_body"]),
            text_color=self.theme.COLORS["text_primary"]
        )
        self.progress_label.pack(pady=(0, 10))
        
        # Progress bar
        self.progress_bar = ProgressBar(self.progress_frame, width=400)
        self.progress_bar.pack(pady=(0, 10))
        self.progress_bar.set(0)
        
        # Progress text
        self.progress_text = ctk.CTkLabel(
            self.progress_frame,
            text="",
            font=(self.theme.FONTS["family"], self.theme.FONTS["size_small"]),
            text_color=self.theme.COLORS["text_secondary"]
        )
        self.progress_text.pack()
        
        # Hide initially
        self.progress_frame.grid_remove()
    
    def _setup_success_section(self, parent) -> None:
        """Setup the success section"""
        self.success_frame = ctk.CTkFrame(parent, fg_color="transparent")
        self.success_frame.grid(row=4, column=0, sticky="ew", pady=20)
        
        # Success icon
        success_icon = ctk.CTkLabel(
            self.success_frame,
            text="✓",
            font=(self.theme.FONTS["family"], 48),
            text_color=self.theme.COLORS["accent_success"]
        )
        success_icon.pack(pady=(0, 10))
        
        # Success message
        success_msg = ctk.CTkLabel(
            self.success_frame,
            text="Operação concluída com sucesso.",
            font=(self.theme.FONTS["family"], self.theme.FONTS["size_heading"]),
            text_color=self.theme.COLORS["text_primary"]
        )
        success_msg.pack(pady=(0, 20))
        
        # Action buttons
        btn_frame = ctk.CTkFrame(self.success_frame, fg_color="transparent")
        btn_frame.pack()
        
        self.restart_btn = ActionButton(
            btn_frame,
            text="Reiniciar Steam",
            command=self._on_restart_steam,
            style="success"
        )
        self.restart_btn.pack(side="left", padx=(0, 10))
        
        self.later_btn = ActionButton(
            btn_frame,
            text="Fazer Depois",
            command=self._on_later,
            style="secondary"
        )
        self.later_btn.pack(side="left")
        
        # Hide initially
        self.success_frame.grid_remove()
    
    def _setup_status_panel(self) -> None:
        """Setup the status panel at the bottom"""
        status_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        status_frame.grid(row=2, column=0, sticky="ew", pady=(20, 0))
        
        # Status indicators
        self.steam_status = StatusIndicator(status_frame, "Steam", True)
        self.steam_status.pack(side="left", padx=(0, 20))
        
        self.lua_status = StatusIndicator(status_frame, "Integração 1", True)
        self.lua_status.pack(side="left", padx=(0, 20))
        
        self.integration2_status = StatusIndicator(status_frame, "Integração 2", True)
        self.integration2_status.pack(side="left")
        
        # History toggle
        history_btn = ctk.CTkButton(
            status_frame,
            text="📜 Histórico",
            width=100,
            height=30,
            fg_color=self.theme.COLORS["bg_tertiary"],
            hover_color=self.theme.COLORS["border"],
            text_color=self.theme.COLORS["text_secondary"],
            font=(self.theme.FONTS["family"], self.theme.FONTS["size_small"]),
            command=self._toggle_history
        )
        history_btn.pack(side="right")
    
    def _start_status_monitor(self) -> None:
        """Start the status monitoring system"""
        self.status_monitor.add_callback(self._on_status_update)
        self.status_monitor.start()
    
    def _on_status_update(self, status: Dict[str, Any]) -> None:
        """Handle status updates from monitor"""
        try:
            integrations = status.get("integrations", [])
            for integration in integrations:
                name = integration.get("name", "").lower()
                is_online = integration.get("online", False)
                
                if "steam" in name:
                    self.after(0, lambda o=is_online: self.steam_status.update_status(o))
                elif "lua" in name:
                    self.after(0, lambda o=is_online: self.lua_status.update_status(o))
        except Exception:
            pass
    
    def _on_search(self, query: str) -> None:
        """Handle search action"""
        # Show results frame
        self.results_frame.grid()
        
        # Clear previous results
        for widget in self.results_container.winfo_children():
            widget.destroy()
        
        # Search for games
        games = self.game_service.search_games(query)
        
        # Display results
        for game in games:
            card = GameCard(
                self.results_container,
                game_data=game,
                on_select=self._on_game_select
            )
            card.pack(fill="x", pady=5)
    
    def _on_game_select(self, game: Dict[str, Any], is_selected: bool) -> None:
        """Handle game selection from results"""
        if is_selected:
            # Deselect other cards
            for widget in self.results_container.winfo_children():
                if hasattr(widget, 'game_data') and widget.game_data != game:
                    widget.is_selected = False
                    widget._update_appearance()
            
            self.selected_game = game
            self._show_selected_game()
    
    def _show_selected_game(self) -> None:
        """Show the selected game section"""
        if not self.selected_game:
            return
        
        # Update selected game info
        game = self.selected_game
        self.selected_name.configure(text=game.get("name", "Unknown"))
        
        genres = game.get("genres", [])
        rating = game.get("rating", 0)
        self.selected_info.configure(
            text=f"{' • '.join(genres)} | ★ {rating}"
        )
        
        # Hide results, show selected
        self.results_frame.grid_remove()
        self.search_box.pack_forget()
        self.select_btn.pack_forget()
        
        self.selected_frame.grid()
    
    def _on_select_game(self) -> None:
        """Handle select game button click"""
        query = self.search_box.get()
        if query:
            self._on_search(query)
    
    def _on_add_to_library(self) -> None:
        """Handle add to library action"""
        if not self.selected_game:
            return
        
        # Hide selected frame, show progress
        self.selected_frame.grid_remove()
        self.progress_frame.grid()
        
        # Run addition in background thread
        thread = threading.Thread(target=self._add_game_thread, daemon=True)
        thread.start()
    
    def _add_game_thread(self) -> None:
        """Background thread for adding game to library"""
        def update_progress(progress: int, message: str):
            self.after(0, lambda: self._update_progress(progress, message))
        
        result = self.game_service.add_to_library(self.selected_game, update_progress)
        
        # Add to history
        self.history.append({
            "game": self.selected_game.get("name", "Unknown"),
            "success": result.get("success", False),
            "timestamp": result.get("timestamp", "")
        })
        
        # Show success or error
        if result.get("success"):
            self.after(0, self._show_success)
        else:
            self.after(0, lambda: self._show_error(result.get("error", "Unknown error")))
    
    def _update_progress(self, progress: int, message: str) -> None:
        """Update progress UI"""
        self.progress_bar.set(progress / 100.0)
        self.progress_text.configure(text=message)
    
    def _show_success(self) -> None:
        """Show success screen"""
        self.progress_frame.grid_remove()
        self.success_frame.grid()
    
    def _show_error(self, error: str) -> None:
        """Show error message"""
        self.progress_frame.grid_remove()
        self.selected_frame.grid()
        
        messagebox.showerror("Erro", f"Falha ao adicionar jogo:\n{error}")
    
    def _on_restart_steam(self) -> None:
        """Handle restart Steam action"""
        success = self.integration_manager.steam.restart()
        
        if success:
            self._add_history_entry("Steam reiniciado", True)
            self._reset_to_search()
        else:
            messagebox.showwarning(
                "Aviso",
                "Não foi possível reiniciar Steam automaticamente.\nPor favor, reinicie manualmente."
            )
    
    def _on_later(self) -> None:
        """Handle do later action"""
        self._add_history_entry("Operação concluída (Steam não reiniciada)", True)
        self._reset_to_search()
    
    def _reset_to_search(self) -> None:
        """Reset UI to initial search state"""
        self.success_frame.grid_remove()
        
        # Show search again
        self.search_box.pack(fill="x", pady=(0, 20))
        self.select_btn.pack(fill="x")
        self.search_box.clear()
        
        self.selected_game = None
    
    def _toggle_history(self) -> None:
        """Toggle history panel"""
        # Create or show history popup
        history_window = ctk.CTkToplevel(self)
        history_window.title("Histórico")
        history_window.geometry("400x300")
        history_window.attributes('-topmost', True)
        
        # History list
        scroll_frame = ctk.CTkScrollableFrame(history_window)
        scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        if not self.history:
            label = ctk.CTkLabel(
                scroll_frame,
                text="Nenhuma operação registrada",
                text_color=self.theme.COLORS["text_muted"]
            )
            label.pack(pady=20)
        else:
            for entry in reversed(self.history[-10:]):  # Last 10 entries
                status_icon = "✓" if entry.get("success") else "✗"
                status_color = self.theme.COLORS["accent_success"] if entry.get("success") \
                              else self.theme.COLORS["accent_error"]
                
                frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
                frame.pack(fill="x", pady=5)
                
                ctk.CTkLabel(
                    frame,
                    text=status_icon,
                    text_color=status_color,
                    font=(self.theme.FONTS["family"], 14, "bold")
                ).pack(side="left", padx=(0, 10))
                
                ctk.CTkLabel(
                    frame,
                    text=f"{entry.get('game', 'Operação')} - {entry.get('timestamp', '')[:19]}",
                    text_color=self.theme.COLORS["text_secondary"],
                    font=(self.theme.FONTS["family"], self.theme.FONTS["size_small"])
                ).pack(side="left")
    
    def _add_history_entry(self, message: str, success: bool) -> None:
        """Add entry to history"""
        from datetime import datetime
        self.history.append({
            "game": message,
            "success": success,
            "timestamp": datetime.now().isoformat()
        })
    
    def _open_settings(self) -> None:
        """Open settings window"""
        settings_window = ctk.CTkToplevel(self)
        settings_window.title("Configurações")
        settings_window.geometry("500x400")
        settings_window.attributes('-topmost', True)
        
        # Tabs
        tab_view = ctk.CTkTabview(settings_window)
        tab_view.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Preferences tab
        pref_tab = tab_view.add("Preferências")
        ctk.CTkLabel(
            pref_tab,
            text="Preferências da Aplicação",
            font=(self.theme.FONTS["family"], self.theme.FONTS["size_heading"], "bold")
        ).pack(pady=20)
        
        # Startup option
        startup_switch = ctk.CTkSwitch(
            pref_tab,
            text="Iniciar com o sistema",
            font=(self.theme.FONTS["family"], self.theme.FONTS["size_body"])
        )
        startup_switch.pack(pady=10, anchor="w", padx=20)
        
        # Tools tab
        tools_tab = tab_view.add("Ferramentas")
        ctk.CTkLabel(
            tools_tab,
            text="Gerenciamento de Ferramentas",
            font=(self.theme.FONTS["family"], self.theme.FONTS["size_heading"], "bold")
        ).pack(pady=20)
        
        # Check tools status
        tools_status = self.tools_manager.get_all_tools_status()
        
        for tool_key, tool_info in tools_status.items():
            tool_frame = ctk.CTkFrame(tools_tab, fg_color=self.theme.COLORS["bg_secondary"])
            tool_frame.pack(fill="x", padx=20, pady=10)
            
            ctk.CTkLabel(
                tool_frame,
                text=tool_info["name"],
                font=(self.theme.FONTS["family"], self.theme.FONTS["size_body"], "bold"),
                text_color=self.theme.COLORS["text_primary"]
            ).pack(anchor="w", padx=15, pady=(15, 5))
            
            ctk.CTkLabel(
                tool_frame,
                text=tool_info["description"],
                font=(self.theme.FONTS["family"], self.theme.FONTS["size_small"]),
                text_color=self.theme.COLORS["text_secondary"]
            ).pack(anchor="w", padx=15, pady=(0, 10))
            
            status_text = "✓ Instalado" if tool_info["installed"] else "✗ Não instalado"
            status_color = self.theme.COLORS["accent_success"] if tool_info["installed"] \
                          else self.theme.COLORS["accent_error"]
            
            ctk.CTkLabel(
                tool_frame,
                text=status_text,
                font=(self.theme.FONTS["family"], self.theme.FONTS["size_small"]),
                text_color=status_color
            ).pack(anchor="w", padx=15, pady=(0, 15))
            
            if not tool_info["installed"]:
                install_btn = ctk.CTkButton(
                    tool_frame,
                    text="Instalar",
                    command=lambda t=tool_key: self._install_tool(t, tool_frame),
                    height=32
                )
                install_btn.pack(anchor="w", padx=15, pady=(0, 15))
        
        # Logs tab
        logs_tab = tab_view.add("Logs")
        log_text = ctk.CTkTextbox(logs_tab, state="disabled")
        log_text.pack(fill="both", expand=True, padx=20, pady=20)
        
        log_text.insert("0.0", "Log do sistema...\n")
        log_text.insert("end", "Inicialização completa\n")
        log_text.insert("end", "Status monitor iniciado\n")
    
    def _install_tool(self, tool_key: str, parent_frame=None) -> None:
        """Handle tool installation with progress dialog"""
        # Create progress dialog
        progress_dialog = ctk.CTkToplevel(self)
        progress_dialog.title(f"Instalando {tool_key.title()}")
        progress_dialog.geometry("400x200")
        progress_dialog.attributes('-topmost', True)
        progress_dialog.transient(self)
        
        content_frame = ctk.CTkFrame(progress_dialog, fg_color=self.theme.COLORS["bg_primary"])
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        title_label = ctk.CTkLabel(
            content_frame,
            text=f"Instalando {tool_key.title()}...",
            font=(self.theme.FONTS["family"], self.theme.FONTS["size_body"], "bold"),
            text_color=self.theme.COLORS["text_primary"]
        )
        title_label.pack(pady=(0, 15))
        
        progress_bar = ProgressBar(content_frame, width=300)
        progress_bar.pack(pady=(0, 10))
        progress_bar.set(0)
        
        status_label = ctk.CTkLabel(
            content_frame,
            text="Iniciando instalação...",
            font=(self.theme.FONTS["family"], self.theme.FONTS["size_small"]),
            text_color=self.theme.COLORS["text_secondary"]
        )
        status_label.pack()
        
        def update_progress(progress: int, message: str):
            progress_bar.set(progress / 100.0)
            status_label.configure(text=message)
        
        def install_thread():
            result = self.tools_manager.install_tool(tool_key, update_progress)
            
            # Close dialog and show result
            progress_dialog.after(0, progress_dialog.destroy)
            
            if result.get("success"):
                if result.get("manual_install"):
                    self.after(100, lambda: messagebox.showinfo(
                        "Instalação",
                        result.get("message", "Por favor, complete a instalação manualmente.")
                    ))
                else:
                    self.after(100, lambda: messagebox.showinfo(
                        "Instalação", 
                        "Ferramenta instalada com sucesso!"
                    ))
                # Refresh tools status if in settings
                if parent_frame and hasattr(parent_frame, 'winfo_exists') and parent_frame.winfo_exists():
                    self.after(500, self._refresh_tools_tab)
            else:
                self.after(100, lambda: messagebox.showerror(
                    "Erro",
                    result.get("error", "Falha na instalação")
                ))
        
        thread = threading.Thread(target=install_thread, daemon=True)
        thread.start()
    
    def _refresh_tools_tab(self) -> None:
        """Refresh the tools tab in settings"""
        # This will be called after installation to refresh status
        pass


def run_app():
    """Run the application"""
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    run_app()

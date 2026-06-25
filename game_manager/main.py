"""
Game Manager - Main Entry Point
A modern, professional desktop application for game management.
"""

import sys
import os

# Add the parent directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from frontend.main_window import run_app


def main():
    """Main entry point for the Game Manager application"""
    # Hide console window on Windows unless there's an error
    if sys.platform == 'win32':
        try:
            import ctypes
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
        except Exception:
            pass
    
    try:
        run_app()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        # Show console and error if something goes wrong
        if sys.platform == 'win32':
            try:
                import ctypes
                ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
            except Exception:
                pass
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        input("Press Enter to exit...")
        sys.exit(1)


if __name__ == "__main__":
    main()

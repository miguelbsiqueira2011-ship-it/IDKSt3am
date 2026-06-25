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
    print("Starting Game Manager...")
    print("=" * 50)
    print("Game Manager v1.0.0")
    print("A modern game management solution")
    print("=" * 50)
    
    try:
        run_app()
    except KeyboardInterrupt:
        print("\nApplication closed by user.")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

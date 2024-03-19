"""Run the game."""

import arcade

from .constants import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH
from .game import GameWindow


def main():
    """Main function"""
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

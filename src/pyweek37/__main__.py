"""
Example of Pymunk Physics Engine Platformer
"""
import arcade

from .game import GameWindow
from .constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE


def main():
    """ Main function """
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

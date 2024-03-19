import arcade

from ..constants import SPRITE_SCALING_PLAYER


class PlayerSprite(arcade.Sprite):
    """Player Sprite"""

    def __init__(self):
        """Init"""
        super().__init__()

        self.scale = SPRITE_SCALING_PLAYER

    def pymunk_moved(self, physics_engine, dx, dy, d_angle):
        """Handle being moved by the pymunk engine"""

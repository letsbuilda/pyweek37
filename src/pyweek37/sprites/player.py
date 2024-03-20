"""Player Sprite"""

import math

import arcade

from ..constants import ASSETS_DIR, SPRITE_SCALING_PLAYER


class PlayerSprite(arcade.Sprite):
    """Player Sprite"""

    def __init__(self, *args, **kwargs):
        """Init"""
        super().__init__(*args, **kwargs)

        self.scale = SPRITE_SCALING_PLAYER

    def point_to(self, x, y):
        """Point to a location"""

        offset = 210  # cannon is off
        angle = math.degrees(math.atan2(y - self.center_y, x - self.center_x))
        self.angle = angle + offset

    def update(self):
        """Update"""

"""Target Sprite"""

import arcade

from ..constants import SPRITE_SCALING_TARGET


class TargetSprite(arcade.Sprite):
    """Target Sprite"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scale = SPRITE_SCALING_TARGET

    def bullet_hit_handler(self, _bullet_sprite, _arbiter, _space, _data):
        """Called for bullet/target collision"""

        self.remove_from_sprite_lists()

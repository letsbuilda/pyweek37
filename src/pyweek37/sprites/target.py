import arcade
from ..constants import SPRITE_SCALING_TARGET


class TargetSprite(arcade.Sprite):
    """Target Sprite"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scale = SPRITE_SCALING_TARGET
    def hit_handler(self):
        self.remove_from_sprite_lists()

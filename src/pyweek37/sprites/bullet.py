"""Bullet Sprite"""

import arcade


class BulletSprite(arcade.SpriteSolidColor):
    """Bullet Sprite"""

    def pymunk_moved(self, physics_engine, dx, dy, d_angle):
        """Handle when the sprite is moved by the physics engine."""
        # If the bullet falls below the screen, remove it
        if self.center_y < -100:
            self.remove_from_sprite_lists()

    def wall_hit_handler(self, _wall_sprite, _arbiter, _space, _data):
        """Called for bullet/wall collision"""

        self.remove_from_sprite_lists()
    def target_hit_handler(self):
        """Called for bullet/target collision"""
        self.remove_from_sprite_lists()
        

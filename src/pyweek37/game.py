"""The main game window"""

import math
from typing import Optional

import arcade

from .constants import (
    ASSETS_DIR,
    BULLET_GRAVITY,
    BULLET_MASS,
    BULLET_MOVE_FORCE,
    DEFAULT_DAMPING,
    GRAVITY,
    PLAYER_FRICTION,
    PLAYER_MASS,
    PLAYER_MAX_HORIZONTAL_SPEED,
    PLAYER_MAX_VERTICAL_SPEED,
    SPRITE_SCALING_TILES,
    WALL_FRICTION,
)
from .sprites.bullet import BulletSprite
from .sprites.player import PlayerSprite


class GameWindow(arcade.Window):
    """Main Window"""

    def __init__(self, width, height, title):
        """Create the variables"""

        super().__init__(width, height, title)

        self.player_sprite: Optional[PlayerSprite] = None
        self.scene = None
        self.physics_engine: Optional[arcade.PymunkPhysicsEngine] = None

        arcade.set_background_color(arcade.color.BLUE)

    def setup(self):
        """Set up everything with the game"""

        self.scene = arcade.Scene()
        self.scene.add_sprite_list("player")
        self.scene.add_sprite_list("bullet")

        map_file = ASSETS_DIR / "tiled" / "map.tmx"
        tile_map = arcade.load_tilemap(map_file, SPRITE_SCALING_TILES)

        self.scene.add_sprite_list(
            "blocks", sprite_list=tile_map.sprite_lists["Blocks"]
        )
        self.scene.add_sprite("player", tile_map.sprite_lists["Entities"][0])
        self.player_sprite = self.scene.get_sprite_list("player")[0]

        self.physics_engine = arcade.PymunkPhysicsEngine(
            damping=DEFAULT_DAMPING, gravity=(0, -GRAVITY)
        )

        self.physics_engine.add_collision_handler(
            "bullet", "wall", post_handler=BulletSprite.wall_hit_handler
        )

        self.physics_engine.add_sprite(
            self.player_sprite,
            friction=PLAYER_FRICTION,
            mass=PLAYER_MASS,
            moment=arcade.PymunkPhysicsEngine.MOMENT_INF,
            collision_type="player",
            max_horizontal_velocity=PLAYER_MAX_HORIZONTAL_SPEED,
            max_vertical_velocity=PLAYER_MAX_VERTICAL_SPEED,
        )

        self.physics_engine.add_sprite_list(
            self.scene.get_sprite_list("blocks"),
            friction=WALL_FRICTION,
            collision_type="wall",
            body_type=arcade.PymunkPhysicsEngine.STATIC,
        )

    def on_mouse_press(self, x, y, button, modifiers):
        """User clicks mouse"""

        if button == arcade.MOUSE_BUTTON_LEFT:
            self.shoot_bullet(x, y)

    def shoot_bullet(self, x, y):
        """Shoot a bullet"""

        bullet = BulletSprite(20, 5, arcade.color.DARK_YELLOW)
        self.scene.add_sprite("bullet", bullet)
        bullet.position = self.player_sprite.position

        x_diff = x - self.player_sprite.center_x
        y_diff = y - self.player_sprite.center_y
        angle = math.atan2(y_diff, x_diff)
        size = max(self.player_sprite.width, self.player_sprite.height) / 2

        bullet.center_x += size * math.cos(angle)
        bullet.center_y += size * math.sin(angle)
        bullet.angle = math.degrees(angle)

        self.physics_engine.add_sprite(
            bullet,
            mass=BULLET_MASS,
            damping=1.0,
            friction=0.6,
            collision_type="bullet",
            gravity=(0, -BULLET_GRAVITY),
            elasticity=0.9,
        )

        force = (BULLET_MOVE_FORCE, 0)
        self.physics_engine.apply_force(bullet, force)

    def on_update(self, delta_time):
        """Movement and game logic"""

        self.physics_engine.step()

    def on_draw(self):
        """Draw everything"""

        self.clear()

        self.scene.draw()

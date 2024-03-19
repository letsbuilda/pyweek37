import arcade

from typing import Optional
import math

from .constants import *
from .sprites.bullet import BulletSprite
from .sprites.player import PlayerSprite


class GameWindow(arcade.Window):
    """ Main Window """

    def __init__(self, width, height, title):
        """ Create the variables """

        super().__init__(width, height, title)

        self.player_sprite: Optional[PlayerSprite] = None

        self.player_list: Optional[arcade.SpriteList] = None
        self.wall_list: Optional[arcade.SpriteList] = None
        self.bullet_list: Optional[arcade.SpriteList] = None
        self.item_list: Optional[arcade.SpriteList] = None
        self.moving_sprites_list: Optional[arcade.SpriteList] = None

        self.left_pressed: bool = False
        self.right_pressed: bool = False
        self.up_pressed: bool = False
        self.down_pressed: bool = False

        self.physics_engine: Optional[arcade.PymunkPhysicsEngine] = None

        arcade.set_background_color(arcade.color.BLUE)

    def setup(self):
        """ Set up everything with the game """

        self.player_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        map_file = ASSETS_DIR / "tiled" / "map.tmx"
        tile_map = arcade.load_tilemap(map_file, SPRITE_SCALING_TILES)

        self.wall_list = tile_map.sprite_lists["Blocks"]
        self.player_sprite = tile_map.sprite_lists["Entities"][0]

        self.player_list.append(self.player_sprite)

        damping = DEFAULT_DAMPING
        gravity = (0, -GRAVITY)
        self.physics_engine = arcade.PymunkPhysicsEngine(damping=damping, gravity=gravity)

        def wall_hit_handler(bullet_sprite, _wall_sprite, _arbiter, _space, _data):
            """ Called for bullet/wall collision """
            bullet_sprite.remove_from_sprite_lists()

        self.physics_engine.add_collision_handler("bullet", "wall", post_handler=wall_hit_handler)

        def item_hit_handler(bullet_sprite, item_sprite, _arbiter, _space, _data):
            """ Called for bullet/wall collision """
            bullet_sprite.remove_from_sprite_lists()
            item_sprite.remove_from_sprite_lists()

        self.physics_engine.add_collision_handler("bullet", "item", post_handler=item_hit_handler)

        self.physics_engine.add_sprite(self.player_sprite,
                                       friction=PLAYER_FRICTION,
                                       mass=PLAYER_MASS,
                                       moment=arcade.PymunkPhysicsEngine.MOMENT_INF,
                                       collision_type="player",
                                       max_horizontal_velocity=PLAYER_MAX_HORIZONTAL_SPEED,
                                       max_vertical_velocity=PLAYER_MAX_VERTICAL_SPEED)

        self.physics_engine.add_sprite_list(self.wall_list,
                                            friction=WALL_FRICTION,
                                            collision_type="wall",
                                            body_type=arcade.PymunkPhysicsEngine.STATIC)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
        elif key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
        elif key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called whenever the mouse button is clicked. """

        bullet = BulletSprite(20, 5, arcade.color.DARK_YELLOW)
        self.bullet_list.append(bullet)

        start_x = self.player_sprite.center_x
        start_y = self.player_sprite.center_y
        bullet.position = self.player_sprite.position

        dest_x = x
        dest_y = y

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        size = max(self.player_sprite.width, self.player_sprite.height) / 2

        bullet.center_x += size * math.cos(angle)
        bullet.center_y += size * math.sin(angle)

        bullet.angle = math.degrees(angle)
        bullet_gravity = (0, -BULLET_GRAVITY)

        self.physics_engine.add_sprite(bullet,
                                       mass=BULLET_MASS,
                                       damping=1.0,
                                       friction=0.6,
                                       collision_type="bullet",
                                       gravity=bullet_gravity,
                                       elasticity=0.9)

        force = (BULLET_MOVE_FORCE, 0)
        self.physics_engine.apply_force(bullet, force)

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Update the player
        self.physics_engine.step()

    def on_draw(self):
        """ Draw everything """
        self.clear()
        self.wall_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()

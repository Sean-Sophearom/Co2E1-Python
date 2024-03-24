from __future__ import annotations
from dataclasses import dataclass
from .constant import GAMESTATUS, TARGET_FPS, pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .sprites import Player, Snackbar

__all__ = ["GameState"]

@dataclass
class GameState:
    player: Player
    player_health: float
    player_max_health: float
    player_regen: float

    gem_radius: float
    gem_collected: float
    gem_capacity: float

    gem_value_multiplier: float

    player_damage_multiplier: float
    player_defense_multiplier: float    

    enemy_speed_multiplier: float
    enemy_health_multiplier: float
    enemy_damage_multiplier: float
    enemy_value_multiplier: float

    snackbar: Snackbar

    sprite_timer: SpriteTimer
    sprite_speed: SpriteSpeed
    sprite_damage: SpriteDamage
    sprite_health: SpriteHealth
    sprite_value: SpriteValue

    delta_time: float = 0
    delta_frame: float = 0
    _getTicksLastFrame: float = 0

    game_status: GAMESTATUS = GAMESTATUS.HOME

    @staticmethod
    def change_status(status: GAMESTATUS):
        GameState.game_status = status
        
    @staticmethod
    def is_playing():
        return GameState.game_status == GAMESTATUS.PLAYING
    
    @staticmethod
    def is_home():
        return GameState.game_status == GAMESTATUS.HOME
    
    @staticmethod
    def is_game_over():
        return GameState.game_status == GAMESTATUS.GAME_OVER
    
    @staticmethod
    def is_skill_menu():
        return GameState.game_status == GAMESTATUS.SKILL_MENU

    @staticmethod
    def update_delta_time():
        ticks = pygame.time.get_ticks()
        GameState.delta_time = (ticks - GameState._getTicksLastFrame) / 1000.0
        GameState.delta_frame = GameState.delta_time * TARGET_FPS
        GameState._getTicksLastFrame = ticks
    
    @staticmethod
    def reset():
        GameState.player = None
        GameState.player_health = 100
        GameState.player_max_health = 100
        GameState.player_regen = 1

        GameState.gem_radius = 200
        GameState.gem_collected = 0
        GameState.gem_capacity = 3

        GameState.gem_value_multiplier = 1

        GameState.player_damage_multiplier = 1
        GameState.player_defense_multiplier = 1    

        GameState.enemy_speed_multiplier = 1
        GameState.enemy_health_multiplier = 1
        GameState.enemy_damage_multiplier = 1
        GameState.enemy_value_multiplier = 1

        GameState.sprite_speed = SpriteSpeed()
        GameState.sprite_timer = SpriteTimer()
        GameState.sprite_damage = SpriteDamage()
        GameState.sprite_health = SpriteHealth()
        GameState.sprite_value = SpriteValue()

        if not hasattr(GameState, "snackbar") or GameState.snackbar is None:
            from .sprites import Snackbar
            GameState.snackbar = Snackbar()

        if not hasattr(GameState, "damage_splash_screen") or GameState.damage_splash_screen is None:
            from .sprites import DamageSplashScreen
            GameState.damage_splash_screen = DamageSplashScreen()
    
class DynamicDataclass:
    def __getitem__(self, key):
        return getattr(self, str(key))
    
    def __setitem__(self, key, value):
        setattr(self, str(key), value)

@dataclass
class SpriteSpeed(DynamicDataclass):
    player: float = 5
    gem: float = 9

    bullet: float = 9
    lightning: float = 9
    fire_ball: float = 9
    fire_ring: float = 9
    flame_ball: float = 9
    magic_arrow: float = 9
    magic_orb: float = 9
    thunder_ball: float = 9
    
    enemy: float = 2
    bat: float = 4
    canine_gray: float = 3
    canine_white: float = 3
    golem: float = 1
    rat: float = 2
    skull: float = 2
    slime: float = 2

@dataclass
class SpriteTimer(DynamicDataclass):
    regen: int = 2000

    bullet: int = 1000
    lightning: int = 1000
    fire_ball: int = 1000
    fire_ring: int = 1000
    flame_ball: int = 1000
    magic_arrow: int = 1000
    magic_orb: int = 1000
    thunder_ball: int = 1000
    
    enemy: int = 1000
    bat: int = 1000
    canine_gray: int = 1000
    canine_white: int = 1000
    golem: int = 1000
    rat: int = 1000
    skull: int = 1000
    slime: int = 1000

@dataclass 
class SpriteDamage(DynamicDataclass):
    bullet: float = 5
    lightning: float = 999
    fire_ball: float = 5
    fire_ring: float = 5 
    flame_ball: float = 5
    magic_arrow: float = 5
    magic_orb: float = 5
    thunder_ball: float = 5
    
    enemy: float = 5
    bat: float = 5
    canine_gray: float = 8
    canine_white: float = 8
    golem: float = 10
    rat: float = 4
    skull: float = 5
    slime: float = 5

@dataclass
class SpriteHealth(DynamicDataclass):
    enemy: float = 10
    bat: float = 4
    canine_gray: float = 5
    canine_white: float = 5
    golem: float = 10
    rat: float = 4
    skull: float = 4
    slime: float = 4

@dataclass
class SpriteValue(DynamicDataclass):
    enemy: float = 1.5
    bat: float = 1
    canine_gray: float = 3
    canine_white: float = 3
    golem: float = 5
    rat: float = 1
    skull: float = 1
    slime: float = 1
    
del dataclass

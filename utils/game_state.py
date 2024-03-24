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
    player_speed: float

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
    projectile_level: ProjectileLevel
    
    max_enemies_cap: float = 100

    delta_time: float = 0
    delta_frame: float = 0
    _getTicksLastFrame: float = 0
    time_snapshot: float = 0
    current_level_play_time: float = 0
    death_time_snapshot: float = 0

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
        GameState.current_level_play_time = ticks - GameState.time_snapshot
    
    @staticmethod
    def reset():
        GameState.player = None
        GameState.player_health = 150
        GameState.player_max_health = 150
        GameState.player_regen = 1
        GameState.player_speed = 4.5

        GameState.gem_radius = 200
        GameState.gem_collected = 0
        GameState.gem_capacity = 6

        GameState.gem_value_multiplier = 1.2

        GameState.player_damage_multiplier = 1.5
        GameState.player_defense_multiplier = 1    

        GameState.enemy_speed_multiplier = 1.2
        GameState.enemy_health_multiplier = 1
        GameState.enemy_damage_multiplier = 1
        GameState.enemy_value_multiplier = 1

        GameState.sprite_speed = SpriteSpeed()
        GameState.sprite_timer = SpriteTimer()
        GameState.sprite_damage = SpriteDamage()
        GameState.sprite_health = SpriteHealth()
        GameState.sprite_value = SpriteValue()
        GameState.projectile_level = ProjectileLevel()

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
    gem: float = 9

    bullet: float = 14
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

    bullet: int = 1500
    lightning: int = 10000
    fire_ball: int = 4500
    fire_ring: int = 4000
    flame_ball: int = 3800
    magic_arrow: int = 3500
    magic_orb: int = 3400
    thunder_ball: int = 4200
    
    enemy: int = int(900 * 0.85)
    bat: int = int(800 * 0.85)
    canine_gray: int = int(1200 * 0.85)
    canine_white: int = int(1200 * 0.85)
    golem: int = int(1500 * 0.85)
    rat: int = int(800 * 0.85)
    skull: int = int(910 * 0.85)
    slime: int = int(940 * 0.85)

@dataclass 
class SpriteDamage(DynamicDataclass):
    bullet: float = 6.2
    lightning: float = 999
    fire_ball: float = 5 * 3
    fire_ring: float = 5 * 2.5
    flame_ball: float = 5 * 2.4
    magic_arrow: float = 5 * 2.2
    magic_orb: float = 5 * 2.1
    thunder_ball: float = 5 * 2.7
    
    enemy: float = 5
    bat: float = 6
    canine_gray: float = 10
    canine_white: float = 10
    golem: float = 15
    rat: float = 5
    skull: float = 7
    slime: float = 6

@dataclass
class SpriteHealth(DynamicDataclass):
    enemy: float = 10
    bat: float = 11
    canine_gray: float = 15
    canine_white: float = 15
    golem: float = 20
    rat: float = 9
    skull: float = 11
    slime: float = 12

@dataclass
class SpriteValue(DynamicDataclass):
    enemy: float = 1.5
    bat: float = 1.4
    canine_gray: float = 3
    canine_white: float = 3
    golem: float = 5
    rat: float = 1.3
    skull: float = 1.6
    slime: float = 1.5

@dataclass
class ProjectileLevel(DynamicDataclass):
    fire_ball: int = None
    fire_ring: int = None
    flame_ball: int = None
    magic_arrow: int = None
    magic_orb: int = None
    thunder_ball: int = None
    
del dataclass

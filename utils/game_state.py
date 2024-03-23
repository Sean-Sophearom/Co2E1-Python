from __future__ import annotations
from dataclasses import dataclass
from .constant import GAMESTATUS, CUSTOMEVENTS
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .sprites import Player, Snackbar

__all__ = ["GameState"]

@dataclass
class Speed:
    player: float
    bullet: float
    enemy: float
    gem: float

@dataclass
class SpriteTimer:
    enemy: int
    bullet: int
    lightning: int

    def __getitem__(self, key):
        return getattr(self, str(key))

    def __setitem__(self, key, value):
        setattr(self, str(key), value)
@dataclass
class GameState:
    player: Player
    player_health: float
    player_max_health: float

    gem_radius: float
    gem_collected: float
    gem_capacity: float

    snackbar: Snackbar

    sprite_timer: SpriteTimer

    speed: Speed
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
    def reset():
        GameState.player = None
        GameState.player_health = 100
        GameState.player_max_health = 100

        GameState.gem_radius = 200
        GameState.gem_collected = 0
        GameState.gem_capacity = 3

        GameState.speed = Speed(
            player = 5, 
            bullet = 9, 
            enemy = 3, 
            gem = 7
        )

        GameState.sprite_timer = SpriteTimer(
            enemy = 1000,
            bullet = 900,
            lightning = 2500
        )

        if not hasattr(GameState, "snackbar") or GameState.snackbar is None:
            from .sprites import Snackbar
            GameState.snackbar = Snackbar()

        if not hasattr(GameState, "damage_splash_screen") or GameState.damage_splash_screen is None:
            from .sprites import DamageSplashScreen
            GameState.damage_splash_screen = DamageSplashScreen()
        
    
    
del dataclass

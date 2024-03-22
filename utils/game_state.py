from __future__ import annotations
from dataclasses import dataclass
from .constant import GAMESTATUS, CUSTOMEVENTS
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .sprites import Player

__all__ = ["GameState"]

@dataclass
class Speed:
    player: float
    bullet: float
    enemy: float
    gem: float

@dataclass
class GameState:
    player: Player
    player_health: float
    player_max_health: float

    gem_radius: float
    gem_collected: float
    gem_capacity: float

    speed: Speed
    game_status: GAMESTATUS = GAMESTATUS.HOME

    def change_status(status: GAMESTATUS):
        GameState.game_status = status

    def is_playing():
        return GameState.game_status == GAMESTATUS.PLAYING
    
    def is_home():
        return GameState.game_status == GAMESTATUS.HOME
    
    def is_game_over():
        return GameState.game_status == GAMESTATUS.GAME_OVER
    
    def is_skill_menu():
        return GameState.game_status == GAMESTATUS.SKILL_MENU
    
    def reset():
        GameState.player = None
        GameState.player_health = 100
        GameState.player_max_health = 100

        GameState.gem_radius = 200
        GameState.gem_collected = 0
        GameState.gem_capacity = 25

        GameState.speed = Speed(
            player = 5, 
            bullet = 9, 
            enemy = 3, 
            gem = 7
        )
    
del dataclass
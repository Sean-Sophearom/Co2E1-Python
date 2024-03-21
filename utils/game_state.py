from dataclasses import dataclass
from .constant import GAMESTATUS
from .sprites import Player

@dataclass
class Speed:
    player: int
    bullet: int
    enemy: int
    gem: int

@dataclass
class GameState:
    game_status: GAMESTATUS = GAMESTATUS.HOME
    player: Player = None
    player_health: int = 100
    player_max_health: int = 100

    gem_radius: int = 200
    gem_collected: int = 0
    gem_capacity = 25

    speed = Speed(
        player = 5, 
        bullet = 9, 
        enemy = 3, 
        gem = 7
    )

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
        GameState.game_status = GAMESTATUS.HOME
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
    
del dataclass, Player
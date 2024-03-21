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

    speed = Speed(
        player = 5, 
        bullet = 9, 
        enemy = 3, 
        gem = 7
    )

    def is_playing():
        return GameState.game_status == GAMESTATUS.PLAYING
    
    def is_home():
        return GameState.game_status == GAMESTATUS.HOME
    
    def is_game_over():
        return GameState.game_status == GAMESTATUS.GAME_OVER

del Speed
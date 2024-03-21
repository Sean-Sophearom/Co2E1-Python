from dataclasses import dataclass
from .constant import GAMESTATE
from .sprites import Player

@dataclass
class Speed:
    player: int
    bullet: int
    enemy: int
    gem: int

@dataclass
class Global:
    game_state: GAMESTATE = GAMESTATE.HOME
    player: Player = None

    speed = Speed(
        player = 5, 
        bullet = 9, 
        enemy = 3, 
        gem = 7
    )

del Speed
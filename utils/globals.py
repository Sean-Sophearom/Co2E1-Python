from dataclasses import dataclass
from .constant import GAMESTATE
from .sprites import Player

@dataclass
class Global:
    game_state: GAMESTATE = GAMESTATE.HOME
    player: Player = None
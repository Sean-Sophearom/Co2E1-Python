from dataclasses import dataclass
from .constant import GAMESTATE


@dataclass
class Global:
    game_state: GAMESTATE = GAMESTATE.HOME
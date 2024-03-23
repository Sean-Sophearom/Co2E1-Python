from dataclasses import dataclass
from .game_state import GameState
from .game_manager import GameManager
from .constant import CUSTOMEVENTS

__all__ = ["SkillManager"]

def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        GameManager.continue_game()
        GameState.gem_collected = 0
        return result
    return wrapper

@dataclass
class SkillManager:
    @decorator
    def increase_speed():
        GameState.sprit_speed.player += 1
        return "Player speed increased by 1"
    
    @decorator
    def unlock_lightning():
        SkillManager.set_timer(CUSTOMEVENTS.ADDLIGHTNING, GameState.sprite_timer.lightning)
        return "Lightning unlocked !!!"
    
    def set_timer(event, time):
        GameState.sprite_timer[event] = time
        GameManager.set_timer(event, time)

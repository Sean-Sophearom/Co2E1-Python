from dataclasses import dataclass
from .game_state import GameState
from .game_manager import GameManager

__all__ = ["SkillManager"]

def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        GameManager.continue_game()
        return result
    return wrapper

@dataclass
class SkillManager:
    @decorator
    def increase_speed():
        GameState.speed.player += 1

    

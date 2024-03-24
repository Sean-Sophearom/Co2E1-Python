from dataclasses import dataclass
from .game_state import GameState
from .game_manager import GameManager
from .constant import CUSTOMEVENTS
from .helper import get_projectiles_data
from math import log10
from random import choice

__all__ = ["SkillManager"]

def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        GameManager.continue_game()
        GameState.gem_collected = 0
        GameState.gem_capacity += log10(GameState.gem_capacity)
        return result
    return wrapper

@dataclass
class SkillManager:
    @decorator
    def unlock_or_upgrade_ability():
        if CUSTOMEVENTS.ADDLIGHTNING not in GameManager.timers:
            GameManager.set_timer(CUSTOMEVENTS.ADDLIGHTNING, GameState.sprite_timer.lightning)
            return "Lightning unlocked !!!"

        all_projectiles = get_projectiles_data()

        maxed_out = True
        for projectile in all_projectiles:
            current_level = GameState.projectile_level[projectile.name]
            if not current_level or current_level < projectile.data.level:
                maxed_out = False
                break
        
        if maxed_out:
            return "All abilities are maxed out !!!"

        while True:
            projectile = choice(all_projectiles)
            if not GameState.projectile_level[projectile.name]:
                GameState.projectile_level[projectile.name] = 1
                GameManager.set_timer(projectile.event, GameState.sprite_timer[projectile.name])
                return f"{projectile.data.title} unlocked !!!"
            elif GameState.projectile_level[projectile.name] < projectile.data.level:
                GameState.projectile_level[projectile.name] += 1
                GameManager.set_timer(projectile.event, GameState.sprite_timer[projectile.name])
                return f"{projectile.data.title} upgraded to level {GameState.projectile_level[projectile.name]}"

    @decorator
    def upgrade_attack():
        pass
    
    @decorator
    def upgrade_utility():
        GameState.sprite_speed.player += 1
        return "Player speed increased by 1"

    @decorator
    def upgrade_defense():
        SkillManager.set_timer(CUSTOMEVENTS.REGEN, GameState.sprite_timer.regen)
        return "Player health regen unlocked !!!"
    
    def set_timer(event, time):
        GameState.sprite_timer[event] = time
        GameManager.set_timer(event, time)

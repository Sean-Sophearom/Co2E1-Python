from dataclasses import dataclass
from .game_state import GameState
from .game_manager import GameManager
from .constant import CUSTOMEVENTS
from .helper import get_projectiles_data
from math import log10
from random import choice, randint

__all__ = ["SkillManager"]


def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        GameManager.continue_game()
        GameState.gem_collected = 0
        GameState.gem_capacity += log10(GameState.gem_capacity) * 1.4
        GameState.player_health = GameState.player_max_health
        return result

    return wrapper


@dataclass
class SkillManager:
    @decorator
    def unlock_or_upgrade_ability():
        if CUSTOMEVENTS.ADDLIGHTNING not in GameManager.timers:
            GameManager.set_timer(
                CUSTOMEVENTS.ADDLIGHTNING, GameState.sprite_timer.lightning
            )
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
                GameManager.set_timer(
                    projectile.event, GameState.sprite_timer[projectile.name]
                )
                return f"{projectile.data.title} unlocked !!!"
            elif GameState.projectile_level[projectile.name] < projectile.data.level:
                GameState.projectile_level[projectile.name] += 1
                GameState.sprite_damage[projectile.name] += (
                    log10(GameState.sprite_damage[projectile.name]) / 4
                )
                GameManager.set_timer(
                    projectile.event, GameState.sprite_timer[projectile.name]
                )
                return f"{projectile.data.title} upgraded to level {GameState.projectile_level[projectile.name]}"

    @decorator
    def upgrade_attack():
        GameState.player_damage_multiplier += log10(GameState.player_damage_multiplier)
        return "Player damage increased by 10%"

    @decorator
    def upgrade_defense():
        rand = randint(1, 3)
        if rand == 1:
            GameState.player_defense_multiplier += log10(
                GameState.player_defense_multiplier
            )
            return "Player defense increased by 10%"
        elif rand == 2:
            GameState.player_max_health += log10(GameState.player_max_health)
            return "Player max health increased by 10%"
        else:
            if CUSTOMEVENTS.REGEN not in GameManager.timers:
                SkillManager.set_timer(CUSTOMEVENTS.REGEN, GameState.sprite_timer.regen)
                return "Player health regen unlocked !!!"
            else:
                GameState.player_regen += log10(GameState.player_regen)
                return "Player health regen increased by 10%"

    @decorator
    def upgrade_utility():
        rand = randint(1, 2)
        if rand == 1:
            GameState.player_speed += log10(GameState.player_speed) / 2
            return "Player speed increased by 10%"
        else:
            GameState.gem_value_multiplier += (
                log10(GameState.gem_value_multiplier + 1) * 2
            )
            return "Experience gained increased by 20%"

    def set_timer(event, time):
        GameState.sprite_timer[event] = time
        GameManager.set_timer(event, time)

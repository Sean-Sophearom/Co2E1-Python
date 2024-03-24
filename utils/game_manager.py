from .game_state import GameState
from .constant import GAMESTATUS, SCREEN_WIDTH, SCREEN_HEIGHT, CUSTOMEVENTS, TARGET_FPS
from .spawner import Spawner
import pygame
from typing import List

__all__ = ["GameManager"]

class GameManager():
    timers: List[int] = []

    @staticmethod
    def home_screen():
        from .sprites import Text, Background
        from .sprite_group import ui_elements, all_sprites, statics, skill_menu_screen_group

        GameState.change_status(GAMESTATUS.HOME)

        empty_group(all_sprites, statics, ui_elements, skill_menu_screen_group)

        statics.add(Background())

        ui_elements.add(Text("Start Game", 60, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), GameManager.start_game))
        ui_elements.add(Text("Exit", 40, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 65), lambda: exit(0)))
    
    @staticmethod
    def start_game():
        from .sprites import Player, HealthBar, ExpBar
        from .sprite_group import all_sprites, statics, ui_elements, skill_menu_screen_group
        
        GameManager.reset()
        GameState.player = Player()

        empty_group(ui_elements, skill_menu_screen_group)
        GameState.change_status(GAMESTATUS.PLAYING)

        GameManager.clear_timers()
        GameManager.set_timer(CUSTOMEVENTS.ADDENEMY, GameState.sprite_timer.enemy)
        GameManager.set_timer(CUSTOMEVENTS.ADDBULLET, GameState.sprite_timer.bullet)
        
        statics.add(HealthBar())
        statics.add(ExpBar())

        all_sprites.add(GameState.player)
    
    @staticmethod
    def game_over():
        from .sprites import Text, Background
        from .sprite_group import ui_elements, all_sprites, statics

        GameState.change_status(GAMESTATUS.GAME_OVER)

        if GameState.player: GameState.player.kill()
        empty_group(all_sprites, statics, ui_elements)

        statics.add(Background())

        ui_elements.add(Text("Game Over!", 70, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 65), color=(255, 0, 0)))
        ui_elements.add(Text("Play again", 40, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), GameManager.start_game))
        ui_elements.add(Text("Exit", 40, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 65), lambda: exit(0)))

    @staticmethod
    def skill_menu():
        GameState.change_status(GAMESTATUS.SKILL_MENU)
        from .sprites import SkillMenuScreen
        from .sprite_group import skill_menu_screen_group

        skill_menu_screen_group.add(SkillMenuScreen())
    
    @staticmethod
    def continue_game():
        GameState.change_status(GAMESTATUS.PLAYING)
        from .sprite_group import skill_menu_screen_group
        empty_group(skill_menu_screen_group)
    
    @staticmethod
    def set_timer(timer: int, duration: int):
        GameManager.timers.append(timer)
        pygame.time.set_timer(timer, duration)
    
    @staticmethod
    def clear_timers():
        for timer in GameManager.timers: pygame.time.set_timer(timer, 0)
        GameManager.timers.clear()
    
    @staticmethod
    def reset():
        GameManager.clear_timers()
        GameState.reset()

    @staticmethod
    def regen_player(heal: float):
        if GameState.player_health < GameState.player_max_health:
            GameState.player_health += heal
            if GameState.player_health > GameState.player_max_health: GameState.player_health = GameState.player_max_health
            Spawner.spawn_health_text(GameState.player.rect.center, heal)

    @staticmethod
    def take_damage(damage: float):
        damage_by_fps = damage / TARGET_FPS
        GameState.player_health -= damage_by_fps
        GameManager.show_damage_splash_screen()
        if GameState.player_health <= 0: GameManager.game_over()

    @staticmethod
    def collect_gem(gem):
        GameState.gem_collected += gem.value
        gem.kill()
        if GameState.gem_collected >= GameState.gem_capacity: 
            GameManager.skill_menu()

    @staticmethod
    def set_snackbar(text: str):
        if hasattr(GameState, "snackbar"):
            GameState.snackbar.set_text(text)

    @staticmethod
    def show_damage_splash_screen():
        if hasattr(GameState, "damage_splash_screen"):
            GameState.damage_splash_screen.show()
    

def empty_group(*groups):
    for group in groups:
        for element in group: element.kill()
        group.empty()
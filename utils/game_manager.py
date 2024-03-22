from .game_state import GameState
from .constant import GAMESTATUS, SCREEN_WIDTH, SCREEN_HEIGHT, CUSTOMEVENTS
import pygame

__all__ = ["GameManager"]

class GameManager():
    timers = []
    def home_screen():
        from .sprites import Text, Background
        from .sprite_group import ui_elements, all_sprites, statics, skill_menu_screen_group

        GameState.change_status(GAMESTATUS.HOME)

        empty_group(all_sprites, statics, ui_elements, skill_menu_screen_group)

        statics.add(Background())

        ui_elements.add(Text("Start Game", 60, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), GameManager.start_game))
        ui_elements.add(Text("Exit", 40, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 65), lambda: exit(0)))

    def start_game():
        from .sprites import Player, HealthBar, ExpBar
        from .sprite_group import all_sprites, statics, ui_elements, skill_menu_screen_group
        
        GameManager.reset()
        GameState.player = Player()

        empty_group(ui_elements, skill_menu_screen_group)
        GameState.change_status(GAMESTATUS.PLAYING)

        GameManager.clear_timers()
        GameManager.set_timer(CUSTOMEVENTS.ADDENEMY, 1000)
        GameManager.set_timer(CUSTOMEVENTS.ADDBULLET, 900)
        
        statics.add(HealthBar())
        statics.add(ExpBar())

        all_sprites.add(GameState.player)
    
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

    def skill_menu():
        GameState.change_status(GAMESTATUS.SKILL_MENU)
        from .sprites import SkillMenuScreen
        from .sprite_group import skill_menu_screen_group

        skill_menu_screen_group.add(SkillMenuScreen())
    
    def continue_game():
        GameState.change_status(GAMESTATUS.PLAYING)
        from .sprite_group import skill_menu_screen_group
        empty_group(skill_menu_screen_group)
    
    def set_timer(timer, duration):
        GameManager.timers.append(timer)
        pygame.time.set_timer(timer, duration)
    
    def clear_timers():
        for timer in GameManager.timers: pygame.time.set_timer(timer, 0)
        GameManager.timers.clear()
    
    def reset():
        GameManager.clear_timers()
        GameState.reset()

def empty_group(*groups):
    for group in groups:
        for element in group: element.kill()
        group.empty()
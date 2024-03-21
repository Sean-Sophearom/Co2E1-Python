from .game_state import GameState
from .constant import GAMESTATUS, SCREEN_WIDTH, SCREEN_HEIGHT

class GameManager():
    def home_screen():
        from .sprites import Text, Background
        from .sprite_group import ui_elements, all_sprites, statics

        GameState.game_status = GAMESTATUS.HOME

        ui_elements.empty()
        all_sprites.empty()
        statics.empty()
        statics.add(Background())

        ui_elements.add(Text("Start Game", 60, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), GameManager.start_game))
        ui_elements.add(Text("Exit", 40, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 65), lambda: exit(0)))

    def start_game():
        from .sprites import Player, HealthBar, ExpBar
        from .sprite_group import all_sprites, statics, ui_elements
        
        GameState.player = Player()
        GameState.game_status = GAMESTATUS.PLAYING

        ui_elements.empty()
        
        statics.add(HealthBar())
        statics.add(ExpBar())

        all_sprites.add(GameState.player)
    
    def game_over():
        GameManager.home_screen()

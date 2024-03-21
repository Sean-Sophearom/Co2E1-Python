from .globals import Global
from .constant import GAMESTATE

class GameManager():
    def start():
        from .sprites import Player, HealthBar, ExpBar
        from .sprite_group import all_sprites, statics
        
        Global.player = Player()
        Global.game_state = GAMESTATE.PLAYING
        
        statics.add(HealthBar())
        statics.add(ExpBar())

        all_sprites.add(Global.player)

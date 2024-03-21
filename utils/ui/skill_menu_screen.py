from ..sprite.imp import *

class SkillMenuScreen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self.rect = self.surf.get_rect(topleft=(0, 0))
        self.surf.set_alpha(128)
        self.surf.fill((0, 0, 0))

    def draw(self): 
        return

    def update(self):
        self.draw()

    def handle_event(self, event):
        from ..game_manager import GameManager
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if self.rect.collidepoint(event.pos):
                    GameManager.continue_game()
                    

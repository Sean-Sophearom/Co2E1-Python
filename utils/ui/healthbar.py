from ..sprite.imp import *

width = 160
height = 15
inner = (255, 0, 0)
border_size = 2
offset = 40
border_radius = 2
outer = (255, 255, 255)

class HealthBar(pygame.sprite.Sprite):
    def __init__(self, fill = 1, center = None):
        if not center: center = (SCREEN_WIDTH - 10, 10)
        super().__init__()
        self.fill = fill
        self.draw()
        self.rect = self.surf.get_rect(topright=center)

    def update(self):
        from ..game_state import GameState
        self.fill = GameState.player_health / GameState.player_max_health
        if self.fill < 0: self.fill = 0
        elif self.fill > 1: self.fill = 1
        self.draw()

    def draw(self):
        self.surf = pygame.Surface((width, height))
        pygame.draw.rect(
            self.surf, 
            outer, 
            pygame.Rect(0, 0, width, height), 
            border_radius = border_radius
        )
        pygame.draw.rect(
            self.surf, 
            inner, 
            pygame.Rect(
                border_size, border_size, 
                (width - (border_size * 2)) * self.fill, 
                height - (border_size * 2)
            ), 
            border_radius = border_radius
        )
from ..sprite.imp import *

width = 120
height = 12
fill = 0
border_size = 2
offset = 40
border_radius = 2
inner = (0, 255, 0)
outer = (255, 255, 255)

class ExpBar(pygame.sprite.Sprite):
    def __init__(self, center = None):
        if not center: center = (SCREEN_WIDTH - 10, 30)
        super().__init__()
        self.fill = fill
        self.draw()
        self.rect = self.surf.get_rect(topright=center)

    def update(self):
        from ..game_state import GameState
        self.fill = GameState.gem_collected / GameState.gem_capacity
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
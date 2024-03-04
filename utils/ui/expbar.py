from ..sprite.imp import *

width = 120
height = 15
fill = 0.6
border_size = 2
offset = 40
border_radius = 2
inner = (0, 255, 0)
outer = (255, 255, 255)

class ExpBar(pygame.sprite.Sprite):
    def __init__(self, center = None):
        if not center: center = (SCREEN_WIDTH - 10, 30)
        super().__init__()
        # self.max_health = max_health
        # self.health = max_health
        self.fill = fill
        self.draw()
        self.rect = self.surf.get_rect(topright=center)
        self.frame_count = 0

    def update(self):
        self.frame_count += 1
        if self.frame_count >= 50:
            self.draw()
            self.frame_count = 0
            self.fill -= 0.1

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



    def decrease(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()
            return True
        return False
from .imp import * 

# Define the Background object extending pygame.sprite.Sprite
class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load("asset/images/background.png").convert()
        # change scale x and y
        self.surf = pygame.transform.scale(self.surf, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.surf.get_rect()
        self.rect.topleft = (0, 0)
        self.tag = "background"

    def update(self):
        pass

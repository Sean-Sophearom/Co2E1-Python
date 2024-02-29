from .imp import *

# Define the cloud object extending pygame.sprite.Sprite
# Use an image for a better looking sprite
class Cloud(pygame.sprite.Sprite):
    def __init__(self, center):
        super(Cloud, self).__init__()
        self.tag = "cloud"
        self.surf = pygame.image.load("sprite/cloud.png").convert()
        self.surf = pygame.transform.rotozoom(self.surf, 0, random.randint(65, 100) / 100)
        self.surf = pygame.transform.rotate(self.surf, random.randint(0, 360))
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(center=(center))


    # Move the cloud based on a constant speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        if is_out_of_bounds(self.rect): return self.kill()

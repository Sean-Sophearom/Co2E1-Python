from .imp import *
from ..spawner import Spawner

# Define the enemy object extending pygame.sprite.Sprite
# Instead of a surface, we use an image for a better looking sprite
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("asset/images/missile.png").convert()
        self.original_surf = self.surf
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.tag = TAGS.ENEMY
        # The starting position is randomly generated
        quadrant = random.randint(1, 4)
        center = (0, 0)
        if quadrant == 1:
            center = (random.randint(-20, 0), random.randint(0, SCREEN_HEIGHT))
        elif quadrant == 2:
            center = (random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 20), random.randint(0, SCREEN_HEIGHT))
        elif quadrant == 3:
            center = (random.randint(0, SCREEN_WIDTH), random.randint(-20, 0))
        else:
            center = (random.randint(0, SCREEN_WIDTH), random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT + 20))

        self.rect = self.surf.get_rect(center=center)
        self.speed = GameState.speed.enemy

    # Move the enemy based on speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        if is_out_of_bounds(self.rect): return self.kill()

        move_vector = pygame.Vector2(
            CENTER.x - self.rect.centerx,
            CENTER.y - self.rect.centery
        )
        
        if move_vector.length_squared() != 0:
            move_vector.normalize_ip()

            angle = math.degrees(math.atan2(move_vector.y, -move_vector.x)) 
            self.surf = pygame.transform.rotate(self.original_surf, angle)

            move_vector *= self.speed
            self.rect.move_ip(move_vector)
    
    def kill(self):
        super().kill()
        Spawner.spawn_gem(self.rect.center)
        Spawner.spawn_explosion(self.rect.center)

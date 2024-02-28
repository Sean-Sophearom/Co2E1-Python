import pygame
import random
import math
from utils.constant import * 
from utils.helper import * 

# Define the Player object extending pygame.sprite.Sprite
# Instead of a surface, we use an image for a better looking sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("jet.png").convert()
        self.original_surf = self.surf
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        )
        self.speed = 5

    # Move the sprite based on keypresses
    def update(self, pressed_keys, all_sprites):
        # Calculate movement vector based on pressed keys
        move_vector = pygame.Vector2(0, 0)
        if pressed_keys[K_UP] or pressed_keys[K_w]:
            move_vector += pygame.Vector2(0, -1)
        if pressed_keys[K_DOWN] or pressed_keys[K_s]:
            move_vector += pygame.Vector2(0, 1)
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            move_vector += pygame.Vector2(-1, 0)
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            move_vector += pygame.Vector2(1, 0)

        # Normalize the movement vector if it's not null
        if move_vector.length_squared() != 0:
            move_vector.normalize_ip()

        # Apply speed to the normalized movement vector
        move_vector *= self.speed
        
        if move_vector.x > 0:
            # flip in x-axis
            self.surf = pygame.transform.flip(self.original_surf, False, False)
        elif move_vector.x < 0:
            # flip in x-axis
            self.surf = pygame.transform.flip(self.original_surf, True, False)

        # Move the player
        self.rect.move_ip(move_vector)

        # Keep player on the screen
        # self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)) ## not needed anymore

        # Update camera position to keep player centered
        camera_offset_x = SCREEN_WIDTH // 2 - self.rect.centerx
        camera_offset_y = SCREEN_HEIGHT // 2 - self.rect.centery

        # Adjust the positions of all game elements (e.g., background) by the camera offset
        for sprite in all_sprites: sprite.rect.move_ip(camera_offset_x, camera_offset_y)


# Define the enemy object extending pygame.sprite.Sprite
# Instead of a surface, we use an image for a better looking sprite
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("missile.png").convert()
        self.original_surf = self.surf
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
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
        self.speed = 3

    # Move the enemy based on speed
    # Remove it when it passes the left edge of the screen
    def update(self):
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



# Define the cloud object extending pygame.sprite.Sprite
# Use an image for a better looking sprite
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the cloud based on a constant speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        if is_out_of_bounds(self.rect): self.kill()
        return
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

# Import the pygame module
import pygame

from utils.sprites import Player, Enemy, Cloud, Bullet, Gem
from utils.constant import *
from utils.helper import find_closest_target, generate_clouds

# Initialize pygame
pygame.init()

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ADDENEMY = pygame.USEREVENT + 1
ADDCLOUD = pygame.USEREVENT + 2
ADDBULLET = pygame.USEREVENT + 3
ADDGEM = pygame.USEREVENT + 4

pygame.time.set_timer(ADDCLOUD, 1000)
pygame.time.set_timer(ADDENEMY, 350)

# Create our 'player'
player = Player()

# Create groups to hold enemy sprites, cloud sprites, and all sprites
# - enemies is used for collision detection and position updates
# - clouds is used for position updates
# - all_sprites isused for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
bullets = pygame.sprite.Group()
gems = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Variable to keep our main loop running
running = True

# Our main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_SPACE:
                # Fire the custom event to add a bullet
                pygame.event.post(pygame.event.Event(ADDBULLET))
                pygame.event.post(pygame.event.Event(ADDGEM))

        # Did the user click the window close button? If so, stop the loop
        elif event.type == QUIT:
            running = False

        # Should we add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy, and add it to our sprite groups
            if len(enemies) <= 100:
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

        # Should we add a new cloud?
        elif event.type == ADDCLOUD:
            # Create the new cloud, and add it to our sprite groups
            if False:
                new_cloud = Cloud()
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)
        
        elif event.type == ADDBULLET:
            # get random target in enemies
            if len(enemies) > 0:
                target = find_closest_target(player, enemies)
                new_bullet = Bullet(target)
                bullets.add(new_bullet)
                all_sprites.add(new_bullet)
        elif event.type == ADDGEM:
            new_gem = Gem()
            gems.add(new_gem)
            all_sprites.add(new_gem)

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys, all_sprites)

    offset_x = SCREEN_WIDTH // 2 - player.rect.centerx
    offset_y = SCREEN_HEIGHT // 2 - player.rect.centery

    # for cloud in generate_clouds(clouds):
    #     clouds.add(cloud)
    #     all_sprites.add(cloud)    

    # Update the position of our enemies and clouds
    enemies.update()
    clouds.update()
    bullets.update(enemies)
    gems.update()

    # Fill the screen with sky blue
    screen.fill((135, 206, 250))

    # Draw all our sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if collected any gems
    if pygame.sprite.spritecollideany(player, gems):
        gem = pygame.sprite.spritecollideany(player, gems)
        gem.kill()

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, remove the player
        player.kill()

        # Stop the loop
        running = False

    # Flip everything to the display
    pygame.display.flip()

    # Ensure we maintain a 30 frames per second rate
    clock.tick(60)
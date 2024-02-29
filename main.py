# Import the pygame module
import pygame

from utils.sprites import Enemy, Cloud, Bullet
from utils.constant import *
from utils.helper import find_closest_target, generate_clouds
from utils.spawner import Spawner

# Initialize pygame
pygame.init()

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

from utils.sprite_group import *

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

        # Did the user click the window close button? If so, stop the loop
        elif event.type == QUIT:
            running = False

        # Should we add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy, and add it to our sprite groups
            if len(enemies) <= 100:
                Spawner.spawn_enemy()

        # Should we add a new cloud?
        elif event.type == ADDCLOUD:
            # Create the new cloud, and add it to our sprite groups
            if False:
                Spawner.spawn_cloud()
        
        elif event.type == ADDBULLET:
            # get random target in enemies
            if len(enemies) > 0:
                target = find_closest_target(player, enemies)
                Spawner.spawn_bullet(target)

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
# Import the pygame module
import pygame

from utils.constant import *
from utils.helper import find_closest_target, find_on_screen_targets
from utils.spawner import Spawner
from utils.sprites import Background

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
background = Background()

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

        elif event.type == ADDBULLET:
            # get random target in enemies
            if len(enemies) > 0:
                target = find_closest_target(player, enemies)
                if target: Spawner.spawn_bullet(target)

        elif event.type == ADDLIGHTNING:
            if len(enemies) > 0:
                target = find_on_screen_targets(enemies)
                if target: Spawner.spawn_lightning(target)

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys, all_sprites)

    offset_x = SCREEN_WIDTH // 2 - player.rect.centerx
    offset_y = SCREEN_HEIGHT // 2 - player.rect.centery


    # Update the position of all sprites
    enemies.update()
    bullets.update(enemies)
    explosions.update()
    lightnings.update(enemies)
    ui.update()
    gems.update()

    screen.blit(background.surf, background.rect)

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

    fps = int(clock.get_fps())

    # Render the FPS text
    fps_text = pygame.font.Font(None, 24).render(f"FPS: {fps}", True, (255,255,255))

    # Blit the FPS text onto the screen
    screen.blit(fps_text, (10, 10))

    pygame.display.flip()

    # Ensure we maintain a 30 frames per second rate
    clock.tick(TARGET_FPS)
# Import the pygame module
import pygame

from utils.constant import *
from utils.helper import find_closest_target, find_on_screen_targets
from utils.spawner import Spawner
from utils.game_state import GameState
from utils.game_manager import GameManager

# Initialize pygame
pygame.init()

# set custom cursor
pygame.mouse.set_cursor(*pygame.cursors.arrow)

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
    if GameState.is_home() and not ui_elements:
        GameManager.home_screen()

    # Look at every event in the queue
    for event in pygame.event.get():
        for element in ui_elements:
            if hasattr(element, "handle_event"):
                element.handle_event(event)

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

        elif event.type == ADDSHINYSTAR:
                Spawner.spawn_star()

        elif GameState.is_playing():
            if event.type == ADDENEMY:
                if len(enemies) <= 100:
                    Spawner.spawn_enemy()

            elif event.type == ADDBULLET:
                if len(enemies) > 0:
                    target = find_closest_target(enemies)
                    if target: Spawner.spawn_bullet(target)

            elif event.type == ADDLIGHTNING:
                if len(enemies) > 0:
                    target = find_on_screen_targets(enemies)
                    if target: Spawner.spawn_lightning(target)

    if GameState.is_playing():
        pressed_keys = pygame.key.get_pressed()
        GameState.player.update(pressed_keys, all_sprites)

        # Check if collected any gems
        if pygame.sprite.spritecollideany(GameState.player, gems):
            gem = pygame.sprite.spritecollideany(GameState.player, gems)
            gem.kill()
        
        # Check if any enemies have collided with the player
        if pygame.sprite.spritecollideany(GameState.player, enemies):
            GameManager.game_over()

    # Update the position of all sprites
    enemies.update()
    bullets.update(enemies)
    explosions.update()
    lightnings.update(enemies)
    ui.update()
    gems.update()
    statics.update()
    stars.update()
    ui_elements.update()

    # Draw all statics elements
    for entity in statics:
        screen.blit(entity.surf, entity.rect)
    
    for entity in ui_elements:
        screen.blit(entity.surf, entity.rect)

    # Draw all our sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)


    fps = int(clock.get_fps())

    # Render the FPS text
    fps_text = pygame.font.Font(FONTPATH, 24).render(f"FPS: {fps}", True, (255,255,255))

    # Blit the FPS text onto the screen
    screen.blit(fps_text, (10, 10))

    pygame.display.flip()

    # Ensure we maintain a 30 frames per second rate
    clock.tick(TARGET_FPS)
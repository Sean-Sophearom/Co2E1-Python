import asyncio

# Import the pygame module
import pygame

from utils.constant import *
from utils.helper import find_closest_target, find_on_screen_targets
from utils.spawner import Spawner
from utils.game_state import GameState
from utils.game_manager import GameManager

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

async def main():
    # Our main loop
    while True:
        if GameState.is_home() and not ui_elements:
            GameManager.home_screen()

        # Look at every event in the queue
        for event in pygame.event.get():
            for element in ui_elements.sprites() + skill_menu_screen_group.sprites():
                if hasattr(element, "handle_event"):
                    element.handle_event(event)

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit(0)

            elif event.type == QUIT:
                exit(0)

            elif event.type == CUSTOMEVENTS.ADDSHINYSTAR:
                Spawner.spawn_star()
            
            elif event.type == CUSTOMEVENTS.REGEN:
                GameManager.regen_player(GameState.player_regen)

            elif GameState.is_playing():
                if event.type == CUSTOMEVENTS.ADDENEMY:
                    if len(enemies) <= 100:
                        Spawner.spawn_enemy()
                        Spawner.spawn_animated_enemy()

                elif event.type == CUSTOMEVENTS.ADDBULLET:
                    if len(enemies) > 0:
                        target = find_closest_target(enemies)
                        if target: Spawner.spawn_bullet(target)

                elif event.type == CUSTOMEVENTS.ADDLIGHTNING:
                    if len(enemies) > 0:
                        target = find_on_screen_targets(enemies)
                        if target: Spawner.spawn_lightning(target)

        if GameState.is_playing():
            pressed_keys = pygame.key.get_pressed()
            GameState.player.update(pressed_keys, all_sprites)

            # Check if collected any gems
            if pygame.sprite.spritecollideany(GameState.player, gems):
                gem = pygame.sprite.spritecollideany(GameState.player, gems)
                GameManager.collect_gem(gem)
            
            # Check all enemies that have collided with player and apply damage accordingly
            collided_enemies = pygame.sprite.spritecollide(GameState.player, enemies, False)
            for enemy in collided_enemies:
                GameManager.take_damage(enemy.damage)

        # Update the position of all sprites
        if GameState.is_playing():
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

        for entity in skill_menu_screen_group:
            screen.blit(entity.surf, entity.rect)
        
        # Draw snackbar
        if hasattr(GameState, "snackbar"):
            GameState.snackbar.update()
            screen.blit(GameState.snackbar.surf, GameState.snackbar.rect)
        
        # Draw Damage SplashScreen
        if hasattr(GameState, "damage_splash_screen"):
            GameState.damage_splash_screen.update()
            screen.blit(GameState.damage_splash_screen.surf, GameState.damage_splash_screen.rect)

        # Check if any ui element is being hovered then change cursor style
        is_hovering = any(hasattr(entity, "is_hovering") and entity.is_hovering for entity in ui_elements.sprites() + skill_menu_screen_group.sprites())
        cursor_style = pygame.cursors.diamond if is_hovering else pygame.cursors.arrow
        try:
            pygame.mouse.set_cursor(*cursor_style)
        except:
            pass

        fps = int(clock.get_fps())

        # Render the FPS text
        fps_text = pygame.font.Font(FONTPATH, 24).render(f"FPS: {fps}", True, (255,255,255))

        # Blit the FPS text onto the screen
        screen.blit(fps_text, (10, 10))

        pygame.display.flip()

        # Ensure we maintain a 60 frames per second rate
        clock.tick(TARGET_FPS)
        GameState.update_delta_time()

        await asyncio.sleep(0)
    
asyncio.run(main())
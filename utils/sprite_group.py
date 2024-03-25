import pygame
from utils.sprites import Player, HealthBar, Background, ExpBar
from .constant import CUSTOMEVENTS

# Create groups to hold enemy sprites, bullets, explosions and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites isused for rendering
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
explosions = pygame.sprite.Group()
lightnings = pygame.sprite.Group()
gems = pygame.sprite.Group()

stars = pygame.sprite.Group()

ui = pygame.sprite.Group()
ui_elements = pygame.sprite.Group()
statics = pygame.sprite.Group()
skill_menu_screen_group = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()

pygame.time.set_timer(CUSTOMEVENTS.ADDSHINYSTAR, 2000)

del pygame
del Player

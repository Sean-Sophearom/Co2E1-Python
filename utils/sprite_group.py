import pygame
from utils.sprites import Player, HealthBar, Background, ExpBar

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

all_sprites = pygame.sprite.Group()


ADDENEMY = pygame.USEREVENT + 1
ADDBULLET = pygame.USEREVENT + 3
ADDLIGHTNING = pygame.USEREVENT + 4
ADDSHINYSTAR = pygame.USEREVENT + 5

pygame.time.set_timer(ADDENEMY, 350)
pygame.time.set_timer(ADDLIGHTNING, 1200)
pygame.time.set_timer(ADDSHINYSTAR, 2000)

del pygame
del Player
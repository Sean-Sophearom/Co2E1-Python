import pygame
from utils.sprites import Player

# Create groups to hold enemy sprites, cloud sprites, and all sprites
# - enemies is used for collision detection and position updates
# - clouds is used for position updates
# - all_sprites isused for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
bullets = pygame.sprite.Group()
gems = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# Create our 'player'
player = Player()
all_sprites.add(player)

ADDENEMY = pygame.USEREVENT + 1
ADDCLOUD = pygame.USEREVENT + 2
ADDBULLET = pygame.USEREVENT + 3

pygame.time.set_timer(ADDCLOUD, 1000)
pygame.time.set_timer(ADDENEMY, 350)

del pygame
del Player
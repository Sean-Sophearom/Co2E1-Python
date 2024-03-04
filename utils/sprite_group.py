import pygame
from utils.sprites import Player, HealthBar, Background, ExpBar

# Create groups to hold enemy sprites, cloud sprites, and all sprites
# - enemies is used for collision detection and position updates
# - clouds is used for position updates
# - all_sprites isused for rendering
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
explosions = pygame.sprite.Group()
lightnings = pygame.sprite.Group()
gems = pygame.sprite.Group()
ui = pygame.sprite.Group()
statics = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# Create our 'player'
player = Player()
all_sprites.add(player)

statics.add(Background())
statics.add(HealthBar())
statics.add(ExpBar())

ADDENEMY = pygame.USEREVENT + 1
ADDBULLET = pygame.USEREVENT + 3
ADDLIGHTNING = pygame.USEREVENT + 4

pygame.time.set_timer(ADDENEMY, 350)
pygame.time.set_timer(ADDLIGHTNING, 1200)

del pygame
del Player
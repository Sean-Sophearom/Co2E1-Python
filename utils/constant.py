from enum import Enum
from dataclasses import dataclass
import pygame
import pygame.math as math
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    K_a,
    K_s,
    K_w,
    K_d,
    KEYDOWN,
    QUIT,
)

class GAMESTATUS(Enum):
    HOME = "home"
    PLAYING = "playing"
    GAME_OVER = "game_over"
    SKILL_MENU = "skill_menu"

class TAGS(Enum):
    PLAYER = "player"
    ENEMY = "enemy"
    BULLET = "bullet"
    GEM = "gem"
    EXPLOSION = "explosion"
    LIGHTNING = "lightning"
    STAR = "star"
    HEALTHBAR = "healthbar"
    EXPBAR = "expbar"
    TEXT = "text"
    BACKGROUND = "background"

@dataclass
class CUSTOMEVENTS():
    ADDENEMY = pygame.USEREVENT + 1
    ADDBULLET = pygame.USEREVENT + 2
    ADDLIGHTNING = pygame.USEREVENT + 3
    ADDSHINYSTAR = pygame.USEREVENT + 4
    REGEN = pygame.USEREVENT + 5

# Define constants for the screen width and height
# For pygame, we will use a larger screen size for better visual experience
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
    
# For pygbag, we will use a smaller screen size for better performance in browser emulator
# SCREEN_WIDTH = 960
# SCREEN_HEIGHT = 540
TARGET_FPS = 60

FONTPATH = "asset/font/8-bit-pixel.ttf"

# Define the center object as a Vector2 with x and y coordinates
CENTER = math.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)



del math
del Enum
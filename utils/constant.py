from enum import Enum
from dataclasses import dataclass
import pygame
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

# Define constants for the screen width and height
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TARGET_FPS = 60

FONTPATH = "asset/font/8-bit-pixel.ttf"

import pygame.math as math

# Define the center object as a Vector2 with x and y coordinates
CENTER = math.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)



del math
del Enum
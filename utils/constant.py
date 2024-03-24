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
    ADDSHINYSTAR = pygame.USEREVENT + 1
    REGEN = pygame.USEREVENT + 2

    ADDBULLET = pygame.USEREVENT + 3
    ADDLIGHTNING = pygame.USEREVENT + 4
    ADDFIREBALL = pygame.USEREVENT + 5
    ADDFIRERING = pygame.USEREVENT + 6
    ADDFLAMEBALL = pygame.USEREVENT + 7
    ADDMAGICARROW = pygame.USEREVENT + 8
    ADDMAGICORB = pygame.USEREVENT + 9
    ADDTHUNDERBALL = pygame.USEREVENT + 10

    ADDENEMY = pygame.USEREVENT + 11
    ADDBAT = pygame.USEREVENT + 12
    ADDCANINEGRAY = pygame.USEREVENT + 13
    ADDCANINEWHITE = pygame.USEREVENT + 14
    ADDGOLEM = pygame.USEREVENT + 15
    ADDRAT = pygame.USEREVENT + 16
    ADDSKULL = pygame.USEREVENT + 17
    ADDSLIME = pygame.USEREVENT + 18

    @staticmethod
    def get_enemy_events():
        return [
            CUSTOMEVENTS.ADDENEMY,
            CUSTOMEVENTS.ADDBAT,
            CUSTOMEVENTS.ADDCANINEGRAY,
            CUSTOMEVENTS.ADDCANINEWHITE,
            CUSTOMEVENTS.ADDGOLEM,
            CUSTOMEVENTS.ADDRAT,
            CUSTOMEVENTS.ADDSKULL,
            CUSTOMEVENTS.ADDSLIME
        ]

    @staticmethod
    def get_projectile_events():
        return [
            CUSTOMEVENTS.ADDBULLET,
            CUSTOMEVENTS.ADDLIGHTNING,
            CUSTOMEVENTS.ADDFIREBALL,
            CUSTOMEVENTS.ADDFIRERING,
            CUSTOMEVENTS.ADDFLAMEBALL,
            CUSTOMEVENTS.ADDMAGICARROW,
            CUSTOMEVENTS.ADDMAGICORB,
            CUSTOMEVENTS.ADDTHUNDERBALL
        ]

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
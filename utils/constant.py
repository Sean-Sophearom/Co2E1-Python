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


class CustomEvents:
    def __init__(self):
        self.ADDSHINYSTAR = pygame.USEREVENT + 10
        self.REGEN = pygame.USEREVENT + 20

        self.ADDBULLET = pygame.USEREVENT + 30
        self.ADDLIGHTNING = pygame.USEREVENT + 40
        self.ADDFIREBALL = pygame.USEREVENT + 50
        self.ADDFIRERING = pygame.USEREVENT + 60
        self.ADDFLAMEBALL = pygame.USEREVENT + 70
        self.ADDMAGICARROW = pygame.USEREVENT + 80
        self.ADDMAGICORB = pygame.USEREVENT + 90
        self.ADDTHUNDERBALL = pygame.USEREVENT + 100

        self.ADDENEMY = pygame.USEREVENT + 110
        self.ADDBAT = pygame.USEREVENT + 120
        self.ADDCANINEGRAY = pygame.USEREVENT + 130
        self.ADDCANINEWHITE = pygame.USEREVENT + 140
        self.ADDGOLEM = pygame.USEREVENT + 150
        self.ADDRAT = pygame.USEREVENT + 160
        self.ADDSKULL = pygame.USEREVENT + 170
        self.ADDSLIME = pygame.USEREVENT + 180

        self.WAVEUPDATE = pygame.USEREVENT + 190

        self.disabled = [
            "canine_gray",
            "canine_white",
        ]

    def get_enemy_events(self):
        return [
            self.ADDENEMY,
            self.ADDBAT,
            self.ADDCANINEGRAY,
            self.ADDCANINEWHITE,
            self.ADDGOLEM,
            self.ADDRAT,
            self.ADDSKULL,
            self.ADDSLIME,
        ]

    def get_projectile_events(self):
        return [
            self.ADDBULLET,
            self.ADDLIGHTNING,
            self.ADDFIREBALL,
            self.ADDFIRERING,
            self.ADDFLAMEBALL,
            self.ADDMAGICARROW,
            self.ADDMAGICORB,
            self.ADDTHUNDERBALL,
        ]


CUSTOMEVENTS = CustomEvents()

# Define constants for the screen width and height
# For pygame, we will use a larger screen size for better visual experience
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
# SCREEN_WIDTH = 1920 / 1.25
# SCREEN_HEIGHT = 1080 / 1.25

# For pygbag, we will use a smaller screen size for better performance in browser emulator
# SCREEN_WIDTH = 960
# SCREEN_HEIGHT = 540
TARGET_FPS = 60

FONTPATH = "asset/font/8-bit-pixel.ttf"

# Define the center object as a Vector2 with x and y coordinates
CENTER = math.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

del math
del Enum

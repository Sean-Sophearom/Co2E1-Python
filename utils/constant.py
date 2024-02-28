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

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

import pygame.math as math

# Define the center object as a Vector2 with x and y coordinates
CENTER = math.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

del math
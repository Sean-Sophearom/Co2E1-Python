import pygame
from ..constant import FONTPATH, SCREEN_HEIGHT, SCREEN_WIDTH

margin = 20
padding = (12, 5)
border_radius = 5
font_size = 25
show_duration = 4000
fade_duration = 400

white = 255, 255, 255
black = 0, 0, 0
red = 220, 38, 38
green = 22, 163, 74
blue = 29, 78, 216
dark_blue = 30, 64, 175
yellow = 252, 211, 77
purple = 139, 92, 246
cyan = 14, 165, 233
dark_cyan = 2, 132, 199

class Snackbar(pygame.sprite.Sprite):
    def __init__(self, text = '', bottomright = None, color = white):
        if bottomright is None:
            bottomright = (
                SCREEN_WIDTH - margin,
                SCREEN_HEIGHT - margin
            )
        super().__init__()
        self.font = pygame.font.Font(FONTPATH, font_size)
        self.text = str(text)
        self.color = color
        self.bottomright = bottomright
        self.draw()
        self.timer = 0

    def update(self):
        current_time = pygame.time.get_ticks()
        diff = current_time - self.timer
        if len(self.text) == 0:
            self.surf.set_alpha(0)
        elif diff > show_duration and self.surf.get_alpha() > 0:
            new_alpha = 255 - (diff - show_duration) / fade_duration * 255 if diff < (show_duration + fade_duration) else 0
            self.surf.set_alpha(new_alpha)
        

    def set_text(self, text):
        self.text = text
        self.draw()
        self.timer = pygame.time.get_ticks()
    
    def draw(self):
        text_size = self.font.size(self.text)

        size = (text_size[0] + padding[0] * 2, text_size[1] + padding[1] * 2)

        self.surf = pygame.Surface(size, pygame.SRCALPHA)
        self.rect = self.surf.get_rect(bottomright = self.bottomright)

        text_surf = self.font.render(self.text, True, self.color)
        text_rect = text_surf.get_rect(
            bottomright = (size[0] - padding[0], size[1] - padding[1])
        )

        pygame.draw.rect(
            self.surf,
            dark_blue,
            pygame.Rect(0, 0, size[0], size[1]),
            border_radius = border_radius
        )

        self.surf.blit(text_surf, text_rect)
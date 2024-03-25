import pygame
from ..constant import FONTPATH


class FadeUpText(pygame.sprite.Sprite):
    def __init__(self, text, center, size, color):
        super().__init__()
        self.font = pygame.font.Font(FONTPATH, size)
        self.text = str(round(float(text), 2))
        self.color = color if len(color) == 4 else (*color, 255)
        self.alpha = self.color[3]
        self.surf = self.font.render(self.text, True, self.color)
        self.rect = self.surf.get_rect(center=center)
        self.frame_count = 0

    def update(self):
        self.frame_count += 1

        self.alpha -= 4
        self.surf.set_alpha(self.alpha)

        self.rect = self.surf.get_rect(
            center=(self.rect.centerx, self.rect.centery - 1)
        )

        if self.frame_count == 60:
            self.kill()

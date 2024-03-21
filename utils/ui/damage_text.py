import pygame
from ..constant import FONTPATH

class DamageText(pygame.sprite.Sprite):
    def __init__(self, text, size, center):
        super().__init__()
        self.font = pygame.font.Font(FONTPATH, size)
        self.text = str(text)
        self.color = (200, 0, 0, 200)
        self.surf = self.font.render(self.text, True, self.color)
        self.rect = self.surf.get_rect(center = center)
        self.frame_count = 0

    def update(self):
        self.frame_count += 1

        self.color = (
            self.color[0],
            self.color[1],
            self.color[2],
            self.color[3] - 4
        )

        self.surf.set_alpha(self.color[3])

        self.rect = self.surf.get_rect(center = (
            self.rect.centerx,
            self.rect.centery - 1
        ))

        if self.frame_count == 60:
            self.kill()
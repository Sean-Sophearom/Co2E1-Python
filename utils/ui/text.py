import pygame
from ..constant import FONTPATH

class Text(pygame.sprite.Sprite):
    def __init__(self, text, size, center, onclick = None, color = (255, 255, 255)):
        super().__init__()
        self.font = pygame.font.Font(FONTPATH, size)
        self.text = str(text)
        self.color = color
        self.surf = self.font.render(self.text, True, self.color)
        self.rect = self.surf.get_rect(center = center)
        self.onclick = onclick
        self.is_hover = False
        self.original_surf = self.surf

    def update(self):
        if self.is_hover and self.onclick:
            self.surf = pygame.transform.scale(self.original_surf, (int(self.rect.width * 1.1), int(self.rect.height * 1.1)))
        else:
            self.surf = pygame.transform.scale(self.original_surf, (self.rect.width, self.rect.height))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if self.rect.collidepoint(event.pos):
                    if self.onclick:
                        self.onclick()
        
        elif event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.is_hover = True
            else:
                self.is_hover = False

from ..sprite.imp import *

frame_count = 5


class DamageSplashScreen(pygame.sprite.Sprite):
    def __init__(self):
        self.surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self.rect = self.surf.get_rect(topleft=(0, 0))

        overlay_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay_surf.fill((255, 0, 0, 24))

        self.surf.blit(overlay_surf, (0, 0))
        self.frame_count = 0

    def update(self):
        if self.frame_count > 0:
            self.surf.set_alpha(255)
            self.frame_count -= 1

        else:
            self.surf.set_alpha(0)

    def show(self, frames=frame_count):
        self.frame_count = frames

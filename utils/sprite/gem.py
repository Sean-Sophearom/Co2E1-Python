from .imp import * 
from .animated import Animated


class Gem(Animated):
    def __init__(self, center, value = 1):
        super().__init__(
            f"asset/images/gem/{value - 1}.png", 
            width = 8 * 8, 
            height = 14 * 8 , 
            frames = 5, 
            scale = 0.16,
            animation_speed = 7
        )
        self.value = value
        self.tag = TAGS.GEM
        self.collected = False
        self.speed = GameState.speed.gem
        self.rect = self.surf.get_rect(center=center)

    def update(self):
        super().update()
        if is_out_of_bounds(self.rect): return self.kill()

        # if self.collected then move towards center of screen
        if self.collected:
            move_vector = pygame.Vector2(
                SCREEN_WIDTH // 2 - self.rect.centerx,
                SCREEN_HEIGHT // 2 - self.rect.centery
            )
            if move_vector.length_squared() == 0:
                return self.kill()
            move_vector.normalize_ip()
            move_vector *= self.speed
            self.rect.move_ip(move_vector)

        # check if distance to center of screen is small
        elif math.sqrt((self.rect.centerx - SCREEN_WIDTH // 2) ** 2 + (self.rect.centery - SCREEN_HEIGHT // 2) ** 2) < GameState.gem_radius:
            self.collected = True

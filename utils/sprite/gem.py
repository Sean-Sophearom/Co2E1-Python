from .imp import *
from .animated import Animated
from math import floor
from ..spawner import Spawner
from ..game_state import GameState

max_gem_img = 13


class Gem(Animated):
    def __init__(self, center, value: float = 1):
        self.value = value * GameState.gem_value_multiplier
        super().__init__(
            f"asset/images/gem/{(floor(self.value - 1) % (max_gem_img + 1))}.png",
            width=8 * 8,
            height=14 * 8,
            frames=5,
            scale=0.16,
            animation_speed=7,
        )
        self.tag = TAGS.GEM
        self.collected = False
        self.rect = self.surf.get_rect(center=center)

    def update(self):
        super().update()
        if GameState.is_playing() == False:
            return
        if is_out_of_bounds(self.rect):
            return self.kill()

        # if self.collected then move towards center of screen
        if self.collected:
            move_vector = pygame.Vector2(
                SCREEN_WIDTH // 2 - self.rect.centerx,
                SCREEN_HEIGHT // 2 - self.rect.centery,
            )
            if move_vector.length_squared() == 0:
                return self.kill()
            move_vector.normalize_ip()
            move_vector *= GameState.sprite_speed.gem * GameState.delta_frame
            self.rect.move_ip(move_vector)

        # check if distance to center of screen is small
        elif (
            math.sqrt(
                (self.rect.centerx - SCREEN_WIDTH // 2) ** 2
                + (self.rect.centery - SCREEN_HEIGHT // 2) ** 2
            )
            < GameState.gem_radius
        ):
            self.collected = True

    def kill(self):
        super().kill()
        Spawner.spawn_exp_text(self.rect.midtop, self.value)

from .imp import *
from .animated import Animated

max_sprite_img = 7


class Explosion(Animated):
    def __init__(self, center=None, idx=0):
        if not center:
            center = (
                random.randint(20, SCREEN_WIDTH - 20),
                random.randint(20, SCREEN_HEIGHT - 20),
            )
        super().__init__(
            f"asset/images/explosion/{idx % max_sprite_img + 1}.png",
            width=550,
            height=550,
            frames=10,
            scale=0.06,
            animation_speed=3,
            mode="once",
        )
        self.tag = TAGS.EXPLOSION
        self.rect = self.surf.get_rect(center=center)

    def update(self):
        super().update()
        if is_out_of_bounds(self.rect):
            self.kill()

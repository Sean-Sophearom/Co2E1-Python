from .imp import * 
from .animated import Animated

class ShinyStar(Animated):
    def __init__(self, center=None):
        if not center: center = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
        super().__init__(
            "asset/images/shiny-star.png", 
            width = 185, 
            height = 185, 
            frames = 10, 
            scale = 0.125,
            gapx=48,
            gapy=34,
            columns=6,
            animation_speed = 5,
            mode = "once"
        )
        self.tag = TAGS.STAR
        self.rect = self.surf.get_rect(center=center)

    def update(self):
        super().update()
from .imp import *
from .animated import Animated
from utils.spawner import Spawner


class Lightning(Animated):
    def __init__(self, target):
        # if not center: center = (random.randint(20, SCREEN_WIDTH - 20), random.randint(20, SCREEN_HEIGHT - 20))
        super().__init__(
            "asset/images/lightning.png",
            width=130,
            height=660,
            frames=5,
            scalex=0.15,
            animation_speed=4,
            mode="once",
        )
        self.damage = GameState.sprite_damage.lightning
        self.tag = TAGS.LIGHTNING
        self.rect = self.surf.get_rect(midbottom=target.rect.center)
        self.target = target

    def update(self, enemies):

        super().update()
        if is_out_of_bounds(self.rect):
            self.kill()
        # check if collide with enemies
        if self.current_frame >= 2 and pygame.sprite.spritecollideany(self, enemies):
            enemy = pygame.sprite.spritecollideany(self, enemies)
            enemy.take_damage(self.damage)

        # if target is dead return
        if not self.target.alive():
            return

        # move towards target
        move_vector = pygame.Vector2(
            self.target.rect.centerx - self.rect.centerx,
            self.target.rect.centery - self.rect.bottom,
        )

        if move_vector.length_squared() != 0:
            move_vector.normalize_ip()
            move_vector *= 10
            self.rect.move_ip(move_vector)

    def kill(self):
        super().kill()
        Spawner.spawn_explosion(self.rect.midbottom)

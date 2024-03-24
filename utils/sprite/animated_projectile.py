#time crunch no more time to refactor
from .imp import *
from .animated import Animated
from ..spawner import Spawner

class AnimatedProjectile(Animated):
    def __init__(self, target, kwargs):
        self.sprite_data = kwargs

        name = self.sprite_data.name
        level = GameState.projectile_level[name]
        if level > self.sprite_data.level: level = self.sprite_data.level
        super().__init__(
            f"asset/images/projectile/{name}/{level}.png", 
            **self.sprite_data.data,
            mode = "loop",
        )
        self.rect = self.surf.get_rect(center=CENTER)
        self.target = target
        self.tag = TAGS.BULLET
        self.damage = GameState.sprite_damage[name] * GameState.player_damage_multiplier
        self.target_move_vector = pygame.Vector2(0, 0)
        self.flip = kwargs.flip
        self.flipped = False

    def update(self, enemies):
        super().update()
        if is_out_of_bounds(self.rect): return self.kill()

        move_vector = pygame.Vector2(
            self.target.rect.centerx - self.rect.centerx,
            self.target.rect.centery - self.rect.centery
        )

        if not self.target.alive(): 
            move_vector = self.target_move_vector
        else:
            self.target_move_vector = move_vector

        if move_vector.length_squared() == 0:
            return self.kill()    
        move_vector.normalize_ip()
        move_vector *= GameState.sprite_speed.bullet * GameState.delta_frame
        self.rect.move_ip(move_vector)

        # rotate to face movement direction
        angle = math.degrees(math.atan2(move_vector.y, -move_vector.x)) 

        if self.flip:
            angle -= 180

        self.surf = pygame.transform.rotate(self.original_surf, angle)

        # if collide with any enemies
        if pygame.sprite.spritecollideany(self, enemies):
            enemy = pygame.sprite.spritecollideany(self, enemies)
            enemy.take_damage(self.damage)
            self.kill()
            
    
    def kill(self):
        super().kill()
        Spawner.spawn_explosion(self.rect.center)



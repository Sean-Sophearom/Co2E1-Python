from .imp import * 
from ..spawner import Spawner
class Bullet(pygame.sprite.Sprite):
    def __init__(self, target, damage = 5):
        super(Bullet, self).__init__()
        self.surf = pygame.image.load("asset/images/missile.png").convert()
        self.surf = pygame.transform.rotozoom(self.surf, 0, 0.55)
        self.original_surf = self.surf
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=CENTER)
        self.target = target
        self.damage = 5
        self.target_move_vector = pygame.Vector2(0, 0)

    def update(self, enemies):
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
        move_vector *= GameState.speed.bullet
        self.rect.move_ip(move_vector)

        # rotate to face movement direction
        angle = math.degrees(math.atan2(move_vector.y, -move_vector.x)) 
        self.surf = pygame.transform.rotate(self.original_surf, angle)

        # if collide with any enemies
        if pygame.sprite.spritecollideany(self, enemies):
            enemy = pygame.sprite.spritecollideany(self, enemies)
            enemy.take_damage(self.damage)
            self.kill()
            
    
    def kill(self):
        super().kill()
        Spawner.spawn_explosion(self.rect.center)
        Spawner.spawn_damage_text(self.rect.center, self.damage)

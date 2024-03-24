#time crunch no more time to refactor
from .imp import *
from .animated import Animated
from ..spawner import Spawner

# self.flip is from sprite
# self.flipped is from movement

class AnimatedEnemy(Animated):
    def __init__(self, kwargs):
        center = self.get_random_spawn()
        self.sprite_data = kwargs

        super().__init__(
            f"asset/images/enemy/{self.sprite_data.name}/run.png", 
            **self.sprite_data.run,
            mode = "loop",
        )
        self.tag = TAGS.ENEMY
        self.value = GameState.sprite_value.enemy
        self.damage = GameState.sprite_damage.enemy
        self.health = GameState.sprite_health.enemy
        self.rect = self.surf.get_rect(center=center)
        self.flip = kwargs.flip
        self.flipped = False

    # Move the enemy based on speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        super().update()
        if is_out_of_bounds(self.rect): return self.kill()

        move_vector = pygame.Vector2(
            CENTER.x - self.rect.centerx,
            CENTER.y - self.rect.centery
        )
        
        if move_vector.length_squared() != 0:
            move_vector.normalize_ip()

            self.flipped = (move_vector.x < 0) ^ self.flip
            
            if self.flipped:
                self.surf = pygame.transform.flip(self.original_surf, True, False)

            move_vector *= GameState.sprite_speed.enemy * GameState.delta_frame
            self.rect.move_ip(move_vector)
    
    def kill(self):
        from ..sprite_group import all_sprites, ui
        
        on_kill = lambda center = None: Spawner.spawn_gem(center=center, value=self.value)
        death_animation = Animated(
            f"asset/images/enemy/{self.sprite_data.name}/death.png", 
            **self.sprite_data.death,
            mode="once",
            flipped=self.flipped,
            on_kill=on_kill
        )
        death_animation.rect = death_animation.surf.get_rect(center=self.rect.center)
        all_sprites.add(death_animation)
        ui.add(death_animation)
        super().kill()
        Spawner.spawn_explosion(self.rect.center)

    def take_damage(self, damage):
        Spawner.spawn_damage_text(self.rect.center, damage)
        self.health -= damage
        if self.health <= 0: self.kill()
    
    def get_random_spawn(self):
        quadrant = random.randint(1, 4)
        center = (0, 0)
        if quadrant == 1:
            center = (random.randint(-20, 0), random.randint(0, SCREEN_HEIGHT))
        elif quadrant == 2:
            center = (random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 20), random.randint(0, SCREEN_HEIGHT))
        elif quadrant == 3:
            center = (random.randint(0, SCREEN_WIDTH), random.randint(-20, 0))
        else:
            center = (random.randint(0, SCREEN_WIDTH), random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT + 20))

        return center

from .imp import * 

class Gem(pygame.sprite.Sprite):
    def __init__(self, center=None):
        if not center: center = (random.randint(20, SCREEN_WIDTH - 20), random.randint(20, SCREEN_HEIGHT - 20))
        super(Gem, self).__init__()
        self.tag = "gem"
        self.surf = pygame.image.load("sprite/gem.png").convert_alpha()
        self.surf = pygame.transform.rotozoom(self.surf, 0, 0.15)
        self.collected = False
        self.speed = SPEED['gem']
        self.rect = self.surf.get_rect(center=center)
        # self.scale_dir = 1
        # self.scale = random.uniform(0.15, 0.2)
        # self.original_surf = self.surf
        

    def update(self):
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
        elif math.sqrt((self.rect.centerx - SCREEN_WIDTH // 2) ** 2 + (self.rect.centery - SCREEN_HEIGHT // 2) ** 2) < 200:
            self.collected = True
        # self.scale += self.scale_dir * 0.002
        # if self.scale > 0.2 or self.scale < 0.15:
        #     self.scale_dir *= -1
        # self.surf = pygame.transform.rotozoom(self.original_surf, 0, self.scale)
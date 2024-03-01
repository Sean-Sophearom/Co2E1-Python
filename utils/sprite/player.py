from .imp import * 

# Define the Player object extending pygame.sprite.Sprite
# Instead of a surface, we use an image for a better looking sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.tag = "player"
        self.surf = pygame.image.load("asset/images/player.png").convert()
        self.original_surf = self.surf
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        )
        self.speed = SPEED['player']

    # Move the sprite based on keypresses
    def update(self, pressed_keys, all_sprites):
        # Calculate movement vector based on pressed keys
        move_vector = pygame.Vector2(0, 0)
        if pressed_keys[K_UP] or pressed_keys[K_w]:
            move_vector += pygame.Vector2(0, -1)
        if pressed_keys[K_DOWN] or pressed_keys[K_s]:
            move_vector += pygame.Vector2(0, 1)
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            move_vector += pygame.Vector2(-1, 0)
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            move_vector += pygame.Vector2(1, 0)

        # Normalize the movement vector if it's not null
        if move_vector.length_squared() != 0:
            move_vector.normalize_ip()

            flipped_surf = pygame.transform.flip(self.original_surf, move_vector.x < 0, False)
            angle = 0
            if move_vector.x == 0:
                angle = 90 if move_vector.y < 0 else 270
            elif move_vector.x > 0:
                if move_vector.y == 0: angle = 0
                else: angle = -45 if move_vector.y > 0 else 45
            else:
                if move_vector.y == 0: angle = 0
                else: angle = 45 if move_vector.y > 0 else -45
            self.surf = pygame.transform.rotate(flipped_surf, angle)
        # Apply speed to the normalized movement vector
        move_vector *= self.speed
        
        # Move the player
        self.rect.move_ip(move_vector)

        # Update camera position to keep player centered
        camera_offset_x = SCREEN_WIDTH // 2 - self.rect.centerx
        camera_offset_y = SCREEN_HEIGHT // 2 - self.rect.centery

        # Adjust the positions of all game elements (e.g., background) by the camera offset
        for sprite in all_sprites: sprite.rect.move_ip(camera_offset_x, camera_offset_y)

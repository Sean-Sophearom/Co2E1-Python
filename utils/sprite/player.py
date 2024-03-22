from .imp import * 
from .animated import Animated

# Define the Player object extending pygame.sprite.Sprite
# Instead of a surface, we use an image for a better looking sprite
class Player(Animated):
    def __init__(self):
        super().__init__(
            "asset/images/player.png", 
            width = 192, 
            height = 192, 
            frames = 5, 
            scale = 0.3,
            animation_speed = 4,
            mode = "loop"
        )
        self.tag = TAGS.PLAYER
        self.target_rotation = 0
        self.rotation_speed = 2
        self.current_rotation = 0
        self.rect = self.surf.get_rect(
            center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        )

    # Move the sprite based on keypresses
    def update(self, pressed_keys, all_sprites):
        super().update()
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
            self.target_rotation = move_vector.angle_to(pygame.Vector2(0, 1)) - 90
            
        self.surf = pygame.transform.rotate(self.original_surf, self.target_rotation)
        # Apply speed to the normalized movement vector
        move_vector *= GameState.speed.player
        
        # Move the player
        self.rect.move_ip(move_vector)

        # Update camera position to keep player centered
        camera_offset_x = SCREEN_WIDTH // 2 - self.rect.centerx
        camera_offset_y = SCREEN_HEIGHT // 2 - self.rect.centery

        # Adjust the positions of all game elements (e.g., background) by the camera offset
        for sprite in all_sprites: sprite.rect.move_ip(camera_offset_x, camera_offset_y)

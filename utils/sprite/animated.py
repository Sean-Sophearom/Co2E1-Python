import pygame

class Animated(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, frame_width, frame_height, num_frames, scale=1, animation_speed=5):
        super(Animated, self).__init__()
        self.sprite_sheet = pygame.image.load(sprite_sheet).convert_alpha()
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.scale = scale
        self.animation_speed = animation_speed
        self.num_frames = num_frames
        
        self.frames = []
        self.current_frame = 0
        self.frame_count = 0
        self.load_frames()

        self.image = self.frames[self.current_frame]
        self.surf = self.image.convert_alpha()

    def load_frames(self):
        for i in range(self.num_frames):
            frame = pygame.Surface((self.frame_width, self.frame_height), pygame.SRCALPHA)
            frame.blit(self.sprite_sheet, (0, 0), (i * self.frame_width, 0, self.frame_width, self.frame_height))
            if self.scale != 1: 
                frame = pygame.transform.rotozoom(frame, 0, self.scale)
            self.frames.append(frame)

    def update(self):
        self.frame_count += 1
        if self.frame_count >= self.animation_speed:
            self.frame_count = 0
            self.animate()
        
    def animate(self):
        self.current_frame = (self.current_frame + 1) % self.num_frames
        self.image = self.frames[self.current_frame]
        self.surf = self.image.convert_alpha()
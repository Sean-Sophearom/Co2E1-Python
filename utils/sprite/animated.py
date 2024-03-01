import pygame

class Animated(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, width, height, frames, scale=1, animation_speed=5, mode="loop", scalex=1, scaley=1):
        super(Animated, self).__init__()
        self.sprite_sheet = pygame.image.load(sprite_sheet).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.scale = scale
        self.scalex = scalex
        self.scaley = scaley
        self.animation_speed = animation_speed
        self.num_frames = frames
        self.mode = mode
        
        self.frames = []
        self.current_frame = 0
        self.frame_count = 0
        self.load_frames()
        self.animate()

    def load_frames(self):
        for i in range(self.num_frames):
            frame = pygame.Surface((self.frame_width, self.frame_height), pygame.SRCALPHA)
            frame.blit(self.sprite_sheet, (0, 0), (i * self.frame_width, 0, self.frame_width, self.frame_height))
            if self.scale != 1: 
                frame = pygame.transform.rotozoom(frame, 0, self.scale)
            if self.scalex != 1 or self.scaley != 1:
                frame = pygame.transform.scale(frame, (int(self.frame_width * self.scalex), int(self.frame_height * self.scaley)))
            self.frames.append(frame)

    def update(self):
        self.frame_count += 1
        if self.frame_count >= self.animation_speed:
            self.frame_count = 0
            self.animate()
        
    def animate(self):
        self.current_frame = (self.current_frame + 1) % self.num_frames

        if self.mode == "once" and self.current_frame == len(self.frames) - 1:
            self.kill()
        else:
            self.surf = self.frames[self.current_frame]
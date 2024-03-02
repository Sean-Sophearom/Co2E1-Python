import pygame
from utils.constant import TARGET_FPS

cached = {}

class Animated(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, width, height, frames, scale=1, animation_speed=5, mode="loop", scalex=1, scaley=1, duration=None):
        super(Animated, self).__init__()

        self.frame_width = width
        self.frame_height = height
        self.scale = scale
        self.scalex = scalex
        self.scaley = scaley
        self.animation_speed = animation_speed if duration is None else int(duration * TARGET_FPS / frames)
        self.num_frames = frames
        self.mode = mode
        
        self.frames = []
        self.current_frame = 0
        self.frame_count = 0

        cacheName = f"{sprite_sheet}{width}{height}{frames}{scale}{animation_speed}{mode}{scalex}{scaley}"
        
        if cacheName in cached:
            self.frames = cached[cacheName]
        else:
            self.sprite_sheet = pygame.image.load(sprite_sheet).convert_alpha()
            self.load_frames()
            cached[cacheName] = self.frames

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
            self.original_surf = self.surf = self.frames[self.current_frame]
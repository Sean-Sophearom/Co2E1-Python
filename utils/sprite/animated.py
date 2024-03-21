import pygame
from utils.constant import TARGET_FPS
from math import ceil

cached = {}

class Animated(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, width, height, frames, scale=1, animation_speed=5, mode="loop", scalex=1, scaley=1, columns=0, gapx=0, gapy=0, duration=None):
        if columns == 0: columns = frames
        super(Animated, self).__init__()
        self.columns = columns
        self.gapx = gapx
        self.gapy = gapy
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

        cacheName = f"{sprite_sheet}{width}{height}{frames}{scale}{animation_speed}{mode}{scalex}{scaley}{columns}{gapx}{gapy}"
        
        if cacheName in cached:
            self.frames = cached[cacheName]
        else:
            self.sprite_sheet = pygame.image.load(sprite_sheet).convert_alpha()
            self.load_frames()
            cached[cacheName] = self.frames

        self.animate()

    def load_frames(self):
        rows = ceil(self.num_frames / self.columns)

        for row in range(rows):
            for col in range(self.columns):
                # cannot exceed num_frames
                if len(self.frames) >= self.num_frames: return

                frame = pygame.Surface((self.frame_width, self.frame_height), pygame.SRCALPHA)
                start_x = col * self.frame_width + self.gapx
                start_y = row * self.frame_height + self.gapy
                frame.blit(self.sprite_sheet, (0, 0), (start_x, start_y, self.frame_width, self.frame_height))
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
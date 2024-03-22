from ..sprite.imp import *
from dataclasses import dataclass

class SkillMenuScreen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self.rect = self.surf.get_rect(topleft=(0, 0))

        overlay_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay_surf.set_alpha(128)
        overlay_surf.fill((0, 0, 0))
        overlay_rect = overlay_surf.get_rect(topleft=(0, 0))
        
        title_font = pygame.font.Font(FONTPATH, 50)
        title_surf = title_font.render("Please Choose An Upgrade", True, (255, 255, 255))
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH // 2, 100))

        skill_names = (
            # "skill",
            # "attack",
            # "defense",
            # "utility"
            SkillSO("Ability", "Unlock a new ability OR Enhance existing ability", "skill", None),
            SkillSO("Attack", "Increase base attack stats, cooldown or attack range", "attack", None),
            SkillSO("Defense", "Increase base defense stats, health or durability", "defense", None),
            SkillSO("Utility", "Increase utility stats, movement speed, or exp", "utility", None)
        )

        self.skills = [
            OneSkillPanel(item.title, item.icon, item.description, idx, item.onclick) for idx, item in enumerate(skill_names)
        ]

        self.surf.blit(overlay_surf, overlay_rect)
        self.surf.blit(title_surf, title_rect)
        
        for entity in self.skills:
            self.surf.blit(entity.surf, entity.rect)

    def update(self):
        is_hovering = False
        for entity in self.skills:
            entity.update()
            if entity.is_hovering: is_hovering = True
        
        self.is_hovering = is_hovering


    def handle_event(self, event):
        from ..game_manager import GameManager

        is_hovering = False
        for entity in self.skills:
            entity.handle_event(event)
            if entity.is_hovering: is_hovering = True
        
        self.is_hovering = is_hovering

class OneSkillPanel:
    def __init__(self, title, icon, description, idx, onclick=None):
        self.top = 200
        self.skill_y_offset = 64
        self.onclick = onclick
        self.idx = idx
        self.is_hovering = False

        self.surf = pygame.Surface((SCREEN_WIDTH // 4, SCREEN_HEIGHT - self.top), pygame.SRCALPHA)
        self.rect = self.surf.get_rect(topleft=(idx * SCREEN_WIDTH//4, self.top))

        self.skill_surf = pygame.image.load(f"asset/images/icon_{icon}.png").convert_alpha()
        self.skill_original_surf = self.skill_surf
        self.skill_surf = pygame.transform.rotozoom(self.skill_surf, 0, 1.4)
        self.skill_rect = self.skill_surf.get_rect(center=(SCREEN_WIDTH // 8, self.skill_y_offset))

        self.panel_surf = pygame.image.load("asset/images/panel.png").convert_alpha()
        self.panel_original_surf = self.panel_surf
        self.panel_surf = pygame.transform.rotozoom(self.panel_surf, 0, 1.4)
        self.panel_rect = self.panel_surf.get_rect(center=(SCREEN_WIDTH // 8, self.skill_y_offset))

        self.font = pygame.font.Font(FONTPATH, 40)
        self.text_surf = self.font.render(title, True, (255, 255, 255))
        self.text_rect = self.text_surf.get_rect(center=(SCREEN_WIDTH // 8, self.skill_y_offset * 2.5))
        
        description_font = pygame.font.Font(FONTPATH, 25)

        renderTextCenteredAt(
            description,
            description_font,
            SCREEN_WIDTH // 8,
            self.skill_y_offset * 3,
            self.surf,
            240
        )

        self.surf.blit(self.panel_surf, self.panel_rect)
        self.surf.blit(self.skill_surf, self.skill_rect)
        self.surf.blit(self.text_surf, self.text_rect)

    def update(self):
        pass

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.is_colliding(event.pos):
                    if self.onclick:
                        self.onclick()

        elif event.type == pygame.MOUSEMOTION:
            if self.is_colliding(event.pos):
                self.is_hovering = True
            else: 
                self.is_hovering = False

    def is_colliding(self, point):
        left = self.rect.left + self.rect.width // 2 - self.panel_rect.width // 2
        right = self.rect.left + self.rect.width // 2 + self.panel_rect.width // 2
        top = self.rect.top + self.skill_y_offset - self.panel_rect.height // 2
        bottom = self.rect.top + self.skill_y_offset + self.panel_rect.height // 2

        x = point[0]
        y = point[1]

        return left <= x <= right and top <= y <= bottom


@dataclass
class SkillSO:
    title: str
    description: str
    icon: str
    onclick: callable

def renderTextCenteredAt(text, font, x, y, screen, allowed_width,colour=(255,255,255)):
    # first, split the text into words
    words = text.split()

    # now, construct lines out of these words
    lines = []
    while len(words) > 0:
        # get as many words as will fit within allowed_width
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))
            fw, fh = font.size(' '.join(line_words + words[:1]))
            if fw > allowed_width:
                break

        # add a line consisting of those words
        line = ' '.join(line_words)
        lines.append(line)

    # now we've split our text into lines that fit into the width, actually
    # render them

    # we'll render each line below the last, so we need to keep track of
    # the culmative height of the lines we've rendered so far
    y_offset = 0
    for line in lines:
        fw, fh = font.size(line)

        # (tx, ty) is the top-left of the font surface
        tx = x - fw / 2
        ty = y + y_offset

        font_surface = font.render(line, True, colour)
        screen.blit(font_surface, (tx, ty))

        y_offset += fh
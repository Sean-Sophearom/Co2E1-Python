from ..sprite.imp import *

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
            "skill",
            "attack",
            "defense",
            "utility"
        )

        self.skills = [
            OneSkillPanel(name, idx) for idx, name in enumerate(skill_names)
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
    def __init__(self, png_name, idx, onclick=None):
        self.top = 200
        self.skill_y_offset = 64
        self.onclick = onclick
        self.idx = idx
        self.is_hovering = False

        self.surf = pygame.Surface((SCREEN_WIDTH // 4, SCREEN_HEIGHT - self.top), pygame.SRCALPHA)
        self.rect = self.surf.get_rect(topleft=(idx * SCREEN_WIDTH//4, self.top))

        self.skill_surf = pygame.image.load(f"asset/images/icon_{png_name}.png").convert_alpha()
        self.skill_original_surf = self.skill_surf
        self.skill_surf = pygame.transform.rotozoom(self.skill_surf, 0, 1.4)
        self.skill_rect = self.skill_surf.get_rect(center=(SCREEN_WIDTH // 8, self.skill_y_offset))

        self.panel_surf = pygame.image.load("asset/images/panel.png").convert_alpha()
        self.panel_original_surf = self.panel_surf
        self.panel_surf = pygame.transform.rotozoom(self.panel_surf, 0, 1.4)
        self.panel_rect = self.panel_surf.get_rect(center=(SCREEN_WIDTH // 8, self.skill_y_offset))

        self.font = pygame.font.Font(FONTPATH, 40)
        self.text_surf = self.font.render(capitalize(png_name), True, (255, 255, 255))
        self.text_rect = self.text_surf.get_rect(center=(SCREEN_WIDTH // 8, self.skill_y_offset * 2.5))
        
        self.description_font = pygame.font.Font(FONTPATH, 25)
        self.description_text_surf = self.description_font.render(capitalize("Lorem Ipsum Dolor Amet Sit"), True, (255, 255, 255))
        self.description_text_rect = self.description_text_surf.get_rect(center=(SCREEN_WIDTH // 8, self.skill_y_offset * 3))

        self.surf.blit(self.panel_surf, self.panel_rect)
        self.surf.blit(self.skill_surf, self.skill_rect)
        self.surf.blit(self.text_surf, self.text_rect)
        self.surf.blit(self.description_text_surf, self.description_text_rect)

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

def capitalize(string: str):
    return string[0].upper() + string[1:]
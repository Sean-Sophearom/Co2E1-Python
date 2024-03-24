from utils.enemies_sprite_data import EnemiesSpriteData
from utils.projectiles_sprite_data import ProjectilesSpriteData
from utils.spawner import Spawner
from dataclasses import dataclass
from utils.constant import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    CENTER,
    CUSTOMEVENTS
)
from random import choice

@dataclass
class ProjectileData:
    name: str
    event: int
    data: any

def is_out_of_bounds(rect):
    return (
        rect.right < -SCREEN_WIDTH
        or rect.left > 2 * SCREEN_WIDTH
        or rect.bottom < -SCREEN_HEIGHT
        or rect.top > 2 * SCREEN_HEIGHT
    )

def is_on_screen(rect):
    return (
        rect.right > 0
        and rect.left < SCREEN_WIDTH
        and rect.bottom > 0
        and rect.top < SCREEN_HEIGHT
    )

def find_closest_target(group, target=None):
    if not group:
        return None
    base_x = target.rect.centerx if target else CENTER.x
    base_y = target.rect.centery if target else CENTER.y
    return min(group, key=lambda x: (x.rect.centerx - base_x)**2 + (x.rect.centery - base_y)**2)

def find_on_screen_targets(group):
    for target in group:
        if is_on_screen(target.rect):
            return target
    
def find_random_target(group):
    if not group:
        return None
    return choice(group.sprites())
        
def get_projectiles_data():
    from .constant import CUSTOMEVENTS
    from .projectiles_sprite_data import ProjectilesSpriteData

    return [
        ProjectileData("fire_ball", CUSTOMEVENTS.ADDFIREBALL, ProjectilesSpriteData.fire_ball),
        ProjectileData("fire_ring", CUSTOMEVENTS.ADDFIRERING, ProjectilesSpriteData.fire_ring),
        ProjectileData("flame_ball", CUSTOMEVENTS.ADDFLAMEBALL, ProjectilesSpriteData.flame_ball),
        ProjectileData("magic_arrow", CUSTOMEVENTS.ADDMAGICARROW, ProjectilesSpriteData.magic_arrow),
        ProjectileData("magic_orb", CUSTOMEVENTS.ADDMAGICORB, ProjectilesSpriteData.magic_orb),
        ProjectileData("thunder_ball", CUSTOMEVENTS.ADDTHUNDERBALL, ProjectilesSpriteData.thunder_ball)
    ]

def handle_spawning(event_type):
    from utils.sprite_group import enemies
    if event_type == CUSTOMEVENTS.ADDENEMY:
        if len(enemies) <= 100:
            Spawner.spawn_enemy()

    elif event_type == CUSTOMEVENTS.ADDBULLET:
        target = find_closest_target(enemies)
        if target: Spawner.spawn_bullet(target)

    elif event_type == CUSTOMEVENTS.ADDLIGHTNING:
        target = find_on_screen_targets(enemies)
        if target: Spawner.spawn_lightning(target)
    
    elif event_type == CUSTOMEVENTS.ADDFIREBALL:
        target = find_random_target(enemies)
        if target: Spawner.spawn_animated_projectile(target, ProjectilesSpriteData.fire_ball)
    
    elif event_type == CUSTOMEVENTS.ADDFIRERING:
        target = find_random_target(enemies)
        if target: Spawner.spawn_animated_projectile(target, ProjectilesSpriteData.fire_ring)

    elif event_type == CUSTOMEVENTS.ADDFLAMEBALL:
        target = find_random_target(enemies)
        if target: Spawner.spawn_animated_projectile(target, ProjectilesSpriteData.flame_ball)
    
    elif event_type == CUSTOMEVENTS.ADDMAGICARROW:
        target = find_random_target(enemies)
        if target: Spawner.spawn_animated_projectile(target, ProjectilesSpriteData.magic_arrow)
    
    elif event_type == CUSTOMEVENTS.ADDMAGICORB:
        target = find_random_target(enemies)
        if target: Spawner.spawn_animated_projectile(target, ProjectilesSpriteData.magic_orb)
    
    elif event_type == CUSTOMEVENTS.ADDTHUNDERBALL:
        target = find_random_target(enemies)
        if target: Spawner.spawn_animated_projectile(target, ProjectilesSpriteData.thunder_ball)

    elif event_type == CUSTOMEVENTS.ADDBAT:
        Spawner.spawn_animated_enemy(EnemiesSpriteData.bat)
    
    elif event_type == CUSTOMEVENTS.ADDCANINEGRAY:
        Spawner.spawn_animated_enemy(EnemiesSpriteData.canine_gray)
    
    elif event_type == CUSTOMEVENTS.ADDCANINEWHITE:
        Spawner.spawn_animated_enemy(EnemiesSpriteData.canine_white)

    elif event_type == CUSTOMEVENTS.ADDGOLEM:
        Spawner.spawn_animated_enemy(EnemiesSpriteData.golem)

    elif event_type == CUSTOMEVENTS.ADDRAT:
        Spawner.spawn_animated_enemy(EnemiesSpriteData.rat)
    
    elif event_type == CUSTOMEVENTS.ADDSKULL:
        Spawner.spawn_animated_enemy(EnemiesSpriteData.skull)
    
    elif event_type == CUSTOMEVENTS.ADDSLIME:
        Spawner.spawn_animated_enemy(EnemiesSpriteData.slime)
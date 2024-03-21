from utils.constant import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    CENTER
)

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
    base_x = target.rect.centerx if target else CENTER.x
    base_y = target.rect.centery if target else CENTER.y
    return min(group, key=lambda x: (x.rect.centerx - base_x)**2 + (x.rect.centery - base_y)**2)

def find_on_screen_targets(group):
    for target in group:
        if is_on_screen(target.rect):
            return target

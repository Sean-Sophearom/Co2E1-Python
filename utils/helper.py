from utils.constant import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT
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

def find_closest_target(player, group):
    return min(group, key=lambda x: (x.rect.centerx - player.rect.centerx)**2 + (x.rect.centery - player.rect.centery)**2)

def find_on_screen_targets(group):
    for target in group:
        if is_on_screen(target.rect):
            return target

def generate_clouds(clouds):
    from utils.sprites import Cloud
    import random
    from pygame import Rect

    new_clouds = []

    x = 1
    y = 1

    base_rect = (
        SCREEN_WIDTH * -1,
        SCREEN_HEIGHT * -1
    )

    rect_size = (
        SCREEN_WIDTH / x,
        SCREEN_HEIGHT / y
    )

    for i in range(x * 3):
        for j in range(y * 3):
            current_rect = Rect(
                base_rect[0] + i * SCREEN_WIDTH,
                base_rect[1] + j * SCREEN_HEIGHT,
                rect_size[0],
                rect_size[1]
            )

            #check if any cloud is in the current rect
            if not any([cloud.rect.colliderect(current_rect) for cloud in clouds]):
                new_cloud = Cloud(
                    (
                        random.randint(current_rect.left, current_rect.right),
                        random.randint(current_rect.top, current_rect.bottom)
                    )
                )

                new_clouds.append(new_cloud)
    return new_clouds
            
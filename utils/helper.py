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
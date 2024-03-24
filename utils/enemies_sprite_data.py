from dataclasses import dataclass

__all__ = ["EnemiesSpriteData"]

@dataclass
class Actions:
    name: str
    run: any
    death: any
    flip: bool = False


@dataclass
class EnemiesSpriteData:
    golem: Actions = Actions(
        name = "golem",
        run = {
            "frames": 4,
            "animation_speed": 4,
            "height": 64,
            "width": 64,
            "scale": 1,
        },
        death = {
            "frames": 9,
            "animation_speed": 4,
            "height": 64,
            "width": 64,
            "scale": 1,
            "columns": 4
        }
    )
    bat: Actions = Actions(
        name = "bat",
        run = {
            "frames": 4,
            "animation_speed": 4,
            "height": 64,
            "width": 64,
            "scale": 1,
            "columns": 0
        },
        death = {
            "frames": 11,
            "animation_speed": 4,
            "height": 64,
            "width": 64,
            "scale": 1,
            "columns": 4
        },
    )
    canine_black: Actions = Actions(
        name = "canine_black",
        flip = True,
        run = {
            "frames": 6,
            "animation_speed": 4,
            "height": 32,
            "width": 48,
            "scale": 1,
            "columns": 4,
        },
        death = {
            "frames": 8,
            "animation_speed": 4,
            "height": 32,
            "width": 48,
            "scale": 1,
            "columns": 4,
        }
    )
    canine_gray: Actions = Actions(
        name = "canine_gray",
        flip = True,
        run = {
            "frames": 6,
            "animation_speed": 4,
            "height": 32,
            "width": 48,
            "scale": 1,
            "columns": 4,
        },
        death = {
            "frames": 8,
            "animation_speed": 4,
            "height": 32,
            "width": 48,
            "scale": 1,
            "columns": 4,
        }
    )
    canine_white: Actions = Actions(
        name = "canine_white",
        flip = True,
        run = {
            "frames": 6,
            "animation_speed": 4,
            "height": 32,
            "width": 48,
            "scale": 1,
            "columns": 4,
        },
        death = {
            "frames": 8,
            "animation_speed": 4,
            "height": 32,
            "width": 48,
            "scale": 1,
            "columns": 4,
        }
    )
    crab: Actions = Actions(
        name = "crab",
        run = {
            "frames": 6,
            "animation_speed": 4,
            "height": 64,
            "width": 64,
            "scale": 1,
            "columns": 4
        },
        death = {
            "frames": 5,
            "animation_speed": 4,
            "height": 64,
            "width": 64,
            "scale": 1,
            "columns": 4
        }
    )
    rat: Actions = Actions(
        name = "rat",
        run = {
            "frames": 6,
            "animation_speed": 4,
            "height": 64,
            "width": 64,
            "scale": 1,
            "columns": 4
        },
        death = {
            "frames": 5,
            "animation_speed": 4,
            "height": 64,
            "width": 64,
            "scale": 1,
            "columns": 4
        },
    )
    skull: Actions = Actions(
        name = "skull",
        run = {
            "frames": 8,
            "animation_speed": 4,
            "height": 64,
            "width": 64,
            "scale": 1,
            "columns": 4
        },
        death = {
            "frames": 10,
            "animation_speed": 4,
            "height": 64,
            "width": 64,
            "scale": 1,
            "columns": 4
        },
    )
    slime: Actions = Actions(
        name = "slime",
        run = {
            "frames": 4,
            "animation_speed": 4,
            "height": 64,
            "width": 64,
            "scale": 1,
            "columns": 4
        },
        death = {
            "frames": 6,
            "animation_speed": 4,
            "height": 64,
            "width": 64,
            "scale": 1,
            "columns": 4
        }
    )
    
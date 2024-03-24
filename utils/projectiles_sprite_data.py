from dataclasses import dataclass

__all__ = ["ProjectilesSpriteData"]

@dataclass
class Properties:
    name: str
    data: dict
    level: int
    flip: bool = False


@dataclass
class ProjectilesSpriteData:
    fire_ball: Properties = Properties(
        name = "Fire Ball",
        level = 3,
        data = {
            "frames": 60,
            "animation_speed": 3,
            "height": 64,
            "width": 64,
            "scale": 0.7,
        }
    )
    fire_ring: Properties = Properties(
        name = "Fire Ring",
        level = 6,
        data = {
            "frames": 60,
            "animation_speed": 3,
            "height": 100,
            "width": 100,
            "scale": 0.6,
        }
    )
    flame_ball: Properties = Properties(
        name = "Flame Ball",
        level = 6,
        data = {
            "frames": 30,
            "animation_speed": 4,
            "height": 16,
            "width": 16,
            "scale": 1.5,
        }
    )
    magic_arrow: Properties = Properties(
        name = "Magic Arrow",
        level = 3,
        data = {
            "frames": 30,
            "animation_speed": 4,
            "height": 100,
            "width": 100,
            "scale": 0.6,
        }
    )
    magic_orb: Properties = Properties(
        name = "Magic Orb",
        level = 3,
        data = {
            "frames": 30,
            "animation_speed": 4,
            "height": 32,
            "width": 32,
            "scale": 1.2,
        }
    )
    thunder_ball: Properties = Properties(
        name = "Thunder Ball",
        level = 6,
        data = {
            "frames": 60,
            "animation_speed": 4,
            "height": 32,
            "width": 32,
            "scale": 1.2,
        }
    )


from dataclasses import dataclass

__all__ = ["ProjectilesSpriteData"]

@dataclass
class Properties:
    title: str
    name: str
    data: dict
    level: int
    flip: bool = False


class DynamicDataclass:
    def __getitem__(self, key):
        return getattr(self, str(key))
    
    def __setitem__(self, key, value):
        setattr(self, str(key), value)

@dataclass
class ProjectilesSpriteData(DynamicDataclass):
    fire_ball: Properties = Properties(
        title = "Fire Ball",
        name = "fire_ball",
        level = 3,
        data = {
            "frames": 60,
            "animation_speed": 1,
            "height": 64,
            "width": 64,
            "scale": 0.7,
            "columns": 10
        }
    )
    fire_ring: Properties = Properties(
        title = "Fire Ring",
        name = "fire_ring",
        level = 6,
        data = {
            "frames": 60,
            "animation_speed": 1,
            "height": 100,
            "width": 100,
            "scale": 0.6,
            "columns": 10
        }
    )
    flame_ball: Properties = Properties(
        title = "Flame Ball",
        name = "flame_ball",
        level = 6,
        data = {
            "frames": 30,
            "animation_speed": 1,
            "height": 16,
            "width": 16,
            "scale": 1.5,
            "columns": 10
        }
    )
    magic_arrow: Properties = Properties(
        title = "Magic Arrow",
        name = "magic_arrow",
        level = 3,
        data = {
            "frames": 30,
            "animation_speed": 1,
            "height": 100,
            "width": 100,
            "scale": 0.6,
            "columns": 10
        }
    )
    magic_orb: Properties = Properties(
        title = "Magic Orb",
        name = "magic_orb",
        level = 3,
        data = {
            "frames": 30,
            "animation_speed": 1,
            "height": 32,
            "width": 32,
            "scale": 1.2,
            "columns": 10
        }
    )
    thunder_ball: Properties = Properties(
        title = "Thunder Ball",
        name = "thunder_ball",
        level = 6,
        data = {
            "frames": 60,
            "animation_speed": 1,
            "height": 32,
            "width": 32,
            "scale": 1.2,
            "columns": 10
        }
    )


from dataclasses import dataclass

__all__ = ["projectiles_sprite_data"]


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
    fire_ball: Properties
    fire_ring: Properties
    flame_ball: Properties
    magic_arrow: Properties
    magic_orb: Properties
    thunder_ball: Properties


projectiles_sprite_data = ProjectilesSpriteData(
    fire_ball=Properties(
        title="Fire Ball",
        name="fire_ball",
        level=3,
        data={
            "frames": 60,
            "animation_speed": 1,
            "height": 64,
            "width": 64,
            "scale": 0.7,
            "columns": 10,
        },
    ),
    fire_ring=Properties(
        title="Fire Ring",
        name="fire_ring",
        level=6,
        data={
            "frames": 60,
            "animation_speed": 1,
            "height": 100,
            "width": 100,
            "scale": 0.5,
            "columns": 10,
        },
    ),
    flame_ball=Properties(
        title="Flame Ball",
        name="flame_ball",
        level=6,
        data={
            "frames": 30,
            "animation_speed": 1,
            "height": 16,
            "width": 16,
            "scale": 1.5,
            "columns": 10,
        },
        flip=True,
    ),
    magic_arrow=Properties(
        title="Magic Arrow",
        name="magic_arrow",
        level=3,
        data={
            "frames": 30,
            "animation_speed": 1,
            "height": 100,
            "width": 100,
            "scale": 0.9,
            "columns": 10,
        },
        flip=True,
    ),
    magic_orb=Properties(
        title="Magic Orb",
        name="magic_orb",
        level=3,
        data={
            "frames": 30,
            "animation_speed": 1,
            "height": 32,
            "width": 32,
            "scale": 0.8,
            "columns": 10,
        },
    ),
    thunder_ball=Properties(
        title="Thunder Ball",
        name="thunder_ball",
        level=6,
        data={
            "frames": 60,
            "animation_speed": 1,
            "height": 32,
            "width": 32,
            "scale": 0.9,
            "columns": 10,
        },
    ),
)

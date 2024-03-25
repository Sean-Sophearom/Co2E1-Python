class Spawner:
    @staticmethod
    def spawn_gem(center=None, *args, **kwargs):
        from .sprite_group import all_sprites, gems
        from .sprites import Gem

        new_gem = Gem(center, *args, **kwargs)
        gems.add(new_gem)
        all_sprites.add(new_gem)
        return new_gem

    @staticmethod
    def spawn_enemy(*args, **kwargs):
        from .sprite_group import all_sprites, enemies
        from .sprites import Enemy

        new_enemy = Enemy(*args, **kwargs)
        enemies.add(new_enemy)
        all_sprites.add(new_enemy)
        return new_enemy

    @staticmethod
    def spawn_animated_enemy(type, *args, **kwargs):
        from .sprite_group import all_sprites, enemies
        from .sprites import AnimatedEnemy

        new_enemy = AnimatedEnemy(type)
        enemies.add(new_enemy)
        all_sprites.add(new_enemy)
        return new_enemy

    @staticmethod
    def spawn_bullet(target, *args, **kwargs):
        from .sprite_group import all_sprites, bullets
        from .sprites import Bullet

        new_bullet = Bullet(target, *args, **kwargs)
        bullets.add(new_bullet)
        all_sprites.add(new_bullet)
        return new_bullet

    @staticmethod
    def spawn_animated_projectile(target, type, *args, **kwargs):
        from .sprite_group import all_sprites, bullets
        from .sprites import AnimatedProjectile

        new_bullet = AnimatedProjectile(target, type, *args, **kwargs)
        bullets.add(new_bullet)
        all_sprites.add(new_bullet)
        return new_bullet

    @staticmethod
    def spawn_explosion(center, *args, **kwargs):
        from .sprite_group import all_sprites, explosions
        from .sprites import Explosion

        new_explosion = Explosion(center, *args, **kwargs)
        explosions.add(new_explosion)
        all_sprites.add(new_explosion)
        return new_explosion

    @staticmethod
    def spawn_lightning(center, *args, **kwargs):
        from .sprite_group import all_sprites, lightnings
        from .sprites import Lightning

        new_lightning = Lightning(center, *args, **kwargs)
        lightnings.add(new_lightning)
        all_sprites.add(new_lightning)
        return new_lightning

    @staticmethod
    def spawn_damage_text(center, damage=0, *args, **kwargs):
        from .sprite_group import all_sprites, ui
        from .sprites import FadeUpText

        if damage > 0:
            color = (255, 0, 0)
            size = 24
            new_text = FadeUpText(damage, center, size, color, *args, **kwargs)
            ui.add(new_text)
            all_sprites.add(new_text)
            return new_text

    @staticmethod
    def spawn_exp_text(center, exp=0, *args, **kwargs):
        from .sprite_group import all_sprites, ui
        from .sprites import FadeUpText

        if exp > 0:
            color = (0, 255, 0)
            size = 22
            exp = f"+{exp}"
            new_text = FadeUpText(exp, center, size, color, *args, **kwargs)
            ui.add(new_text)
            all_sprites.add(new_text)
            return new_text

    @staticmethod
    def spawn_health_text(center, health=0, *args, **kwargs):
        from .sprite_group import all_sprites, ui
        from .sprites import FadeUpText

        if health > 0:
            color = (255, 0, 0)
            size = 22
            health = f"+{health}"
            new_text = FadeUpText(health, center, size, color, *args, **kwargs)
            ui.add(new_text)
            all_sprites.add(new_text)
            return new_text

    @staticmethod
    def spawn_star(center=None, *args, **kwargs):
        from .sprite_group import all_sprites, stars
        from .sprites import ShinyStar

        new_star = ShinyStar(center, *args, **kwargs)
        stars.add(new_star)
        all_sprites.add(new_star)
        return new_star

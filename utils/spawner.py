
class Spawner():
    # define static method
    def spawn_gem(center = None, *args, **kwargs):
        from .sprite_group import all_sprites, gems
        from .sprites import Gem
        new_gem = Gem(center, *args, **kwargs)
        gems.add(new_gem)
        all_sprites.add(new_gem)
        return new_gem
    
    def spawn_enemy(*args, **kwargs):
        from .sprite_group import all_sprites, enemies
        from .sprites import Enemy
        new_enemy = Enemy(*args, **kwargs)
        enemies.add(new_enemy)
        all_sprites.add(new_enemy)
        return new_enemy
    
    def spawn_bullet(target, *args, **kwargs):
        from .sprite_group import all_sprites, bullets
        from .sprites import Bullet
        new_bullet = Bullet(target, *args, **kwargs)
        bullets.add(new_bullet)
        all_sprites.add(new_bullet)
        return new_bullet
    
    def spawn_explosion(center, *args, **kwargs):
        from .sprite_group import all_sprites, explosions
        from .sprites import Explosion
        new_explosion = Explosion(center, *args, **kwargs)
        explosions.add(new_explosion)
        all_sprites.add(new_explosion)
        return new_explosion
    
    def spawn_lightning(center, *args, **kwargs):
        from .sprite_group import all_sprites, lightnings
        from .sprites import Lightning
        new_lightning = Lightning(center, *args, **kwargs)
        lightnings.add(new_lightning)
        all_sprites.add(new_lightning)
        return new_lightning
    
    def spawn_text(center, *args, **kwargs):
        from .sprite_group import all_sprites, ui
        from .sprites import DamageText
        new_text = DamageText(100, 24, center, *args, **kwargs)
        ui.add(new_text)
        all_sprites.add(new_text)
        return new_text

    def spawn_star(center=None, *args, **kwargs):
        from .sprite_group import all_sprites, stars
        from .sprites import ShinyStar
        new_star = ShinyStar(center, *args, **kwargs)
        stars.add(new_star)
        all_sprites.add(new_star)
        return new_star
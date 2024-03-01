
class Spawner():
    # define static method
    @staticmethod
    def spawn_gem(center = None):
        from .sprite_group import all_sprites, gems
        from .sprites import Gem
        new_gem = Gem(center)
        gems.add(new_gem)
        all_sprites.add(new_gem)
        return new_gem
    
    @staticmethod
    def spawn_enemy():
        from .sprite_group import all_sprites, enemies
        from .sprites import Enemy
        new_enemy = Enemy()
        enemies.add(new_enemy)
        all_sprites.add(new_enemy)
        return new_enemy
    
    @staticmethod
    def spawn_bullet(target):
        from .sprite_group import all_sprites, bullets
        from .sprites import Bullet
        new_bullet = Bullet(target)
        bullets.add(new_bullet)
        all_sprites.add(new_bullet)
        return new_bullet
    
    @staticmethod
    def spawn_explosion(center):
        from .sprite_group import all_sprites, explosions
        from .sprites import Explosion
        new_explosion = Explosion(center)
        explosions.add(new_explosion)
        all_sprites.add(new_explosion)
        return new_explosion
    
    @staticmethod
    def spawn_lightning(center):
        from .sprite_group import all_sprites, lightnings
        from .sprites import Lightning
        new_lightning = Lightning(center)
        lightnings.add(new_lightning)
        all_sprites.add(new_lightning)
        return new_lightning

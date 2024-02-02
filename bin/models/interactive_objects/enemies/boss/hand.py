from bin.models.interactive_objects.enemies.enemy import Enemy
from pygame.sprite import Sprite, Group


class Hand(Enemy):
    def __init__(self, enemy_group: Group, coordinates: (int, int)):
        super().__init__(enemy_group, coordinates)

    def update(self, position: (int, int) = None, position_plus: (int, int) = (0, 0)):
        super(Hand, self).update(position, position_plus)
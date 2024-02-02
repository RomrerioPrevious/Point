from icecream import ic

from bin.models.interactive_objects.enemies.enemy import Enemy
from pygame.sprite import Sprite, Group
import pygame


class Obstacle(Enemy):
    def __init__(self, enemy_group: Group, coordinates: (int, int)):
        super().__init__(enemy_group, coordinates)
        image = pygame.image.load("resources/sprites/enemy.png")
        self.image = pygame.transform.scale(image, (80, 110))
        self.rect = self.image.get_rect()
        self.rect.x = coordinates[0]
        self.rect.y = coordinates[1]

    def update(self, position: (int, int) = None, position_plus: (int, int) = (0, 2)):
        super(Obstacle, self).update(position, position_plus)

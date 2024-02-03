from bin.models.interactive_objects.enemies.enemy import Enemy
from bin.models.states import Direction
from pygame.sprite import Sprite, Group
import pygame


class SideObstacle(Enemy):
    def __init__(self, enemy_group: Group, coordinates: (int, int), direction: Direction):
        super().__init__(enemy_group, coordinates)
        self.image = pygame.image.load("resources/sprites/side enemy.png")
        self.rect = self.image.get_rect()
        self.speed = 60 * direction
        self.tick = 0
        self.direction = direction
        self.rect.x = coordinates[0]
        self.rect.y = coordinates[1]

    def update(self, position: (int, int) = None, position_plus: (int, int) = (0, 0)):
        super(SideObstacle, self).update(position, (int(self.speed), 0))
        self.speed /= 2
        if self.speed * self.direction <= 2:
            self.speed = 60 * self.direction * -1
            self.tick += 1
        if self.tick == 2:
            del self

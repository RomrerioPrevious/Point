from pygame.sprite import Sprite, Group
from bin.models.interactive_objects import Point1D
import pygame
from abc import ABC


class Enemy(Sprite, ABC):
    def __init__(self, enemy: Group, coordinates: (int, int)):
        super().__init__(enemy)
        self.image = pygame.image.load("resources/sprites/enemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = coordinates[0]
        self.rect.y = coordinates[1]

    def update(self, position: (int, int) = None, position_plus: (int, int) = (0, 0)):
        if position:
            self.rect.x = position[0]
            self.rect.y = position[1]
        self.rect.x += position[0]
        self.rect.y += position[1]

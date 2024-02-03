from pygame.sprite import Sprite, Group
import pygame
from abc import ABC


class Deco(Sprite, ABC):
    def __init__(self, enemy_group: Group, coordinates: (int, int), image_path: str):
        super().__init__(enemy_group)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = coordinates[0]
        self.rect.y = coordinates[1]

    def update(self, position: (int, int) = None, position_plus: (int, int) = (0, 0)):
        if position:
            self.rect.x = position[0]
            self.rect.y = position[1]
        self.rect.x += position_plus[0]
        self.rect.y += position_plus[1]

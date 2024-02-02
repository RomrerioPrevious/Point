from abc import ABC
from pygame.sprite import Sprite, Group
import pygame


class Button(Sprite, ABC):
    def __init__(self, buttons_group: Group, coordinates: (int, int), image_path: str):
        super().__init__(buttons_group)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = coordinates[0]
        self.rect.y = coordinates[1]

    def click(self):
        ...

    def update(self):
        ...

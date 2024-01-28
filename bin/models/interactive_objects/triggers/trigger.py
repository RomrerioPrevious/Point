from abc import ABC
from pygame.sprite import Sprite, Group
import pygame


class Trigger(Sprite, ABC):
    def __init__(self, triggers_group: Group, point_group: Group, coordinates: (int, int)):
        super().__init__(triggers_group)
        self.image = pygame.image.load("resources/sprites/trigger.png")
        self.rect = self.image.get_rect()
        self.rect.x = coordinates[0]
        self.rect.y = coordinates[1]
        self.point = point_group

    def have_touch(self):
        if pygame.sprite.spritecollideany(self, self.point):
            self.action()

    def action(self, *args, **kwargs):
        ...

    def update(self):
        self.have_touch()

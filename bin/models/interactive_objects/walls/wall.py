from pygame.sprite import Sprite, Group
from bin.models.states import Direction
import pygame


class Wall(Sprite):
    def __init__(self, walls_group: Group, position: (int, int)):
        super().__init__(walls_group)
        self.image = pygame.image.load("resources/sprites/wall.png")
        self.image = pygame.transform.scale(self.image, (200, 1000))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

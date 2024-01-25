from pygame.sprite import Sprite
from bin.models.states import States
import pygame


class Point1D(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resources/sprites/point_1D.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, position: int = 0, condition: States = States.CALM):
        self.rect.x = position

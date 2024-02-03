from abc import ABC
from pygame.sprite import Sprite, Group
from bin.models.states import FontStates
import pygame


class Button(Sprite, ABC):
    def __init__(self, buttons_group: Group, coordinates: (int, int), name: str):
        super().__init__(buttons_group)
        self.name = name
        self.image = self.generate_text()
        self.rect = self.image.get_rect()
        self.rect.x = coordinates[0]
        self.rect.y = coordinates[1]

    def generate_text(self, active: FontStates = FontStates.NO_ACTIVE) -> pygame.Surface:
        if active:
            color = (255, 255, 255)
        else:
            color = (120, 120, 120)
        font = pygame.font.SysFont("pressstart2pregular", 32)
        text = font.render(self.name, 1, color)
        return text

    def click(self):
        ...

    def update(self):
        ...

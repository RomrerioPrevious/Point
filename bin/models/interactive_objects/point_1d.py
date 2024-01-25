from pygame.sprite import Sprite
from bin.models.states import States
import pygame


class Point1D(Sprite):
    def __init__(self, all_sprites):
        super().__init__(all_sprites)
        self.sprites = self.get_sprites()
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    @staticmethod
    def get_sprites() -> [Sprite]:
        size = (9, 9)
        sprites = []
        image = pygame.image.load("resources/sprites/point_1D.png")
        for rows in range(0, 9 * 2, 9):
            for columns in range(0, 9 * 4, 9):
                frame_location = (columns, rows)
                sprites.append(image.subsurface(pygame.Rect(frame_location, size)))
        sprites = list(map(lambda a: pygame.transform.scale(a, (75, 75)), sprites))
        return sprites

    def update(self, position: int = 0, condition: States = States.CALM):
        self.rect.x = position

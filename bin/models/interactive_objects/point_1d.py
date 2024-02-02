from icecream import ic
from pygame.sprite import Sprite, Group
from bin.models.states import PointStates
import pygame


class Point1D(Sprite):
    def __init__(self, all_sprites: Group):
        super().__init__(all_sprites)
        self.condition = PointStates.CALM
        self.sprites = self.get_sprites()
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 450
        self.tick = 0
        self.hp = 100
        self.speeds = {
            PointStates.CALM: 2,
            PointStates.PULL: 256,
            PointStates.DIE: 0
        }
        self.speed = self.speeds[PointStates.CALM]

    @staticmethod
    def get_sprites() -> [Sprite]:
        size = (9, 9)
        sprites = []
        image = pygame.image.load("resources/sprites/point_1D.png")
        for rows in range(0, 9 * 3, 9):
            for columns in range(0, 9 * 4, 9):
                frame_location = (columns, rows)
                sprites.append(image.subsurface(pygame.Rect(frame_location, size)))
        sprites = list(map(lambda a: pygame.transform.scale(a, (90, 90)), sprites))
        return sprites

    def damage(self, damage: int):
        self.hp -= damage
        if self.hp <= 0:
            self.dead()

    def dead(self):
        ...

    def update(self, position: int = None, condition: PointStates = PointStates.CALM, direction: int = 0):
        if condition and self.tick >= 10:
            self.tick = 0
            self.condition = condition
        match self.condition:
            case PointStates.CALM:
                self.calm(position, direction)
            case PointStates.PULL:
                self.pull(direction)
            case PointStates.DIE:
                self.dead()

    def calm(self, position: int, direction: int):
        if position:
            self.rect.x = position
        self.rect.x += direction * self.speeds[PointStates.CALM]
        self.tick += 1

    def pull(self, direction: int):
        if self.tick == 40:
            self.image = self.sprites[0]
            self.tick = 0
            self.speed = 2
            self.condition = PointStates.CALM
        else:
            if self.speed == 2:
                self.speed = direction * self.speeds[PointStates.PULL]
            self.rect.x += self.speed / (2 + (2 * self.tick))
            self.tick += 1

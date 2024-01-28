from pygame.sprite import Sprite, Group
from bin.models.states import PointStates
from bin.models.constants import Constants
import pygame


class Point1D(Sprite):
    def __init__(self, all_sprites: Group, enemy: Group):
        super().__init__(all_sprites)
        self.enemy = enemy
        self.condition = PointStates.CALM
        self.sprites = self.get_sprites()
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 450
        self.tick = 0
        self.hp = 100
        self.speed = 2

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

    def update(self, position: int = None, condition: PointStates = PointStates.CALM, position_plus: int = 0):
        if condition:
            self.condition = condition
        match self.condition:
            case PointStates.CALM:
                self.calm(position, position_plus)
            case PointStates.PULL:
                self.pull(position_plus)
            case PointStates.DIE:
                self.dead()

    def calm(self, position: int, position_plus: int):
        if position:
            self.rect.x = position
        self.rect.x += position_plus
        if pygame.sprite.spritecollideany(self, self.enemy):
            self.damage(10)

    def pull(self, position_plus: int):
        if self.tick == 48:
            self.image = self.sprites[0]
            self.tick = 0
            self.speed = 2
            self.condition = PointStates.CALM
        else:
            if not self.speed:
                self.speed = position_plus / 2
            self.rect.x += int((self.tick + 2) / self.speed)
            self.tick += 1

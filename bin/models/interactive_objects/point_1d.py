from icecream import ic
from pygame.sprite import Sprite, Group

from bin.models.constants import Constants
from bin.models.states import PointStates
import pygame


class Point1D(Sprite):
    def __init__(self, all_sprites: Group, screen):
        super().__init__(all_sprites)
        self.all_sprites = all_sprites
        self.screen = screen
        self.condition = PointStates.CALM
        self.sprites = self.get_sprites()
        self.image = self.sprites[3]
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 450
        self.tick = 0
        self.hp = 100
        self.speeds = {
            PointStates.CALM: 2,
            PointStates.DASH: 256,
            PointStates.DIE: 0
        }
        self.speed = self.speeds[PointStates.CALM]
        self.stop = False

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

    def dead(self):
        self.stop = True
        clock = pygame.time.Clock()
        group = self.all_sprites
        for i in range(30):
            self.screen.fill(Constants.BACKGROUND)
            self.image = self.sprites[int(8 + (i / 10))]
            group.draw(self.screen)
            pygame.display.flip()
            clock.tick(Constants.FPS)
        self.image = self.sprites[3]

    def update(self, position: int = None, condition: PointStates = PointStates.CALM, direction: int = 0):
        if self.stop:
            return
        if condition and self.tick >= 10:
            self.tick = 0
            self.condition = condition
        match self.condition:
            case PointStates.STOP:
                self.tick = 0
                self.calm(position, direction)
                self.condition = PointStates.CALM
            case PointStates.CALM:
                self.calm(position, direction)
            case PointStates.DASH:
                self.dash(direction)
            case PointStates.DIE:
                self.dead()
        self.tick += 1

    def calm(self, position: int, direction: int):
        if position:
            self.rect.x = position
        self.rect.x += direction * self.speeds[PointStates.CALM]

    def dash(self, direction: int):
        if self.tick == 40:
            self.image = self.sprites[0]
            self.tick = 0
            self.speed = 2
            self.condition = PointStates.CALM
        else:
            if self.speed == 2:
                self.speed = direction * self.speeds[PointStates.DASH]
                pygame.mixer.Sound("resources/sounds/actions/dash.mp3").play()
            if self.speed >= 0:
                self.image = self.sprites[int(1 + (self.tick / 15))]
            else:
                self.image = pygame.transform.rotate(self.sprites[int(1 + (self.tick / 15))], 180)
            self.rect.x += self.speed / (2 + (2 * self.tick))

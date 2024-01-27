from pygame.sprite import Sprite, Group
from bin.models.interactive_objects import Point1D
from bin.models.states import Direction
import pygame
import sys


class KeysController:
    def __init__(self, screen: pygame.Surface, all_sprites: Group, point: Point1D):
        self.screen = screen
        self.all_sprites = all_sprites
        self.point = point
        self.speed = 3

    def parse_event(self, event: pygame.event) -> Sprite | None:
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_LEFT:
                    self.point.update(position_plus=-self.speed)
                case pygame.K_RIGHT:
                    self.point.update(position_plus=self.speed)
                case pygame.K_x:
                    direction = self.direction()
                case pygame.K_c:
                    ...
        return None

    def pressed(self):
        direction = self.direction()
        match direction:
            case Direction.LEFT:
                self.point.update(position_plus=-self.speed)
            case Direction.RIGHT:
                self.point.update(position_plus=self.speed)

    @staticmethod
    def direction() -> Direction:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            return Direction.LEFT
        if keys[pygame.K_RIGHT]:
            return Direction.RIGHT

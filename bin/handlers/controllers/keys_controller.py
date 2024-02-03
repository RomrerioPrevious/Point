from bin.models.interactive_objects import Point1D
from bin.models.states import Direction, PointStates, GameStates
import pygame
import sys


class KeysController:
    def __init__(self, point: Point1D):
        self.point = point

    def parse_event(self, event: pygame.event) -> None:
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_LEFT:
                    self.point.update(direction=-1)
                case pygame.K_RIGHT:
                    self.point.update(direction=1)
                case pygame.K_x:
                    direction = self.direction()
                    if direction == 0:
                        direction = 1
                    self.point.update(condition=PointStates.DASH, direction=direction)
                case pygame.K_ESCAPE:
                    if self.state == GameStates.PAUSE:
                        self.state = GameStates.GAME
                    else:
                        self.state = GameStates.PAUSE

    def pressed(self) -> bool:
        direction = self.direction()
        match direction:
            case Direction.LEFT:
                self.point.update(direction=-1)
            case Direction.RIGHT:
                self.point.update(direction=1)
            case _:
                return False
        return True

    @staticmethod
    def direction() -> int:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            return Direction.LEFT
        if keys[pygame.K_RIGHT]:
            return Direction.RIGHT
        return 0

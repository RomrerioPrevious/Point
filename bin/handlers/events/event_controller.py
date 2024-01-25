from bin.models.interactive_objects import Point1D
from pygame.sprite import Sprite
import pygame
import sys


class EventController:
    def __init__(self, screen: pygame.display):
        self.screen = screen

    @staticmethod
    def parse_event(event: pygame.event) -> Sprite or None:
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_LEFT:
                    ...
                case pygame.K_RIGHT:
                    ...
                case pygame.K_x:
                    ...
        return None

from pygame.sprite import Sprite, Group
import pygame
import sys


class EventController:
    def __init__(self, screen: pygame.Surface, all_sprites: Group):
        self.screen = screen
        self.all_sprites = all_sprites

    def parse_event(self, event: pygame.event) -> Sprite | None:
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

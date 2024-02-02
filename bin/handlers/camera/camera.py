from pygame.sprite import Sprite, Group
import pygame


class Camera:
    def __init__(self, screen: pygame.Surface, all_sprites: Group, player: Sprite):
        self.screen = screen
        self.all_sprites = all_sprites
        self.player = player

    def follow_player(self):
        ...

    def shake(self, hard: int = 0):
        ...

    def move_and_stop(self):
        ...

import pygame


class Effects:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.tick = 0

    def shake(self, hard: float, rate: float):
        ...

    def glitch(self):
        ...

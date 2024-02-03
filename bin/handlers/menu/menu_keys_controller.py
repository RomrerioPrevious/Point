from icecream import ic
from pygame.sprite import Sprite, Group
from bin.models.menu.buttons import Button
from bin.models.states import FontStates
import pygame
import sys


class MenuKeysController:
    def __init__(self, buttons: [Button]):
        self.buttons = buttons
        self.pointer = 0
        self.previous = 0

    def parse_event(self, event: pygame.event) -> Button | None:
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_UP:
                    self.previous = self.pointer
                    button = self.buttons[self.previous]
                    button.update(FontStates.NO_ACTIVE)
                    self.pointer -= 1
                    if self.pointer == -1:
                        self.pointer = len(self.buttons) - 1
                    button = self.buttons[self.pointer]
                    button.update(FontStates.ACTIVE)
                case pygame.K_DOWN:
                    self.previous = self.pointer
                    button = self.buttons[self.previous]
                    button.update(FontStates.NO_ACTIVE)
                    self.pointer += 1
                    if self.pointer == len(self.buttons):
                        self.pointer = 0
                    button = self.buttons[self.pointer]
                    button.update(FontStates.ACTIVE)
                case pygame.K_c:
                    return self.buttons[self.pointer]
                case pygame.K_ESCAPE:
                    return None

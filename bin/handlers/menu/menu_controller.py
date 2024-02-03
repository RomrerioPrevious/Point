from icecream import ic
from pygame.sprite import Sprite, Group
from bin.handlers.menu.menu_keys_controller import MenuKeysController
from bin.models.constants import Constants
from bin.models.menu import Save
from bin.models.menu.buttons import *
from bin.models.deco import Deco
import pygame


class MenuController:
    def __init__(self, screen: pygame.Surface):
        self.group = Group()
        Deco(self.group, (0, 100), "resources/sprites/logo.png")
        self.buttons = self.generate_buttons()
        self.screen = screen
        self.controllers = {"keys": MenuKeysController(self.buttons)}

    def generate_buttons(self) -> [Button]:
        return [
            NewGame(self.group, (10, 250), "New game"),
            LoadGame(self.group, (10, 300), "Load game"),
            QuitGame(self.group, (10, 350), "Quit")
        ]

    def create_frame(self) -> None | Save:
        self.screen.fill(Constants.BACKGROUND)
        button = self.keys()
        save = self.button(button)
        self.group.draw(self.screen)
        pygame.display.flip()
        return save

    def keys(self) -> Button | None:
        controller = self.controllers["keys"]
        for event in pygame.event.get():
            button = controller.parse_event(event)
            if button:
                return button
        return None

    def button(self, button: Button) -> Save | None:
        save = None
        if button:
            save = button.click()
            if type(save) == dict:
                if "coins" in save.keys():
                    return save
                else:
                    self.load(save)
        return None

    def load(self, saves: dict[str, Save]):
        self.buttons = []
        del self.group
        self.group = Group()
        Deco(self.group, (0, 100), "resources/sprites/logo.png")
        for i, name in enumerate(saves.keys()):
            self.buttons.append(SaveButton(self.group, (10, 250 + (i * 50)), name))
        self.controllers["keys"].pointer = 0
        self.controllers["keys"].previous = 0
        self.controllers["keys"].buttons = self.buttons

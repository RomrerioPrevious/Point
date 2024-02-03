import sys
from pygame.sprite import Sprite, Group
from bin.models.menu import Save, SaveConstructors
from bin.models.states import FontStates
from bin.models.menu.buttons.button import Button
from bin.handlers.services import SaveService
from random import randint


class NewGame(Button):
    def __init__(self, buttons_group: Group, coordinates: (int, int), name: str):
        super().__init__(buttons_group, coordinates, "New Game")
        self.image = self.generate_text(FontStates.ACTIVE)

    def click(self) -> Save:
        service = SaveService()
        service.add_empty_save(f"Save {randint(1, 1000000)}")
        return SaveConstructors.create_empty_save()

    def update(self, active: FontStates = FontStates.NO_ACTIVE):
        self.generate_text(active)


class LoadGame(Button):
    def __init__(self, buttons_group: Group, coordinates: (int, int), name: str):
        super().__init__(buttons_group, coordinates, "Load Game")

    def click(self) -> [Save]:
        service = SaveService()
        return service.load_saves()

    def update(self, active: FontStates = FontStates.NO_ACTIVE):
        self.generate_text(active)


class QuitGame(Button):
    def __init__(self, buttons_group: Group, coordinates: (int, int), name: str):
        super().__init__(buttons_group, coordinates, "Quit")

    def click(self) -> None:
        sys.exit()

    def update(self, active: FontStates = FontStates.NO_ACTIVE):
        self.generate_text(active)


class SaveButton(Button):
    def __init__(self, buttons_group: Group, coordinates: (int, int), name: str):
        super().__init__(buttons_group, coordinates, name)

    def click(self) -> Save:
        service = SaveService()
        return service.load_save(self.name)
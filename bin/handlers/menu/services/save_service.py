from icecream import ic
from bin.models.menu import Save, SaveConstructors
import json


# SaveService is a class that give access to work with database with saves.
class SaveService:
    def __init__(self):
        self.saves = {}
        with open("resources/data/saves.json", encoding="UTF-8") as file:
            self.saves = json.load(file)

    def add_save_with_data(self, name: str, save: Save) -> None:
        self.saves[name] = save

    def add_empty_save(self, name: str) -> None:
        save = SaveConstructors.create_empty_save()
        self.add_save_with_data(name, save)

    def load_saves(self) -> dict[str: Save]:
        saves = {}
        for save in self.saves:
            saves[save] = self.load_save(save)
        return saves

    def load_save(self, name: str) -> Save:
        try:
            data = self.saves[name]
            save = SaveConstructors.create_save_by_dict(data)
            return save
        except KeyError as err:
            ic.prefix = "error | "
            ic(err)
            return SaveConstructors.create_empty_save()

    def update_save(self, name: str, new_save: Save) -> None:
        try:
            self.saves[name] = new_save
        except KeyError as err:
            ic.prefix = "error | "
            ic(err)
            return SaveConstructors.create_empty_save()

    def delete_save(self, name: str) -> None:
        try:
            del self.saves[name]
        except KeyError as err:
            ic.prefix = "error | "
            ic(err)
            return SaveConstructors.create_empty_save()

    def __del__(self):
        with open("resources/data/saves.json", "w", encoding="UTF-8") as file:
            json.dump(self.saves, file, indent=2)

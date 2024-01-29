from typing import TypedDict


class Save(TypedDict):
    background: int
    dialogs: list
    opened: list
    coins: int
    max_point: int


class SaveConstructors:
    @staticmethod
    def create_empty_save():
        return Save(
            background=1,
            dialogs=[],
            opened=[],
            coins=0,
            max_point=0
        )

    @staticmethod
    def create_save_by_dict(data: dict):
        return Save(
            background=data["background"],
            dialogs=data["dialogs"],
            opened=data["opened"],
            coins=data["coins"],
            max_point=data["max_point"],
        )

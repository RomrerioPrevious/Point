from bin.handlers import EventController
from bin.models.interactive_objects import Point1D, Enemy
from pygame.sprite import Sprite, Group
import pygame


def main():
    screen = init_window()
    all_sprites = {"All": Group(), "Enemy": Group()}
    point = Point1D(all_sprites["All"], all_sprites["Enemy"])
    controller = EventController(screen=screen,
                                 all_sprites_groups=all_sprites,
                                 main_character=point)
    while True:
        controller.create_frame()


def init_window() -> pygame.Surface:
    pygame.init()
    pygame.display.set_caption("Point")
    pygame.display.set_icon(pygame.image.load("resources/data/icon.png"))
    screen = pygame.display.set_mode((1600, 900))  # (1980, 1020)
    return screen


if __name__ == "__main__":
    main()

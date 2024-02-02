from bin.handlers import EventController
from bin.models.interactive_objects import Point1D, Obstacle
from pygame.sprite import Sprite, Group
from icecream import ic
import pygame


def main():
    screen = init_window()
    all_sprites = {"Point": Group(), "Enemy": Group(), "Triggers": Group(), "Decoration": Group(), "Walls": Group()}
    point = Point1D(all_sprites["Point"])
    controller = EventController(screen=screen,
                                 all_sprites_groups=all_sprites,
                                 main_character=point)
    Obstacle(all_sprites["Enemy"], (200, 400))
    while True:
        controller.create_frame()


def init_window() -> pygame.Surface:
    pygame.init()
    pygame.display.set_caption("Point")
    pygame.display.set_icon(pygame.image.load("resources/data/icon.png"))
    screen = pygame.display.set_mode((1600, 900))
    return screen


if __name__ == "__main__":
    main()

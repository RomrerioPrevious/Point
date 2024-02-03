from bin.handlers import EventController, MenuController
from bin.models.constants import Constants
from bin.models.interactive_objects import *
from pygame.sprite import Sprite, Group
from icecream import ic
import pygame


def main():
    screen = init_window()
    save = None
    controller = MenuController(screen)
    while not save:
        save = controller.create_frame()
    all_sprites = {"Point": Group(), "Enemy": Group(), "Triggers": Group(), "Decoration": Group(), "Walls": Group()}
    point = Point1D(all_sprites["Point"], screen)
    point_animation(point, all_sprites, screen)
    create_walls(all_sprites)
    controller = EventController(screen=screen,
                                 all_sprites_groups=all_sprites,
                                 main_character=point)
    while True:
        controller.create_frame()


def create_walls(all_sprites):
    Wall(all_sprites["Walls"], (-200, 300))
    Wall(all_sprites["Walls"], (1600, 300))


def point_animation(point, all_sprites, screen):
    clock = pygame.time.Clock()
    for i in range(30):
        point.image = point.sprites[int(3 + (i / 5))]
        all_sprites["Point"].draw(screen)
        pygame.display.flip()
        clock.tick(Constants.FPS)
    point.image = point.sprites[0]


def init_window() -> pygame.Surface:
    pygame.init()
    pygame.display.set_caption("Point")
    pygame.display.set_icon(pygame.image.load("resources/data/icon.png"))
    screen = pygame.display.set_mode((1600, 900))
    return screen


if __name__ == "__main__":
    main()

from bin.handlers import KeysController
from bin.models.interactive_objects import Point1D
from pygame.sprite import Sprite, Group
import pygame


def main():
    screen = init_window()
    all_sprites = {"All": Group(), "Enemy": Group()}
    point = Point1D(all_sprites["All"], all_sprites["Enemy"])
    controller = KeysController(screen, all_sprites["All"], point)
    update = None
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            update = controller.parse_event(event)
        controller.pressed()
        draw_sprites(all_sprites)
        pygame.display.flip()


def draw_sprites(all_sprites: dict[str, Group]):
    for group in all_sprites.items():
        if group is not Group():
            continue
        group.draw()


def init_window() -> pygame.Surface:
    pygame.init()
    pygame.display.set_caption("Point")
    pygame.display.set_icon(pygame.image.load("resources/data/icon.png"))
    screen = pygame.display.set_mode((1600, 900))  # (1980, 1020)
    return screen


if __name__ == "__main__":
    main()

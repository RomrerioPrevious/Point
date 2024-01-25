from bin.handlers import EventController
from bin.models.interactive_objects import Point1D
import pygame


def main():
    screen = init_window()
    all_sprites = pygame.sprite.Group()
    controller = EventController(screen, all_sprites)
    update = None
    x = 0
    while True:
        for event in pygame.event.get():
            update = controller.parse_event(event)
        all_sprites.draw(screen)
        pygame.display.flip()


def init_window() -> pygame.Surface:
    pygame.init()
    pygame.display.set_caption("Point")
    pygame.display.set_icon(pygame.image.load("resources/data/icon.png"))
    screen = pygame.display.set_mode((1600, 900))  # (1980, 1020)
    return screen


if __name__ == "__main__":
    main()

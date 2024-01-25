from bin.handlers import EventController
import pygame


def main():
    screen = init_window()
    controller = EventController(pygame.display)
    objects = pygame.sprite.Group()
    update = None
    while True:
        for event in pygame.event.get():
            update = controller.parse_event(event)
        pygame.display.flip()


def init_window() -> pygame.display:
    pygame.init()
    pygame.display.set_caption("Point")
    screen = pygame.display.set_mode((1600, 900))  # (1980, 1020)
    return screen


if __name__ == "__main__":
    main()

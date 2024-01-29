from .keys_controller import KeysController
from pygame.sprite import Group
from bin.models.constants import Constants
from bin.models.interactive_objects import Point1D
import pygame


class EventController:
    def __init__(self, screen: pygame.Surface, all_sprites_groups: dict[str, Group], main_character: Point1D):
        self.controllers = {"keys": KeysController(screen, main_character)}
        self.point = main_character
        self.all_sprites = all_sprites_groups
        self.screen = screen
        self.clock = pygame.time.Clock()

    # This function create and draw frame.
    def create_frame(self):
        self.screen.fill((0, 0, 0))
        self.check_the_keys()
        self.draw_sprites()
        pygame.display.flip()
        self.clock.tick(Constants.FPS)

    def check_the_keys(self):
        controller = self.controllers["keys"]
        for event in pygame.event.get():
            update = controller.parse_event(event)
        controller.pressed()
        controller.point.update()

    def triggers(self):
        ...

    def dialogs(self) -> bool:
        ...

    def draw_sprites(self):
        for group in self.all_sprites.values():
            group.draw(self.screen)

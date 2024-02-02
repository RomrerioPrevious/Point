from .keys_controller import KeysController
from .collisions_controller import CollisionController
from pygame.sprite import Group
from bin.models.constants import Constants
from bin.models.interactive_objects import Point1D
import pygame


class EventController:
    def __init__(self, screen: pygame.Surface, all_sprites_groups: dict[str, Group], main_character: Point1D):
        self.point = main_character
        self.all_sprites = all_sprites_groups
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.controllers = {"keys": KeysController(main_character),
                            "collision": CollisionController(main_character, all_sprites_groups)}

    # This function create and draw frame.
    def create_frame(self):
        self.screen.fill(Constants.BACKGROUND)
        self.check_the_keys()
        self.update_all()
        self.check_the_collision()
        self.draw_sprites()
        pygame.display.flip()
        self.clock.tick(Constants.FPS)

    def check_the_keys(self):
        controller = self.controllers["keys"]
        for event in pygame.event.get():
            controller.parse_event(event)
        if not controller.pressed():
            controller.point.update()

    def check_the_collision(self):
        controller = self.controllers["collision"]
        controller.check_collision()

    def triggers(self):
        ...

    def dialogs(self) -> bool:
        ...

    def draw_sprites(self):
        for group in self.all_sprites.values():
            group.draw(self.screen)

    def update_all(self):
        for i in self.all_sprites.keys():
            if i == "Point":
                continue
            self.all_sprites[i].update()

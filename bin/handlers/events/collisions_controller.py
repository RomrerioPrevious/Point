from bin.models.interactive_objects import Point1D
from bin.models.states import PointStates
from pygame.sprite import Sprite, Group
from icecream import ic
import pygame


class CollisionController:
    def __init__(self, main_character: Point1D, all_sprites_groups: dict[str, Group]):
        self.point = main_character
        self.all_sprites = all_sprites_groups

    def check_collision(self):
        if pygame.sprite.spritecollideany(self.point, self.all_sprites["Enemy"]):
            self.point.update(condition=PointStates.DAMAGE)
        if pygame.sprite.spritecollideany(self.point, self.all_sprites["Walls"]):
            ...
        if pygame.sprite.spritecollideany(self.point, self.all_sprites["Triggers"]):
            ...

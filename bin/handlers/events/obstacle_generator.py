from random import randint
from bin.models.interactive_objects import Obstacle


class ObstacleGenerator:
    def __init__(self, enemy_group):
        self.group = enemy_group

    def generate(self):
        Obstacle(self.group, (randint(0, 1550), 0))

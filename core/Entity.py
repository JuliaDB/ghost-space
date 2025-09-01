from abc import ABC, abstractmethod
from core.Const import EntityEnum

import pygame.image


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./assets/images/entities/level_1/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = EntityEnum.HEALTH[self.name]
        self.damage = EntityEnum.DAMAGE[self.name]
        self.score = EntityEnum.SCORE[self.name]
        self.last_dmg = 'None'

    @abstractmethod
    def move(self):
        pass

from core.Const import EnvEnum, EntityEnum
from core.Entity import Entity
import pygame


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.transform.scale(self.surf, EnvEnum.WINDOW_SIZE)
        self.rect = self.surf.get_rect(left=position[0], top=position[1])

    def move(self):
        self.rect.centerx -= EntityEnum.SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = EnvEnum.WINDOW_SIZE[0]

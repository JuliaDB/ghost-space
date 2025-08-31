import pygame.key

# from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
#     PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY
from core.Const import EntityEnum, EnvEnum, PlayerKeyEnum
from core.Entity import Entity
from core.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = EntityEnum.SHOT_DELAY[self.name]

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PlayerKeyEnum.KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= EntityEnum.SPEED[self.name]
        if pressed_key[PlayerKeyEnum.KEY_DOWN[self.name]] and self.rect.bottom < EnvEnum.WINDOW_SIZE[1]:
            self.rect.centery += EntityEnum.SPEED[self.name]
        if pressed_key[PlayerKeyEnum.KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= EntityEnum.SPEED[self.name]
        if pressed_key[PlayerKeyEnum.KEY_RIGHT[self.name]] and self.rect.right < EnvEnum.WINDOW_SIZE[0]:
            self.rect.centerx += EntityEnum.SPEED[self.name]
        pass

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = EntityEnum.SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PlayerKeyEnum.KEY_SHOOT[self.name]]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
            else:
                return None
        else:
            return None
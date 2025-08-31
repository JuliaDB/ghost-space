from core.Const import EntityEnum
from core.EnemyShot import EnemyShot
from core.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = EntityEnum.SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= EntityEnum.SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = EntityEnum.SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
from core.Const import EntityEnum
from core.Entity import Entity


class EnemyShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= EntityEnum.SPEED[self.name]

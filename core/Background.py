from core.Const import EnvEnum, EntityEnum
from core.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= EntityEnum.SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = EnvEnum.WINDOW_SIZE[0]

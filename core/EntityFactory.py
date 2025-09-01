import random

from core.Background import Background
from core.Const import EnvEnum
from core.Enemy import Enemy
from core.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        if entity_name == 'Level_1_':
            list_bg = []
            for i in range(4):  # level1bg images number
                list_bg.append(Background(f'Level_1_{i}', (0, 0)))
                list_bg.append(Background(f'Level_1_{i}', (EnvEnum.WINDOW_SIZE[0], 0)))
            return list_bg

        elif entity_name == 'Level2Bg':
            list_bg = []
            for i in range(5):  # level2bg images number
                list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                list_bg.append(Background(f'Level2Bg{i}', (EnvEnum.WINDOW_SIZE[0], 0)))
            return list_bg

        elif entity_name == 'Player1':
            return Player('Player1', (10, EnvEnum.WINDOW_SIZE[0] / 2 - 30))

        elif entity_name == 'Player2':
            return Player('Player2', (10, EnvEnum.WINDOW_SIZE[0] / 2 + 30))

        elif entity_name == 'Enemy1':
            return Enemy('Enemy1', (EnvEnum.WINDOW_SIZE[0] + 10, random.randint(40, EnvEnum.WINDOW_SIZE[1] - 40)))

        elif entity_name == 'Enemy2':
            return Enemy('Enemy2', (EnvEnum.WINDOW_SIZE[0] + 10, random.randint(40, EnvEnum.WINDOW_SIZE[1] - 40)))
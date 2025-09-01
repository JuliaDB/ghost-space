from enum import Enum
import pygame


class ColorEnum(Enum):
    ORANGE = (255, 128, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 128, 0)
    CYAN = (0, 128, 128)


class MenuEnum(str, Enum):
    NEW_GAME = "New Game"
    QUIT = "Quit"


class EntityEnum:
    SPEED = {
        'Level_1_0': 0,
        'Level_1_1': 1,
        'Level_1_2': 2,
        'Level_1_3': 3,
        # 'Level_1_4': 4,
        # 'Level_1_5': 5,
        # 'Level_1_6': 6,
        'Level2Bg0': 0,
        'Level2Bg1': 1,
        'Level2Bg2': 2,
        'Level2Bg3': 3,
        'Level2Bg4': 4,
        'Player1': 3,
        'Player1Shot': 1,
        'Player2': 3,
        'Player2Shot': 3,
        'Enemy1': 1,
        'Enemy1Shot': 5,
        'Enemy2': 1,
        'Enemy2Shot': 2,
    }
    HEALTH = {
        'Level_1_0': 999,
        'Level_1_1': 999,
        'Level_1_2': 999,
        'Level_1_3': 999,
        # 'Level1Bg4': 999,
        # 'Level1Bg5': 999,
        # 'Level1Bg6': 999,
        'Level2Bg0': 999,
        'Level2Bg1': 999,
        'Level2Bg2': 999,
        'Level2Bg3': 999,
        'Level2Bg4': 999,
        'Player1': 200,
        'Player1Shot': 1,
        'Enemy1': 50,
        'Enemy1Shot': 1,
        'Enemy2': 60,
        'Enemy2Shot': 1,
    }
    DAMAGE = {
        'Level_1_0': 0,
        'Level_1_1': 0,
        'Level_1_2': 0,
        'Level_1_3': 0,
        # 'Level1Bg4': 0,
        # 'Level1Bg5': 0,
        # 'Level1Bg6': 0,
        'Level2Bg0': 0,
        'Level2Bg1': 0,
        'Level2Bg2': 0,
        'Level2Bg3': 0,
        'Level2Bg4': 0,
        'Player1': 1,
        'Player1Shot': 25,
        'Player2': 1,
        'Player2Shot': 20,
        'Enemy1': 1,
        'Enemy1Shot': 20,
        'Enemy2': 1,
        'Enemy2Shot': 15,
    }
    SCORE = {
        'Level_1_0': 0,
        'Level_1_1': 0,
        'Level_1_2': 0,
        'Level_1_3': 0,
        # 'Level1Bg4': 0,
        # 'Level1Bg5': 0,
        # 'Level1Bg6': 0,
        'Level2Bg0': 0,
        'Level2Bg1': 0,
        'Level2Bg2': 0,
        'Level2Bg3': 0,
        'Level2Bg4': 0,
        'Player1': 0,
        'Player1Shot': 0,
        'Player2': 0,
        'Player2Shot': 0,
        'Enemy1': 100,
        'Enemy1Shot': 0,
        'Enemy2': 125,
        'Enemy2Shot': 0,
    }
    SHOT_DELAY = {
        'Player1': 20,
        'Player2': 15,
        'Enemy1': 100,
        'Enemy2': 200,
    }


class PlayerKeyEnum:
    KEY_UP = {'Player1': pygame.K_UP,
              'Player2': pygame.K_w}
    KEY_DOWN = {'Player1': pygame.K_DOWN,
                'Player2': pygame.K_s}
    KEY_LEFT = {'Player1': pygame.K_LEFT,
                'Player2': pygame.K_a}
    KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                 'Player2': pygame.K_d}
    KEY_SHOOT = {'Player1': pygame.K_SPACE,
                'Player2': pygame.K_RCTRL}



class EventEnum:
    ENEMY = pygame.USEREVENT + 1
    TIMEOUT = pygame.USEREVENT + 2


class EnvEnum:
    NAME_GAME = "Ghost Space"
    WINDOW_SIZE = (576, 324)
    BACKGROUND_MENU = 'assets/images/bg-menu.jpg'
    SOUND_MENU = 'assets/sounds/menu.mp3'
    MENU_OPTION_DEFAULT = MenuEnum.NEW_GAME
    SPAWN_TIME = 4000
    TIMEOUT_STEP = 100  # 100ms
    TIMEOUT_LEVEL = 60000  # 60s

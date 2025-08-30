from enum import Enum

class ColorEnum(Enum):
    ORANGE = (255, 128, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)

class MenuEnum(str, Enum):
    NEW_GAME = "New Game"
    SCORE = "Score"
    QUIT = "Quit"

class EnvEnum:
    NAME_GAME = "Ghost Space"
    WINDOW_SIZE = (576, 324)
    BACKGROUND_MENU = 'assets/images/bg-menu.jpg'
    SOUND_MENU = 'assets/sounds/menu.mp3'
    MENU_OPTION_DEFAULT = MenuEnum.NEW_GAME
    
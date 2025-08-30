from code.Const import EnvEnum, MenuEnum
from code.Menu import Menu
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(EnvEnum.WINDOW_SIZE)

    def run(self):
       while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MenuEnum.NEW_GAME:
                print("Starting New Game...")
            elif menu_return == MenuEnum.SCORE:
                print("Showing Scores...")
            elif menu_return == MenuEnum.QUIT:
                print("Quitting Game...")
                pygame.quit()
                quit()
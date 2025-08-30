from code.Const import EnvEnum
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
           print(menu_return)
from core.Const import EnvEnum, MenuEnum
from core.Menu import Menu
from core.Level import Level
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
                # player_score = [0, 0]  # [Player1, Player2]
                player_score = [0]  # [Player1]
                level = Level(self.window, 'Level_1_', menu_return, player_score)
                level_return = level.run(player_score)
                # if level_return:
                #     level = Level(self.window, 'Level2', menu_return, player_score)
                #     level_return = level.run(player_score)
                #     if level_return:
                #         score.save(menu_return, player_score)

            elif menu_return == MenuEnum.QUIT:
                print("Quitting Game...")
                pygame.quit()
                quit()

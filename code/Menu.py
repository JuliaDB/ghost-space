import pygame.image
from code.Const import EnvEnum, ColorEnum, MenuEnum
from pygame import Surface, Rect
from pygame.font import Font

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load(EnvEnum.BACKGROUND_MENU).convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load(EnvEnum.SOUND_MENU)
        pygame.mixer_music.play(-1)
        menu_option = EnvEnum.MENU_OPTION_DEFAULT

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            WIN_WIDTH_CENTER = EnvEnum.WINDOW_SIZE[0] / 2
            POSITION_INIT_TITLE = (WIN_WIDTH_CENTER, 70)

            # Título do jogo
            for word in EnvEnum.NAME_GAME.split():
                self.menu_text(50, word, ColorEnum.ORANGE.value, POSITION_INIT_TITLE)
                POSITION_INIT_TITLE = (POSITION_INIT_TITLE[0], POSITION_INIT_TITLE[1] + 50)

            # Menu
            options = list(MenuEnum)
            index = options.index(menu_option)

            for i, opcao in enumerate(options):
                color_text = ColorEnum.YELLOW.value if opcao == menu_option else ColorEnum.WHITE.value
                self.menu_text(20, opcao.value, color_text, (WIN_WIDTH_CENTER, 200 + 25 * i))

            pygame.display.flip()

            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # seta para baixo
                        if index < len(options) - 1:
                            menu_option = options[index + 1]
                        else:
                            menu_option = options[0]

                    elif event.key == pygame.K_UP:  # seta para cima
                        if index > 0:
                            menu_option = options[index - 1]
                        else:
                            menu_option = options[-1]

                    elif event.key == pygame.K_RETURN:  # ENTER
                        return menu_option.value

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
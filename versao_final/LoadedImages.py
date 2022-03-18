import os
from singleton import Singleton
import pygame
from pygame.locals import *
from filePaths import file_paths


class LoadedImages(Singleton):

    def __init__(self):
        super().__init__()
        self.tela = pygame.display.set_mode((800, 480))

        self.imagens_obtaculos = {'Spike': pygame.image.load(f'{file_paths.imagens}/FakeSpike01.png'),
                                  'Win': pygame.image.load(f'{file_paths.imagens}/win.png'),
                                  'Orb': pygame.image.load(f'{file_paths.imagens}/orb-yellow.png'),
                                  'Block': pygame.image.load(f'{file_paths.imagens}/block2.png'),
                                  'Portal': pygame.image.load(f'{file_paths.imagens}/portal.png'),
                                  'PortalSaida': pygame.image.load(f'{file_paths.imagens}/portal-saida.png')
                                  }

        self.imagens_telas = {
            'Menu_skin': self.__add_imagem('/menu_view/fundo_menuskins.png', 800, 480),
            'Menu_principal': self.__add_imagem('/menu_view/fundo_menu.png', 800, 480),
            'Menu_fases': self.__add_imagem('/menu_view/tela_fases.png', 800, 500),
            'Menu_instrucoes': self.__add_imagem('/menu_view/fundo_instrucoes.png', 800, 480)
        }

        self.imagens_botoes = {
            'Ret_select_rosa': self.__add_imagem('/menu_view/ret_menu.png', 100, 30),
            'Ret_select_rosa_120': self.__add_imagem('/menu_view/ret_menu.png', 120, 30),
        }

        self.skin_nave = pygame.image.load(
            f"{file_paths.imagens}/nave teste.png")

        self.imagens_skins = {'Padrão': pygame.image.load(f'{file_paths.imagens}/geo.png'),
                              'Azul': pygame.image.load(f'{file_paths.imagens}/geo blue.jpg'),
                              'Beta': pygame.image.load(f'{file_paths.imagens}/quadrado preto.png'),
                              'Mine': pygame.image.load(f'{file_paths.imagens}/mineblock.png'),
                              'Cubo Mágico': pygame.image.load(f'{file_paths.imagens}/cubomagico.jpg')}

        self.miniatura_fases = {
            'Blue': self.__add_imagem('/fase_01_miniatura.png', 100, 60),
            'Purple': self.__add_imagem('/fase_02_miniatura.png', 100, 60),
            'Green': self.__add_imagem('/fase_03_miniatura.png', 100, 60),
            'Orange': self.__add_imagem('/orange_miniatura.png', 100, 60)
        }

        self.bg_fase = {
            'Blue': pygame.image.load(f'{file_paths.imagens}/bg_blue.png'),
            'Purple': pygame.image.load(f'{file_paths.imagens}/bg_purple.jpg'),
            'Green': pygame.image.load(f'{file_paths.imagens}/bg_green.png'),
            'Orange': pygame.image.load(f'{file_paths.imagens}/bg_orange.png'),

        }

        self.floor_fase = {
            'Blue': pygame.image.load(f'{file_paths.imagens}/floor_blue.png'),
            'Purple': pygame.image.load(f'{file_paths.imagens}/floor_purple.png'),
            'Green': pygame.image.load(f'{file_paths.imagens}/floor_green.png'),
            'Orange': pygame.image.load(f'{file_paths.imagens}/floor_orange.png'),
        }

    def __add_imagem(self, file_name, size_x, size_y):
        image = pygame.image.load(
            f'{file_paths.imagens}/{file_name}')
        return pygame.transform.smoothscale(
            image.convert(), (size_x, size_y))


loaded_images = LoadedImages()

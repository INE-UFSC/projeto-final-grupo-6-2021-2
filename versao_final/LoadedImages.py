import os
from singleton import Singleton
import pygame
from pygame.locals import *
from filePaths import file_paths


class LoadedImages(Singleton):

    def __init__(self):
        super().__init__()
        current_directory = os.path.dirname(__file__)
        self.imagens_obtaculos = {'Spike': pygame.image.load(f'{file_paths.imagens}/FakeSpike01.png'),
                                  'Win': pygame.image.load(f'{file_paths.imagens}/win.png'),
                                  'Orb': pygame.image.load(f'{file_paths.imagens}/orb-yellow.png'),
                                  'Block': pygame.image.load(f'{file_paths.imagens}/block1.png'),
                                  'Portal': pygame.image.load(f'{file_paths.imagens}/portal.png'),
                                  'PortalSaida': pygame.image.load(f'{file_paths.imagens}/portal-saida.png')
                                  }


loaded_images = LoadedImages()

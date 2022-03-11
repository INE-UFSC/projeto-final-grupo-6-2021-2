import os
from singleton import Singleton
import pygame
from pygame.locals import *

class FilePaths(Singleton):

    def __init__(self):
        super().__init__()
        current_directory = os.path.dirname(__file__)
        self.musicas = os.path.join(current_directory, 'musicas')
        self.fontes = os.path.join(current_directory, 'fonts')
        self.imagens = os.path.join(current_directory, 'imagens')
        self.mapas = os.path.join(current_directory, 'mapas')

        self.imagens_obtaculos = {'Spike': pygame.image.load(f'{self.imagens}/FakeSpike01.png'),
                                  'Win': pygame.image.load(f'{self.imagens}/win.png'),
                                  'Orb': pygame.image.load(f'{self.imagens}/orb-yellow.png'),
                                  'Block': pygame.image.load(f'{self.imagens}/block1.png')
                                  }


file_paths = FilePaths()

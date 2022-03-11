import os
from singleton import Singleton


class FilePaths(Singleton):

    def __init__(self):
        super().__init__()
        current_directory = os.path.dirname(__file__)
        self.musicas = os.path.join(current_directory, 'musicas')
        self.fontes = os.path.join(current_directory, 'fonts')
        self.imagens = os.path.join(current_directory, 'imagens')
        self.mapas = os.path.join(current_directory, 'mapas')


file_paths = FilePaths()

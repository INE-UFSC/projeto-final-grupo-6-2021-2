from fase import Fase
from filePaths import file_paths
from LoadedImages import loaded_images


class ContainerFases():

    def __init__(self) -> None:
        self.fases = [
            Fase('Blue',
                 f'{file_paths.musicas}/undertale-megalovania.mp3',
                 f'{file_paths.mapas}/mapa_teste4.json',
                 loaded_images.bg_fase['Blue'],
                 loaded_images.floor_fase['Blue'],
                 loaded_images.miniatura_fases['Blue'], volume=0.5),
            Fase('Purple',
                 f'{file_paths.musicas}/billie-eilish-therefore-i-am.mp3',
                 f'{file_paths.mapas}/mapa_purple.json',
                 loaded_images.bg_fase['Purple'],
                 loaded_images.floor_fase['Purple'],
                 loaded_images.miniatura_fases['Purple'],
                 volume=0.5),
            Fase('Green',
                 f'{file_paths.musicas}/DigEx - Fall In Love [NCS Release].mp3',
                 f'{file_paths.mapas}/mapa_green.json',
                 loaded_images.bg_fase['Green'],
                 loaded_images.floor_fase['Green'],
                 loaded_images.miniatura_fases['Green'],
                 volume=0.5),
            Fase('Orange',
                 f'{file_paths.musicas}/Imagine-Dragons-J-I-D-Enemy.mp3',
                 f'{file_paths.mapas}/mapa_orange.json',
                 loaded_images.bg_fase['Orange'],
                 loaded_images.floor_fase['Orange'],
                 loaded_images.miniatura_fases['Orange'],
                 volume=0.5)

        ]

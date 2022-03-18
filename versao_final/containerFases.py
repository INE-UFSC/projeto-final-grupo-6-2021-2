from fase import Fase
from filePaths import file_paths
from LoadedImages import loaded_images


class ContainerFases():

    def __init__(self) -> None:
        self.fases = [
            Fase('Fase 1',
                 f'{file_paths.musicas}/undertale-megalovania.mp3',
                 f'{file_paths.mapas}/mapa_teste4.json',
                 f'{file_paths.imagens}/bg_blue.png',
                 f'{file_paths.imagens}/floor_blue.png',
                 loaded_images.miniatura_fases['Blue'], volume=0.2),
            Fase('Fase 2',
                 f'{file_paths.musicas}/billie-eilish-therefore-i-am.mp3',
                 f'{file_paths.mapas}/teste_voo.json',
                 f'{file_paths.imagens}/bg_purple.jpg',
                 f'{file_paths.imagens}/floor_purple.png',
                 loaded_images.miniatura_fases['Purple'],
                 volume=0.5),
            Fase('Fase 3',
                 f'{file_paths.musicas}/DigEx - Fall In Love [NCS Release].mp3',
                 f'{file_paths.mapas}/mapa_green.json',
                 f'{file_paths.imagens}/bg_green.png',
                 f'{file_paths.imagens}/floor_green.png',
                 loaded_images.miniatura_fases['Green'],
                 volume=0.2),
            Fase('Fase 4',
                 f'{file_paths.musicas}/Imagine-Dragons-J-I-D-Enemy.mp3',
                 f'{file_paths.mapas}/mapa_orange.json',
                 f'{file_paths.imagens}/bg_orange.png',
                 f'{file_paths.imagens}/floor_orange.png',
                 loaded_images.miniatura_fases['Orange'],
                 volume=0.2)

        ]

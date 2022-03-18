from fase import Fase
import os
from filePaths import file_paths


class ContainerFases():

    def __init__(self) -> None:
        self.fases = [
            Fase('Fase 1',
                 f'{file_paths.musicas}/undertale-megalovania.mp3',
                 f'{file_paths.mapas}/mapa_teste4.json',
                 f'{file_paths.imagens}/bg_blue.png',
                 f'{file_paths.imagens}/floor_blue.png', volume=0.2),
            Fase('Fase 2',
                 f'{file_paths.musicas}/music_bossfight-Vextron.mp3',
                 f'{file_paths.mapas}/teste_voo.json',
                 f'{file_paths.imagens}/bg_purple.jpg',
                 f'{file_paths.imagens}/floor_purple.png', volume=0.2),
            Fase('Fase 3',
                 f'{file_paths.musicas}/DigEx - Fall In Love [NCS Release].mp3',
                 f'{file_paths.mapas}/mapa_green.json',
                 f'{file_paths.imagens}/bg_green.png',
                 f'{file_paths.imagens}/floor_green.png', volume=0.2),
            Fase('Fase 4',
                 f'{file_paths.musicas}/Imagine-Dragons-J-I-D-Enemy.mp3',
                 f'{file_paths.mapas}/mapa_orange.json',
                 f'{file_paths.imagens}/bg_orange.png',
                 f'{file_paths.imagens}/floor_orange.png', volume=0.2)

        ]

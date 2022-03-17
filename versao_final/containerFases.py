from fase import Fase
import os
from filePaths import file_paths


class ContainerFases():

    def __init__(self) -> None:
        self.fases = [
            Fase('Fase 1',
                 f'{file_paths.musicas}/undertale-megalovania.mp3',
                 f'{file_paths.mapas}/mapa_teste4.json',
                 f'{file_paths.imagens}/bg_green.png',
                 f'{file_paths.imagens}/floor_green.png'),
            Fase('Fase 2',
                 f'{file_paths.musicas}/music_bossfight-Vextron.mp3',
                 f'{file_paths.mapas}/teste_voo.json',
                 f'{file_paths.imagens}/bg2_1.jpg',
                 f'{file_paths.imagens}/floor2.png', volume=0.2),

        ]

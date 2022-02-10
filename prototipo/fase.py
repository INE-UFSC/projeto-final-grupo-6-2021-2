import os
import json
from pygame import mixer


class Fase():

    def __init__(self, nome, musica, arquivo) -> None:
        self.__nome = nome
        self.__musica = musica
        self.__arquivo = arquivo

    @property
    def nome(self):
        return self.__nome

    @property
    def musica(self):
        return self.__musica

    @property
    def arquivo(self):
        return self.__arquivo

    def toca_musica(self):
        mixer.init()
        mixer.music.load(self.musica)
        mixer.music.play()

    def mapear_fase(self):
        #Carrega a lista com os dados do mapa e converte em uma matriz
        with open(self.arquivo) as f:
            data = json.load(f)
            linha = []
            mapa = []
            count = 0
            for x in data["layers"][0]['data']:
                linha.append(x)
                count += 1
                if count == 160:
                    count = 0
                    mapa.append(linha[:])
                    linha.clear()
            f.close()
        return mapa

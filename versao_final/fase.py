import pygame
import json


class Fase():

    def __init__(self, nome, musica, arquivo, bg, floor) -> None:
        self.__nome = nome
        self.__musica = musica
        self.__arquivo = arquivo
        self.__bg = pygame.image.load(bg)
        #self.__bg = pygame.transform.smoothscale(
        #    self.__bg.convert(), (1000, 480))
        self.mapa = self.mapear_fase()
        self.floor = pygame.image.load(floor)

    @property
    def nome(self):
        return self.__nome

    @property
    def musica(self):
        return self.__musica

    @property
    def arquivo(self):
        return self.__arquivo

    @property
    def bg(self):
        return self.__bg

    @bg.setter
    def bg(self, valor):
        self.__bg = valor

    def mapear_fase(self):
        # Carrega a lista com os dados do mapa e converte em uma matriz
        with open(self.arquivo) as f:
            data = json.load(f)
            linha = []
            mapa = []
            count = 0
            for x in data["layers"][0]['data']:
                linha.append(x)
                count += 1
                # Json cria apenas uma lista unidimensional, o mapa tem 320 quadrados em uma linha, portanto transformo em uma matriz
                if count == 360:
                    count = 0
                    mapa.append(linha[:])
                    linha.clear()
            f.close()
        return mapa

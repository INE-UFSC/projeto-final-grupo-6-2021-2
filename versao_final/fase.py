import json


class Fase():

    def __init__(self, nome, musica, arquivo, bg, floor, miniatura, volume=1) -> None:
        self.__nome = nome
        self.__musica = musica
        self.__arquivo = arquivo
        self.__volume_musica = volume
        self.__bg = bg
        self.mapa = self.mapear_fase()
        self.floor = floor
        self.miniatura = miniatura

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
    def volume_musica(self):
        return self.__volume_musica

    @property
    def bg(self):
        return self.__bg

    @bg.setter
    def bg(self, valor):
        self.__bg = valor

    def mapear_fase(self) -> list:
        '''Carrega a lista com os dados do mapa e converte em uma matriz'''
        with open(self.arquivo) as f:
            data = json.load(f)
            linha = []
            mapa = []
            count = 0
            for x in data["layers"][0]['data']:
                linha.append(x)
                count += 1
                # Json cria apenas uma lista unidimensional, o mapa tem 320 quadrados em uma linha, portanto transformo em uma matriz
                if count == 500:
                    count = 0
                    mapa.append(linha[:])
                    linha.clear()
            f.close()
        return mapa

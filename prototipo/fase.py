import os, json



class Fase():

    def __init__(self, nome, musica, arquivo) -> None:
        self.__nome = nome
        self.__musica = musica
        self.__arquivo = arquivo
        self.__mapeamento = self.mapear_fase()

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
    def mapeamento(self):
        return self.__mapeamento

    def mapear_fase(self):
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

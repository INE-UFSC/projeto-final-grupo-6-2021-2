import os, json


#Global directory
current_directory = os.path.dirname(__file__)
file_path_mapa = os.path.join(current_directory, 'Mapas')

class Fase():

    def __init__(self, nome, musica, arquivo) -> None:
        self.nome = nome
        self.musica = musica
        self.arquivo = arquivo
        self.mapeamento = self.mapear_fase()

    def mapear_fase(self):
        with open(self.arquivo) as f:
            data = json.load(f)
            linha = []
            mapa = []
            count = 0
            for x in data["layers"][1]['data']:
                linha.append(x)
                count += 1
                if count == 80:
                    count = 0
                    mapa.append(linha[:])
                    linha.clear()
            f.close()
        return mapa

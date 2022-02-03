from fase import Fase


class containerFases():

    def __init__(self, arquivoContainer) -> None:
        #fazer um metodo para pegar as fases de um .json
        #self.fases = pegar_fases(arquivoContainer)
        pass

    def criar_fase(self, nome, musica, arquivo):
        novafase = Fase(nome, musica, arquivo)
        #self.fases.append(novafase)
        #manda essa nova fase pro arquivo json também

    def pegar_fases(arquivoContainer):
        #pegas os mapas de um .json ou cria um caso não exista
        pass
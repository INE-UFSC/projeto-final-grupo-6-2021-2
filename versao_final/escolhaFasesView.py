import pygame
from pygame.locals import *
from botao_menu import Botao
from filePaths import file_paths
from fase import Fase
from LoadedImages import loaded_images
from containerFases import ContainerFases

class EscolhaFasesView():

    def __init__(self, tela) -> None:
     # devo pegar fases do container no futuro. e instanciar em outro lugar
        self.Containerfases = ContainerFases()

        fonte_botao = pygame.font.SysFont('calibri', 20)
        self.__tela = tela

        self.fundo = loaded_images.imagens_telas['Menu_fases']

        # só colocar texto não funcionou por enquanto
        self.fundo_fase = loaded_images.imagens_botoes['Ret_fase']

        # Lista deve ser automatizada no futuro. Atualmente, tuple com botao e fase (ou key voltar)
        self.lista_botoes = [
            (Botao(self.fundo_fase, 250, 225, 'Fase 01', fonte_botao,
             (255, 255, 255), (255, 137, 6)), self.Containerfases.fases[0]),
            (Botao(self.fundo_fase, 400, 225, 'Fase 02', fonte_botao,
             (255, 255, 255), (255, 137, 6)), self.Containerfases.fases[1]),

            (Botao(
                self.fundo_fase, 55, 25, 'Voltar', fonte_botao, (255, 255, 255), (255, 137, 6)), 'Voltar')
        ]

        # BOTÕES: jogar, skins, instrucoes, sair

    '''param :mouse_pos: entregue pelo pygame dentro do loop'''

    def desenha(self):
        self.__tela.blit(self.fundo, (0, 0))

        for botao_tup in self.lista_botoes:
            botao_tup[0].update(self.__tela)
            botao_tup[0].muda_cor()

        pygame.display.update()  # tela

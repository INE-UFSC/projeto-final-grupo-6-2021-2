import pygame
from pygame.locals import *
from botao_menu import Botao
from fase import Fase
from LoadedImages import loaded_images


class EscolhaFasesView():

    def __init__(self, tela, lista_fases: list[Fase]) -> None:
        fonte_botao = pygame.font.SysFont('calibri', 20)
        self.__tela = tela

        self.fundo = loaded_images.imagens_telas['Menu_fases']

        self.fundo_fase = loaded_images.imagens_botoes['Ret_fase']
        self.fundo_botao = loaded_images.imagens_botoes['Ret_select_rosa']

        self.lista_botoes = []
        x, y = 250, 225
        for fase in lista_fases:
            self.lista_botoes.append(
                (Botao(self.fundo_fase, x, y, fase.nome, fonte_botao,
                       (255, 255, 255), (255, 137, 6)), lista_fases.index(fase))
            )
            x += 150
            if x > 550:
                x = 250
                y = 375  # numeros nao testados

        self.lista_botoes.append(
            (Botao(
                self.fundo_botao, 55, 25, 'Voltar', fonte_botao, (255, 255, 255), (255, 137, 6)), 'Voltar')
        )
        # BOTÕES: jogar, skins, instrucoes, sair

    def desenha(self):
        self.__tela.blit(self.fundo, (0, 0))

        for botao_tup in self.lista_botoes:
            botao_tup[0].update(self.__tela)
            botao_tup[0].muda_cor()

        pygame.display.update()  # tela

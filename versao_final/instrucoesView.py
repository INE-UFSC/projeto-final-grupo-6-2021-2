import pygame
from pygame.locals import *
from botao_menu import Botao
from LoadedImages import loaded_images



class InstrucoesView():
    def __init__(self, tela):
        self.__tela = tela

        fonte_botao = pygame.font.SysFont('calibri', 20)
        self.fundo_menu = loaded_images.imagens_telas['Menu_instrucoes']
        self.fundo_botao = loaded_images.imagens_botoes['Ret_select_rosa']

        self.botao_voltar = Botao(imagem=self.fundo_botao, x_pos=55, y_pos=25,
                                  mensagem='Voltar', fonte=fonte_botao,
                                  cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6))

    def desenha(self):
        self.__tela.blit(self.fundo_menu, (0, 0))
        self.botao_voltar.muda_cor()
        self.botao_voltar.update(self.__tela)

        pygame.display.update()
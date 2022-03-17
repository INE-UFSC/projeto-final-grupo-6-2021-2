import pygame
from pygame.locals import *
from botao_menu import Botao
from abstractView import AbstractView



class InstrucoesView(AbstractView):
    def __init__(self, tela):
        super().__init__(tela, 'Menu_instrucoes')

        self.botao_voltar = Botao(imagem=self.fundo_botao, x_pos=55, y_pos=25,
                                  mensagem='Voltar', fonte=self.fonte_botao,
                                  cor_base_texto=self.COR_BASE_TEXTO, cor_mouse=self.COR_MOUSE)

    def desenha(self):
        self.tela.blit(self.fundo_tela, (0, 0))
        self.botao_voltar.muda_cor()
        self.botao_voltar.update(self.tela)

        pygame.display.update()
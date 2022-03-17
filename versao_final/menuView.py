import pygame
from pygame.locals import *
from botao_menu import Botao
from abstractView import AbstractView


class menuView(AbstractView):

    def __init__(self, tela) -> None:
        super().__init__(tela, 'Menu_principal')

        self.lista_botoes = [
            Botao(imagem=self.fundo_botao, x_pos=250, y_pos=350,
                  mensagem='Jogar', fonte=self.fonte_botao,
                  cor_base_texto=self.COR_BASE_TEXTO, cor_mouse=self.COR_MOUSE),
            Botao(imagem=self.fundo_botao, x_pos=360, y_pos=350,
                  mensagem='Skins', fonte=self.fonte_botao,
                  cor_base_texto=self.COR_BASE_TEXTO, cor_mouse=self.COR_MOUSE),
            Botao(imagem=self.fundo_botao, x_pos=470, y_pos=350,
                  mensagem='Instruções', fonte=self.fonte_botao,
                  cor_base_texto=self.COR_BASE_TEXTO, cor_mouse=self.COR_MOUSE),
            Botao(imagem=self.fundo_botao, x_pos=580, y_pos=350,
                  mensagem='Sair', fonte=self.fonte_botao,
                  cor_base_texto=self.COR_BASE_TEXTO, cor_mouse=self.COR_MOUSE)
        ]

    def desenha(self):
        self.tela.blit(self.fundo_tela, (0, 0))

        for botao in self.lista_botoes:
            botao.update(self.tela)
            botao.muda_cor()

        pygame.display.update()  # tela

        # se for True, o mouse esta acima do botao. me da (True, botao)
        # eu vou usar isso caso eu receba um click na tela. pego botao.mensagem para ver que func vou executar

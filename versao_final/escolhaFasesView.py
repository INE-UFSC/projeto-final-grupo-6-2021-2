import pygame
from pygame.locals import *
from botao_menu import Botao
from abstractView import AbstractView


class EscolhaFasesView(AbstractView):

    def __init__(self, tela, lista_fases) -> None:
        super().__init__(tela, 'Menu_fases')
        self.lista_botoes = []
        self.miniaturas = []

        x, y = 250, 225
        for fase in lista_fases:
            self.miniaturas.append(fase.miniatura)
            self.lista_botoes.append(
                (Botao(self.fundo_botao, x, y, fase.nome, self.fonte_botao,
                       self.COR_BASE_TEXTO, self.COR_MOUSE),
                 lista_fases.index(fase))
            )
            x += 150
            if x > 550:
                x = 250
                y = 360  # numeros nao testados

        self.lista_botoes.append(
            (Botao(
                self.fundo_botao, 55, 25, 'Voltar', self.fonte_botao,
                self.COR_BASE_TEXTO, self.COR_MOUSE), 'Voltar')
        )

    def desenha(self):
        self.tela.blit(self.fundo_tela, (0, 0))
        x_miniatura, y_miniatura = 200, 140
        for miniatura in self.miniaturas:
            self.tela.blit(miniatura, (x_miniatura, y_miniatura))
            x_miniatura += 150

            if x_miniatura > 535:
                x_miniatura = 200
                y_miniatura = 275

        for botao_tup in self.lista_botoes:
            botao_tup[0].update(self.tela)
            botao_tup[0].muda_cor()

        pygame.display.update()

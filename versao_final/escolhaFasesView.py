import pygame
from pygame.locals import *
from botao_menu import Botao
from LoadedImages import loaded_images
from abstractView import AbstractView


class EscolhaFasesView(AbstractView):

    def __init__(self, tela, lista_fases) -> None:
        super().__init__(tela, 'Menu_fases')

        self.fundo_botao_fase = loaded_images.imagens_botoes['Ret_fase']

        self.lista_botoes = []
        x, y = 250, 225
        for fase in lista_fases:
            self.lista_botoes.append(
                (Botao(self.fundo_botao, x, y, fase.nome, self.fonte_botao,
                       self.COR_BASE_TEXTO, self.COR_MOUSE), lista_fases.index(fase))
            )
            x += 150
            if x > 550:
                x = 250
                y = 350  # numeros nao testados

        self.lista_botoes.append(
            (Botao(
                self.fundo_botao, 55, 25, 'Voltar', self.fonte_botao, self.COR_BASE_TEXTO, self.COR_MOUSE), 'Voltar')
        )
        # BOTÕES: jogar, skins, instrucoes, sair

    def desenha(self):
        self.tela.blit(self.fundo_tela, (0, 0))
        x_miniatura, y_miniatura = 200, 140
        for miniatura in loaded_images.miniatura_fases.values():
            self.tela.blit(miniatura, (x_miniatura, y_miniatura))
            x_miniatura += 150

            if x_miniatura > 535:
                x_miniatura = 200
                y_miniatura = 275

        for botao_tup in self.lista_botoes:
            botao_tup[0].update(self.tela)
            botao_tup[0].muda_cor()

        pygame.display.update()  # tela

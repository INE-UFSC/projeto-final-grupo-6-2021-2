import pygame
from pygame.locals import *
from botao_menu import Botao
from filePaths import file_paths
from LoadedImages import loaded_images


class pauseView():

    def __init__(self) -> None:
        fonte_botao = pygame.font.SysFont('calibri', 20)
        self.tela = pygame.Surface([500, 200], SRCALPHA, 32)
        self.tela = self.tela.convert_alpha()
        self.tela.fill((255, 255, 255, 95))

        texto_mensagem = 'Jogo pausado'
        fontesys24 = pygame.font.SysFont('calibri', 24)
        self.tela_texto_mensagem = fontesys24.render(
            texto_mensagem, 1, (0, 0, 0))

        self.fundo_botao = loaded_images.imagens_botoes['Ret_select_rosa']

        self.lista_botoes = [
            Botao(imagem=self.fundo_botao, x_pos=240, y_pos=280,
                  mensagem='Continuar', fonte=fonte_botao,
                  cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)),
            Botao(imagem=self.fundo_botao, x_pos=350, y_pos=280,
                  mensagem='Menu', fonte=fonte_botao,
                  cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)),
            Botao(imagem=self.fundo_botao, x_pos=460, y_pos=280,
                  mensagem='Resetar', fonte=fonte_botao,
                  cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)),
            Botao(imagem=self.fundo_botao, x_pos=570, y_pos=280,
                  mensagem='Sair', fonte=fonte_botao,
                  cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)),
        ]

    def desenha(self, tela):
        for botao in self.lista_botoes:
            botao.update(tela)
            botao.muda_cor()

        tela.blit(self.tela_texto_mensagem, (320, 200))

        pygame.display.update()

    def removeView(self, tela):
        self.tela.fill(0, 0, 0, 0)

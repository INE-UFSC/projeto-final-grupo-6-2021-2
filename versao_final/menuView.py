import pygame
from pygame.locals import *
from botao_menu import Botao
from filePaths import file_paths
from LoadedImages import loaded_images


class menuView():

    def __init__(self, tela) -> None:
        fonte_botao = pygame.font.SysFont('calibri', 20)
        self.__tela = tela

        self.fundo_menu = loaded_images.imagens_telas['Menu_principal']
        self.fundo_botao = loaded_images.imagens_botoes['Ret_select_rosa']

        self.lista_botoes = [
            Botao(imagem=self.fundo_botao, x_pos=250, y_pos=350,
                  mensagem='Jogar', fonte=fonte_botao,
                  cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)),
            Botao(imagem=self.fundo_botao, x_pos=360, y_pos=350,
                  mensagem='Skins', fonte=fonte_botao,
                  cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)),
            Botao(imagem=self.fundo_botao, x_pos=470, y_pos=350,
                  mensagem='Instruções', fonte=fonte_botao,
                  cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)),
            Botao(imagem=self.fundo_botao, x_pos=580, y_pos=350,
                  mensagem='Sair', fonte=fonte_botao,
                  cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6))
        ]

    def desenha(self):
        self.__tela.blit(self.fundo_menu, (0, 0))

        for botao in self.lista_botoes:
            botao.update(self.__tela)
            botao.muda_cor()

        pygame.display.update()  # tela

        # se for True, o mouse esta acima do botao. me da (True, botao)
        # eu vou usar isso caso eu receba um click na tela. pego botao.mensagem para ver que func vou executar

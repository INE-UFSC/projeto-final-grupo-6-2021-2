import pygame
from pygame.locals import *
from botao_menu import Botao
from filePaths import file_paths


class menuView():

    def __init__(self) -> None:
        pygame.init()
     #      fontesys60 = pygame.font.SysFont('calibri', 60)
        fonte_botao = pygame.font.SysFont('calibri', 20)
        self.__tela = pygame.display.set_mode(
            (800, 500))

        self.fundo_menu = pygame.image.load(
            f'{file_paths.imagens}/menu_view/fundo_menu.png')
        self.fundo_menu = pygame.transform.smoothscale(
            self.fundo_menu.convert(), (800, 480))

        self.fundo_botao = pygame.image.load(
            f'{file_paths.imagens}/menu_view/ret_menu.png')

        self.fundo_botao = pygame.transform.smoothscale(
            self.fundo_botao.convert(), (100, 30))

        self.lista_botoes = [
            Botao(imagem=self.fundo_botao, x_pos=250, y_pos=350, mensagem='Jogar',
                  fonte=fonte_botao, cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)),
            Botao(imagem=self.fundo_botao, x_pos=360, y_pos=350, mensagem='Skins',
                  fonte=fonte_botao, cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)),
            Botao(imagem=self.fundo_botao, x_pos=470, y_pos=350, mensagem='Instruções',
                  fonte=fonte_botao, cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)),
            Botao(imagem=self.fundo_botao, x_pos=580, y_pos=350, mensagem='Sair',
                  fonte=fonte_botao, cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6))
        ]

        # BOTÕES: jogar, skins, instrucoes, sair

    '''param :mouse_pos: entregue pelo pygame dentro do loop'''

    def desenha(self, mouse_pos):
        self.__tela.blit(self.fundo_menu, (0, 0))

        for botao in self.lista_botoes:
            botao.update(self.__tela)
            botao.muda_cor(mouse_pos)


#      self.__tela.blit(tela_texto_opcoes, (220, 280))
        pygame.display.update()  # tela

        # se for True, o mouse esta acima do botao. me da (True, botao)
        # eu vou usar isso caso eu receba um click na tela. pego botao.mensagem para ver que func vou executar

import pygame
from pygame.locals import *


class menuView():

    def __init__(self) -> None:
        self.__tela = pygame.display.set_mode(
            (800, 480))

    def desenha(self):
        pygame.mixer.music.stop()
        self.__tela.fill((0, 0, 0))
        texto_mensagem = 'MENU'
        texto_opcoes = 'Aperte tab para iniciar e ESC para sair'
        fontesys60 = pygame.font.SysFont('calibri', 60)
        fontesys24 = pygame.font.SysFont('calibri', 24)
        tela_texto_mensagem = fontesys60.render(
            texto_mensagem, 1, (255, 255, 255))
        tela_texto_opcoes = fontesys24.render(texto_opcoes, 1, (255, 255, 255))
        self.__tela.blit(tela_texto_mensagem, (240, 200))
        self.__tela.blit(tela_texto_opcoes, (220, 280))
        pygame.display.update()  # tela

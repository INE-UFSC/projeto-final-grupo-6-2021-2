import pygame
from pygame.locals import *
from botao_menu import Botao
from skin import Skin



class MenuSkin():

    def __init__(self):
        fonte = pygame.font.SysFont('calibri', 24)
        self.__skins = [
            Skin('Padrão', 'geo.png'),
            Skin('Quadrado Preto', 'quadrado preto.png'),
            Skin('Azul', 'geo blue.jpg')
        ]
        self.__lista_botoes = [
            Botao(None, 400, 100, "Padrão", fonte, "Black", "Green"),
            Botao(None, 400, 250, "Azul", fonte, "Black", "Green"),
            Botao(None, 400, 400, "Beta", fonte, "Black", "Green")
        ]
    
    def inicia(self, tela):
        while True:
            mouse_pos = pygame.mouse.get_pos()

            tela.fill("white")

            for botao in self.__lista_botoes:
                botao.muda_cor(mouse_pos)


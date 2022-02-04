import pygame
from pygame.locals import *
import os

current_directory = os.path.dirname(__file__)
file_path_image = os.path.join(current_directory, 'imagens')

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.__x = 50
        self.__y = 468
        self.__velocidade_pulo = 8
        self.__altura_pulo = 410
        self.__gravidade = 0.5
        self.__pulando = False

        # Criação do retângulo
        self.__image = pygame.image.load(f"{file_path_image}/quadrado preto.png")
        self.__rect = self.image.get_rect()

        # Posicionamento do retângulo
        self.__rect.topleft = (self.__x, self.__y)

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect

    def pular(self):
        if self.__rect.y == self.__y:
            self.__pulando = True

    def update(self):       
        '''Mecanica de movimento do pulo'''
        if self.__pulando:
            if self.__rect.y <= self.__altura_pulo:
                self.__pulando = False
                self.__velocidade_pulo = 0
            self.__rect.y -= self.__velocidade_pulo
            self.__velocidade_pulo -= self.__gravidade
        
        else:
            if self.__rect.y < self.__y:
                self.__rect.y += self.__velocidade_pulo
                self.__velocidade_pulo += self.__gravidade
            else:
                self.__rect.y = self.__y
                self.__velocidade_pulo = 8

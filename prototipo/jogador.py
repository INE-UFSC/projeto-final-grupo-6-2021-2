import pygame
from pygame.locals import *
import os
from pygame.math import Vector2
from obstaculos import *



current_directory = os.path.dirname(__file__)
file_path_image = os.path.join(current_directory, 'imagens')

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.__x = 100
        self.__y = 432
        self.__velocidade = Vector2(1, 0)
        self.__gravidade = 0.5
        self.__pulando = False
        self.__nochao = True

        # Criação do retângulo
        self.__image = pygame.image.load(f"{file_path_image}/geo.png")
        self.__image = pygame.transform.scale(self.__image, (24, 24))
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

    @property
    def nochao(self):
        return self.__nochao

    @property
    def pulando(self):
        return self.__pulando

    @property
    def gravidade(self):
        return self.__gravidade

    @property
    def velocidade(self):
        return self.__velocidade

    def pular(self):
        if self.nochao:
            self.__pulando = True
            self.__velocidade.y = -8
    
    def collide(self, yvel, grupo):

        # Verificação das colisões 
        for x in grupo:
            if pygame.sprite.collide_rect(self, x):
                if isinstance(x, Block):
                    if yvel > 0:
                        self.rect.bottom = x.rect.top
                        self.__velocidade.y =  0
                        self.__pulando = False
                        self.__nochao = True
                    elif yvel < 0:
                        self.rect.top = x.rect.bottom 
                    else:
                        self.__velocidade.x = 0
                        self.rect.right = x.rect.left
                        self.died = True

    def update(self, grupo):
            
        # Caso não encoste no chão, a gravidade começa a agir no jogador
        if not self.nochao:
            self.__velocidade.y += self.__gravidade
            self.collide(0, grupo)

        self.rect.top += self.__velocidade.y
        self.__nochao = False
        self.collide(self.__velocidade.y, grupo)
            
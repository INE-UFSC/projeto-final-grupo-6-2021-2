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
        self.__velocidade = Vector2(3, 0)
        self.__gravidade = 0.5
        self.__pulando = False
        self.__nochao = True
        self.__morte = False

        # Criação do retângulo
        self.__image = pygame.image.load(f"{file_path_image}/geo.png")
        self.__image = pygame.transform.scale(self.__image, (24, 24))
        self.__rect = self.image.get_rect()

        # Posicionamento do retângulo
        self.__rect.topleft = (self.__x, self.__y)

    @property
    def morte(self):
        return self.__morte
    
    @morte.setter
    def morte(self, status):
        self.__morte = status

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, valor):
        self.__x = valor
    
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

    @velocidade.setter
    def velocidade(self, valor):
        self.__velocidade = valor

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
                        self.__morte = True
                        self.__velocidade.x = 0
                    else:
                        self.rect.right = x.rect.left
                        self.__morte = True
                        # Caso o personagem morra, ele fica parado
                        self.__velocidade.x = 0

                if isinstance(x, Spike):
                    self.__morte = True
                    self.__velocidade.x = 0

    def update(self, grupo):


    
        # Caso não encoste no chão, a gravidade começa a agir no jogador
        if not self.__morte:
            if not self.nochao:
                self.__velocidade.y += self.__gravidade
                self.collide(0, grupo)

            self.rect.top += self.__velocidade.y
            self.__nochao = False
            self.collide(self.__velocidade.y, grupo)

    def resetar(self):
        self.__x = 100
        self.__y = 432
        self.__velocidade = Vector2(3, 0)
        self.__gravidade = 0.5
        self.__pulando = False
        self.__nochao = True
        self.__morte = False
        self.__rect.topleft = (self.__x, self.__y)
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
    def x(self):
        return self.__x

    @x.setter
    def x(self, valor):
        self.__x = valor

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, valor):
        self.__y = valor

    @property
    def velocidade(self):
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, valor):
        self.__velocidade = valor

    @property
    def gravidade(self):
        return self.__gravidade
    
    @gravidade.setter
    def gravidade(self, valor):
        self.__gravidade = valor

    @property
    def pulando(self):
        return self.__pulando
    
    @pulando.setter
    def pulando(self, valor):
        self.__pulando = valor

    @property
    def nochao(self):
        return self.__nochao
    
    @nochao.setter
    def nochao(self, valor):
        self.__nochao = valor

    @property
    def morte(self):
        return self.__morte

    @morte.setter
    def morte(self, status):
        self.__morte = status

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, status):
        self.__rect = status

    def pular(self):
        if self.nochao:
            self.pulando = True
            self.velocidade.y = -8

    def collide(self, yvel, grupo):

        # Verificação das colisões
        for x in grupo:
            if pygame.sprite.collide_rect(self, x):
                if isinstance(x, Block):
                    if yvel > 0:
                        self.rect.bottom = x.rect.top
                        self.velocidade.y = 0
                        self.pulando = False
                        self.nochao = True
                    elif yvel < 0:
                        self.rect.top = x.rect.bottom
                        self.morte = True
                        self.velocidade.x = 0
                    else:
                        self.rect.right = x.rect.left
                        self.morte = True
                        # Caso o personagem morra, ele fica parado
                        self.velocidade.x = 0

                if isinstance(x, Spike):
                    self.morte = True
                    self.velocidade.x = 0

    def update(self, grupo):

        # Caso não encoste no chão, a gravidade começa a agir no jogador
        if not self.morte:
            if not self.nochao:
                self.velocidade.y += self.gravidade
                self.collide(0, grupo)

            self.rect.top += self.velocidade.y
            self.nochao = False
            self.collide(self.velocidade.y, grupo)

    def resetar(self):
        self.x = 100
        self.y = 432
        self.velocidade = Vector2(3, 0)
        self.gravidade = 0.5
        self.pulando = False
        self.nochao = True
        self.morte = False
        self.rect.topleft = (self.x, self.y)

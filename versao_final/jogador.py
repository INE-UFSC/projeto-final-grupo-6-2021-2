import pygame
from pygame.locals import *
from filePaths import file_paths
from pygame.math import Vector2
from obstaculos import *
from skin import Skin


class Jogador(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.__x = 100
        self.__y = 432
        self.__velocidade = Vector2(3, 0)
        self.__gravidade = 0.7
        self.__pulando = False
        self.__nochao = True
        self.__morte = False
        self.__vitoria = False
        self.__angulo = 0
        self.__skin_atual = Skin('Padrão', 'geo.png') # Skin padrão

        # Criação do retângulo
        self.__image = pygame.image.load(f"{file_paths.imagens}/{self.__skin_atual.arquivo}")
        self.__image = pygame.transform.scale(self.__image, (24, 24))
        self.__rect = self.image.get_rect()

        self.__mask = pygame.mask.Mask(fill=True, size=self.__image.get_size())

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
    def vitoria(self):
        return self.__vitoria

    @vitoria.setter
    def vitoria(self, status):
        self.__vitoria = status

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, status):
        self.__image = status

    @property
    def angulo(self):
        return self.__angulo

    @angulo.setter
    def angulo(self, status):
        self.__angulo = status

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, status):
        self.__rect = status

    @property
    def mask(self):
        return self.__mask

    @mask.setter
    def mask(self, value):
        self.__mask = value

    @property
    def skin_atual(self):
        return self.__skin_atual

    @skin_atual.setter
    def skin_atual(self, value):
        self.__skin_atual = value

    def pular(self):
        if self.nochao:
            self.pulando = True
            self.velocidade.y = - 8.5

    def rotate(self, image, rect, angulo):
        new_image = pygame.transform.rotate(image, angulo)
        self.angulo += angulo
        rect = new_image.get_rect(center=rect.center)
        return new_image, rect


    def resetar(self):
        # Reseta todos os valores para os padrão para resetar a fase
        self.x = 100
        self.y = 432
        self.velocidade = Vector2(3, 0)
        self.gravidade = 0.7
        self.pulando = False
        self.nochao = True
        self.morte = False
        self.rect.topleft = (self.x, self.y)
        self.image, self.rect = self.rotate(
            self.image, self.rect, -self.angulo)

    def muda_skin(self, skin):
        # Criação do retângulo
        self.__skin_atual = skin
        self.__image = pygame.image.load(f"{file_paths.imagens}/{self.__skin_atual.arquivo}")
        self.__image = pygame.transform.scale(self.__image, (24, 24))
        self.__rect = self.image.get_rect()

        self.__mask = pygame.mask.Mask(fill=True, size=self.__image.get_size())

        # Posicionamento do retângulo
        self.__rect.topleft = (self.__x, self.__y)

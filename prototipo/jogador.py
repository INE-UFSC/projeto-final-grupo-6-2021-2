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
        self.__gravidade = 0.7
        self.__pulando = False
        self.__nochao = True
        self.__morte = False
        self.__vitoria = False
        self.__angulo = 0

        # Criação do retângulo
        self.__image = pygame.image.load(f"{file_path_image}/geo.png")
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

    def pular(self):
        if self.nochao:
            self.pulando = True
            self.velocidade.y = -8

    def rotate(self, image, rect, angulo):
        new_image = pygame.transform.rotate(image, angulo)
        self.angulo += angulo
        rect = new_image.get_rect(center=rect.center)
        return new_image, rect

    def collide(self, yvel, grupo):

        # Verificação das colisões
        for x in grupo:
            if pygame.sprite.spritecollide(self, [x], False, pygame.sprite.collide_mask):
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
                        self.velocidade.x = 0 # Caso o personagem morra, ele fica parado

                if isinstance(x, Spike):
                    self.morte = True
                    self.velocidade.x = 0

                '''tirar o comentário e preencher após a criação do obstáculo de vitória
                if isinstance(x, (Preencher com classe do obstáculo de vitória)):
                    self.vitoria = True
                    self.velocidade.x = 0
                '''

    def update(self, grupo):

        # Caso não encoste no chão, a gravidade começa a agir no jogador
        if not self.morte:
            if not self.nochao:
                self.velocidade.y += self.gravidade
                #Verifica colisão no eixo X
                self.collide(0, grupo)

            if self.velocidade.y == -8:
                self.image, self.rect = self.rotate(self.image, self.rect, -90)

            self.rect.top += self.velocidade.y
            self.nochao = False
            #Verifica colisão no eixo Y
            self.collide(self.velocidade.y, grupo)

    def resetar(self):
        #Reseta todos os valores para os padrão para resetar a fase
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

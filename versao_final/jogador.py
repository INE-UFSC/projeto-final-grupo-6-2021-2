import pygame
from pygame.locals import *
from pygame.math import Vector2
from obstaculos import *
from containerSkins import *


class Jogador(pygame.sprite.Sprite):

    def __init__(self, container_skin: ContainerSkins):
        super().__init__()
        self.__x = 100
        self.__y = 432
        self.__velocidade = Vector2(3, 0)
        self.__gravidade = 0.7
        self.__pulando = False
        self.__forca_pulo = 8.5
        self.__nochao = True
        self.__morte = False
        self.__vitoria = False
        self.__voo = False
        self.__angulo = 0
        self.__skin_atual = container_skin.skins_quadrado[0]
        self.__skin_nave = container_skin.skin_nave
        imagem, mask, rect = self.__cria_e_posiciona_retangulo()
        self.__image = imagem
        self.__mask = mask
        self.__rect = rect

    @property
    def voo(self):
        return self.__voo

    @voo.setter
    def voo(self, valor):
        self.__voo = valor

    @property
    def forca_pulo(self):
        return self.__forca_pulo

    @forca_pulo.setter
    def forca_pulo(self, valor):
        self.__forca_pulo = valor

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

    @property
    def skin_nave(self):
        return self.__skin_nave

    @skin_nave.setter
    def skin_nave(self, valor):
        self.__skin_nave = valor

    def __cria_e_posiciona_retangulo(self):
        imagem = self.__skin_atual.arquivo
        imagem_escalonada = pygame.transform.scale(imagem, (24, 24))
        rect = imagem_escalonada.get_rect()
        mask = pygame.mask.Mask(fill=True, size=imagem_escalonada.get_size())
        rect.topleft = (self.__x, self.__y)
        return imagem_escalonada, mask, rect

    def pular(self):
        self.pulando = True
        self.velocidade.y = - self.forca_pulo
        if not self.voo:
            self.image, self.rect = self.rotate(self.image, self.rect, -90)

    def rotate(self, image, rect, angulo):
        new_image = pygame.transform.rotate(image, angulo)
        self.angulo += angulo
        rect = new_image.get_rect(center=rect.center)
        return new_image, rect

    def resetar(self):
        # Reseta todos os valores para os valores default do jogador
        self.x = 100
        self.y = 432
        self.velocidade = Vector2(3, 0)
        self.gravidade = 0.7
        self.pulando = False
        self.nochao = True
        self.morte = False
        self.voo = False
        self.vitoria = False
        self.forca_pulo = 8.5
        self.muda_skin(self.skin_atual)
        self.image, self.rect = self.rotate(
            self.image, self.rect, -self.angulo)

    def muda_skin(self, skin):
        self.skin_atual = skin
        imagem, mask, rect = self.__cria_e_posiciona_retangulo()
        self.__image = imagem
        self.__mask = mask
        self.__rect = rect

    def transforma_nave(self):
        imagem = loaded_images.skin_nave
        imagem_escalonada = pygame.transform.scale(imagem, (46, 24))
        rect = imagem_escalonada.get_rect()
        mask = pygame.mask.Mask(fill=True, size=imagem_escalonada.get_size())
        coords = self.__rect.topleft
        rect.topleft = coords
        self.__image = imagem_escalonada
        self.__mask = mask
        self.__rect = rect

    def transforma_jogador(self):
        imagem = self.__skin_atual.arquivo
        imagem_escalonada = pygame.transform.scale(imagem, (24, 24))
        rect = imagem_escalonada.get_rect()
        mask = pygame.mask.Mask(fill=True, size=imagem_escalonada.get_size())
        coords = self.__rect.topleft
        rect.topleft = coords
        self.__image = imagem_escalonada
        self.__mask = mask
        self.__rect = rect

    def parar_jogador(self):
        self.velocidade = Vector2(0, 0)
        self.pulando = False

    def continuar_jogador(self):
        self.velocidade = Vector2(3, 0)

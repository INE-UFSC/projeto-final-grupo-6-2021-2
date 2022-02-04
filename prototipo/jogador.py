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
        self.__y = 424
        self.__velocidade_pulo = 8
        self.__altura_pulo = 410
        self.__gravidade = 0.5
        self.__pulando = False
        self.__nochao = True
        self.vel = Vector2(1, 0)

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

    @property
    def nochao(self):
        return self.__nochao

    @property
    def pulando(self):
        return self.__pulando

    @property
    def gravidade(self):
        return self.__gravidade

    def pular(self):
        if self.nochao:
            self.__pulando = True
            self.vel.y = -8
    
    def collide(self, yvel, grupo):

        for x in grupo:
            if pygame.sprite.collide_rect(self, x):
                if isinstance(x, Block):
                    if yvel > 0:
                        self.rect.bottom = x.rect.top
                        self.vel.y =  0
                        self.__pulando = False
                        self.__nochao = True
                    elif yvel < 0:
                        """if yvel is (-),player collided while jumping"""
                        self.rect.top = x.rect.bottom  # player top is set the bottom of block like it hits it head
                    else:
                        """otherwise, if player collides with a block, he/she dies."""
                        self.vel.x = 0
                        self.rect.right = x.rect.left  # dont let player go through walls
                        self.died = True

    def update(self, grupo):
            
        if not self.nochao:
            self.vel.y += self.__gravidade
            self.collide(0, grupo)

        self.rect.top += self.vel.y
        self.__nochao = False
        self.collide(self.vel.y, grupo)
      
      
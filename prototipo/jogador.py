import pygame
from pygame.locals import *


class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = 468
        self.velocidade_pulo = 8
        self.pulando = False
        self.image = pygame.image.load('quadrado preto.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def pular(self):
        self.pulando = True

    def update(self):       
        
        '''Mecanica de movimento do pulo'''
        if self.pulando:
            if self.rect.y <= 410:
                self.pulando = False
            self.rect.y -= self.velocidade_pulo
        
        else:
            if self.rect.y < self.y:
                self.rect.y += self.velocidade_pulo
            else:
                self.rect.y = self.y
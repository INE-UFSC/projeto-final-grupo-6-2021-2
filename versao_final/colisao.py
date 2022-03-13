import pygame
from obstaculos import Block, Spike, Win, Orb, Portal, PortalSaida
from skin import Skin

class Colisao():

    def __init__(self, jogador, tela, elementos) -> None:
        self.__jogador = jogador
        self.__tela = tela
        self.__elementos = elementos

    @property
    def jogador(self):
        return self.__jogador

    @property
    def tela(self):
        return self.__tela

    @property
    def elementos(self):
        return self.__elementos

    def collide(self, yvel, keys):
        grupo = self.__elementos
        # Verificação das colisões
        for x in grupo:
            if pygame.sprite.spritecollide(self.__jogador, [x], False, pygame.sprite.collide_mask):
                if isinstance(x, Block):
                    if yvel > 0:
                        self.jogador.rect.bottom = x.rect.top
                        self.jogador.velocidade.y = 0
                        self.jogador.pulando = False
                        self.jogador.nochao = True
                        if self.jogador.voo:
                            self.jogador.morte = True
                            self.jogador.velocidade.x = 0
                    elif yvel < 0:
                        self.jogador.rect.top = x.rect.bottom
                        self.jogador.morte = True
                        self.jogador.velocidade.x = 0
                    else:
                        self.jogador.rect.right = x.rect.left
                        self.jogador.morte = True
                        self.jogador.velocidade.x = 0  # Caso o personagem morra, ele fica parado

                if isinstance(x, Spike):
                    self.jogador.morte = True
                    self.jogador.velocidade.x = 0

                if isinstance(x, Win):
                    self.jogador.vitoria = True
                    self.jogador.velocidade.x = 0

                if (isinstance(x, Orb) and keys[pygame.K_SPACE] and yvel > 0):
                    self.jogador.forca_pulo = 10
                    self.jogador.pular()
                    self.jogador.forca_pulo = 8.5
                
                if isinstance(x, Portal):
                        self.jogador.transforma_nave()
                        self.jogador.velocidade.y = 0
                        self.jogador.forca_pulo = 3
                        self.jogador.voo = True
                        self.jogador.gravidade = 0.2

                if isinstance(x, PortalSaida):
                        self.jogador.transforma_jogador()
                        self.jogador.velocidade.y = 0
                        self.jogador.voo = False
                        self.jogador.gravidade = 0.7
                        self.jogador.forca_pulo = 8.5
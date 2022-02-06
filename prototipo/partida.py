import os
from obstaculos import *


class Partida():

    def __init__(self, fase, jogador) -> None:
        self.fase = fase
        self.elementos = []
        self.jogador = jogador
        self.tela = pygame.display.set_mode((800, 480))

    def desenhar_nivel(self, mapa):
        x = 0
        y = 0
        for row in mapa:
            for col in row:

                if col == 2:
                    objeto = Block((x, y))
                    self.elementos.append(objeto)
                if col == 1:
                    objeto = Spike((x, y))
                    self.elementos.append(objeto)
                x += 24
            y += 24
            x = 0

    def atualizar_nivel(self, velocidade):
        for sprite in self.elementos:
            sprite.rect.x -= velocidade

    def desenhar_elementos(self):
        for x in self.elementos:
            self.tela.blit(x.image, (x.rect.x, x.rect.y))

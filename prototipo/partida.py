import os
from obstaculos import *

current_directory = os.path.dirname(__file__)
file_path_mapa = os.path.join(current_directory, 'Mapas')


class Partida():

    def __init__(self, fase, jogador) -> None:
        self.fase = fase
        self.elements = []
        self.jogador = jogador
        self.screen = pygame.display.set_mode((800, 480))

    def desenhar_level(self, mapa):
        x = 0
        y = 0
        for row in mapa:
            for col in row:
                
                if col == 1:
                    objeto = Block((x, y))
                    self.elements.append(objeto)
                if col == 2:
                    objeto = Spike((x, y))
                    self.elements.append(objeto)
                x += 24
            y += 24
            x = 0

    def atualizar_level(self, velocidade):
        for sprite in self.elements:
            sprite.rect.x -= velocidade

    def desenhar_elementos(self):
        for x in self.elements:
            self.screen.blit(x.image, (x.rect.x, x.rect.y))

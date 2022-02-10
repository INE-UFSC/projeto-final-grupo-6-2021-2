import os
from obstaculos import *


class Partida():

    def __init__(self, fase, jogador) -> None:
        self.fase = fase
        self.elementos = []
        self.jogador = jogador
        self.tela = pygame.display.set_mode((800, 480))
        self.bg_x = 0
    
    def draw_bg(self):
        #desenha o fundo da fase com x variavel para dar movimento
        self.tela.blit(self.fase.bg ,(self.bg_x, 0))
        self.tela.blit(self.fase.bg ,(self.bg_x+990, 0))  

    def desenhar_nivel(self, mapa):
        #Lê a matriz do mapa e instancia os objetos 
        x = 0
        y = 0
        for row in mapa:
            for col in row:

                if col == 2:
                    objeto = Block((x, y))
                    self.elementos.append(objeto)
                elif col == 1:
                    objeto = Spike((x, y))
                    self.elementos.append(objeto)
                elif col == 3:
                    objeto = Win((x, y))
                    self.elementos.append(objeto)
                x += 24
            y += 24
            x = 0

    def atualizar_nivel(self, velocidade):
        #Movimenta o mapa inteiro para dar impressão de movimento
        for sprite in self.elementos:
            sprite.rect.x -= velocidade
        #self.bg_x -= velocidade
        #if self.bg_x <= -990:
        #    self.bg_x = 0

    def desenhar_elementos(self):
        for x in self.elementos:
            self.tela.blit(x.image, (x.rect.x, x.rect.y))

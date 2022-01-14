import pygame
from pygame.locals import *
from sys import exit
from jogador import Jogador
import os

pygame.init()

FPS = 60
clock = pygame.time.Clock()

PRETO = (34, 40, 49)
BRANCO = (240, 240, 240)

LARGURA = 800
ALTURA = 600
y_chao = 500

# Criação da janela de jogo
display = pygame.display.set_mode((LARGURA, ALTURA))
display.fill(BRANCO)
pygame.display.set_caption("Geometry Dash")

# Grupo que armazena os objetos e sprites 
sprites = pygame.sprite.Group()
jogador = Jogador()
sprites.add(jogador)

while True:
    
    # Preenche o fundo e desenha a linha a cada ciclo
    display.fill(BRANCO)
    pygame.draw.line(display, PRETO, (0, y_chao), (800, y_chao))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Detecção da tecla para o pulo
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_SPACE]:
        if jogador.rect.y != jogador.y:
            pass
        else:
            jogador.pular()

    # Desenho e update do grupo de sprites
    sprites.draw(display)
    sprites.update()
    
    pygame.display.update()
    
    clock.tick(FPS)
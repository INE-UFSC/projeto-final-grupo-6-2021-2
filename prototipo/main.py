import pygame
from pygame.locals import *
from sys import exit

pygame.init()

FPS = 60
clock = pygame.time.Clock()

PRETO = (34, 40, 49)
BRANCO = (240, 240, 240)

display = pygame.display.set_mode((800, 600))
display.fill(BRANCO)
pygame.display.set_caption("Geometry Dash")

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.draw.rect(display, PRETO, (50, 450, 50, 50))

pygame.draw.line(display, PRETO, (0, 500), (800, 500))

J1 = Jogador()

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    clock.tick(FPS)
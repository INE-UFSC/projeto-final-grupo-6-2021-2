import pygame
import csv
from pygame.locals import *
from sys import exit


#Cada objeto recebe uma imagem, a posição dele e de que grupo ele faz parte.
#É necessário criar o grupo préviamente usando pygame.sprite.Group(), exemplo na linha 47
#Cada objeto é adicionado a esse grupo automaticamente pelo pygame ao ser intanciado
#No loop principal usa-se nome_do_grupo.draw(tela_em_que_vai_ser_desenhado), exemplo linha 114

class Obstaculo(pygame.sprite.Sprite):

    def __init__(self, image, pos, *groups) -> None:
        super().__init__(*groups)
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)


class Spike(Obstaculo):

    def __init__(self, image, pos, *groups) -> None:
        super().__init__(image, pos, *groups)


class Block(Obstaculo):

    def __init__(self, image, pos, *groups) -> None:
        super().__init__(image, pos, *groups)


class Orb(Obstaculo):

    def __init__(self, image, pos) -> None:
        super().__init__(image, pos)


class Coin(Obstaculo):

    def __init__(self, image, pos) -> None:
        super().__init__(image, pos)



# A partir daqui é apenas codigo para teste, apagar futuramente

'''
pygame.init()

elements = pygame.sprite.Group()
FPS = 60
clock = pygame.time.Clock()

PRETO = (34, 40, 49)
BRANCO = (240, 240, 240)

screen = pygame.display.set_mode((800, 400))
bg_surface = pygame.image.load('C:/1Principal/Projects/Python/ProjetoFinalPOO2/Img/bg.png')
block = pygame.image.load('C:/1Principal/Projects/Python/ProjetoFinalPOO2/Img/FakeSpike01.png')
block = pygame.transform.smoothscale(block, (32, 32))
pygame.display.set_caption("Geometry Dash")

def init_level(map):
    """this is similar to 2d lists. it goes through a list of lists, and creates instances of certain obstacles
    depending on the item in the list"""
    x = 0
    y = 0

    for row in map:
        for col in row:

            if col == "0":
                Block(block, (x, 300), elements)
            x += 32
        y += 16
        x = 0

def block_map(level_num):
    """
    :type level_num: rect(screen, BLACK, (0, 0, 32, 32))
    open a csv file that contains the right level map
    """
    lvl = []
    with open(level_num, newline='') as csvfile:
        trash = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in trash:
            lvl.append(row)
    return lvl

def resize(img, size=(32, 32)):
    """resize images
    :param img: image to resize
    :type img: im not sure, probably an object
    :param size: default is 32 because that is the tile size
    :type size: tuple
    :return: resized img
    :rtype:object?
    """
    resized = pygame.transform.smoothscale(img, size)
    return resized

level_list = block_map('C:/1Principal/Projects/Python/ProjetoFinalPOO2/Mapas/mapa_teste.csv')
init_level(level_list)

print(elements)

while True: 
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    screen.blit(bg_surface,(0,0))
    elements.draw(screen)
    clock.tick(FPS)
'''
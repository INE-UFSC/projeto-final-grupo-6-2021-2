import json, os
import pygame
from pygame.locals import *
from obstaculos import Spike, Block

current_directory = os.path.dirname(__file__)
file_path_image = os.path.join(current_directory, 'imagens')
file_path_mapa = os.path.join(current_directory, 'Mapas')

pygame.init()

elements = pygame.sprite.Group()
FPS = 60
clock = pygame.time.Clock()

PRETO = (34, 40, 49)
BRANCO = (240, 240, 240)

screen = pygame.display.set_mode((1280, 960))
bg_surface = pygame.image.load(f'{file_path_image}/bg.png')
bg_surface = pygame.transform.smoothscale(bg_surface, (1280, 960))
spike = pygame.image.load(f'{file_path_image}/FakeSpike01.png')
spike = pygame.transform.smoothscale(spike, (48, 48))
block = pygame.image.load(f'{file_path_image}/block1.png')
block = pygame.transform.smoothscale(block, (48, 48))
pygame.display.set_caption("Geometry Dash")

def init_level(map):
    """this is similar to 2d lists. it goes through a list of lists, and creates instances of certain obstacles
    depending on the item in the list"""
    x = 0
    y = 0

    for row in map:
        for col in row:
            
            if col == 1:
                Block(block, (x, y), elements)
            if col == 2:
                Spike(spike, (x, y), elements)
            x += 48
        y += 48
        x = 0

def block_map(file):
    """
    :type level_num: rect(screen, BLACK, (0, 0, 32, 32))
    open a csv file that contains the right level map
    """
    with open(file) as f:
        data = json.load(f)
        linha = []
        mapa = []
        count = 0
        for x in data["layers"][1]['data']:
            linha.append(x)
            count += 1
            if count == 80:
                count = 0
                mapa.append(linha[:])
                linha.clear()
        f.close()
    return mapa
     

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

level_list = block_map(f'{file_path_mapa}/mapa_teste2.json')
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

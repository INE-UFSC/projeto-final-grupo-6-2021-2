import pygame
import csv
from pygame.locals import *
from sys import exit

class Obstaculo(pygame.sprite.Sprite):

    def __init__(self, image, pos) -> None:
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)


class Spike(Obstaculo):

    def __init__(self, image, pos) -> None:
        super().__init__(image, pos)


class Block(Obstaculo):

    def __init__(self, image, pos) -> None:
        super().__init__(image, pos)


class Orb(Obstaculo):

    def __init__(self, image, pos) -> None:
        super().__init__(image, pos)


class Coin(Obstaculo):

    def __init__(self, image, pos) -> None:
        super().__init__(image, pos)




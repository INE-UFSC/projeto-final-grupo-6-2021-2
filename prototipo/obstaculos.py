import pygame
from pygame.locals import *


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

    def __init__(self, image, pos, *groups) -> None:
        super().__init__(image, pos, groups)


class Coin(Obstaculo):

    def __init__(self, image, pos, *groups) -> None:
        super().__init__(image, pos, groups)

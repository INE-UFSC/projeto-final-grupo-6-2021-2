from abc import ABC
import pygame
from pygame.locals import *
from filePaths import file_paths




class Obstaculo(ABC):

    def __init__(self, image, pos) -> None:
        image = pygame.transform.smoothscale(image, (24, 24))
        self.__image = image
        self.__rect = self.image.get_rect(topleft=pos)
        self.__mask = pygame.mask.from_surface(self.image)

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, value):
        self.__rect = value

    @property
    def mask(self):
        return self.__mask

    @mask.setter
    def mask(self, value):
        self.__mask = value


class Spike(Obstaculo):

    def __init__(self, pos) -> None:
        image = pygame.image.load(f'{file_paths.imagens}/FakeSpike01.png')
        super().__init__(image, pos)


class Block(Obstaculo):

    def __init__(self, pos) -> None:
        image = pygame.image.load(f'{file_paths.imagens}/block1.png')
        super().__init__(image, pos)


class Win(Obstaculo):

    def __init__(self, pos) -> None:
        image = pygame.image.load(f'{file_paths.imagens}/win.png')
        image = pygame.transform.smoothscale(
            image.convert(), (16, 16))
        super().__init__(image, pos)


class Orb(Obstaculo):

    def __init__(self, pos) -> None:
        image = pygame.image.load(f'{file_paths.imagens}/orb-yellow.png')
        image = pygame.transform.smoothscale(
            image.convert(), (16, 16))
        super().__init__(image, pos)


class Coin(Obstaculo):

    def __init__(self, image, pos) -> None:
        super().__init__(image, pos)

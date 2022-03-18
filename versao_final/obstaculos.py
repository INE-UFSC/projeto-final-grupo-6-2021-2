from abc import ABC
import pygame
from pygame.locals import *
from LoadedImages import loaded_images


class Obstaculo(ABC):

    def __init__(self, image, pos) -> None:
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
        image = loaded_images.imagens_obtaculos['Spike']
        image = pygame.transform.smoothscale(image, (24, 24))
        super().__init__(image, pos)


class Block(Obstaculo):

    def __init__(self, pos) -> None:
        image = loaded_images.imagens_obtaculos['Block']
        image = pygame.transform.smoothscale(image, (24, 24))
        super().__init__(image, pos)


class Win(Obstaculo):

    def __init__(self, pos) -> None:
        image = loaded_images.imagens_obtaculos['Win']
        image = pygame.transform.smoothscale(image, (24, 24))
        super().__init__(image, pos)


class Portal(Obstaculo):

    def __init__(self, pos) -> None:
        image = loaded_images.imagens_obtaculos['Portal']
        super().__init__(image, pos)


class PortalSaida(Obstaculo):

    def __init__(self, pos) -> None:
        image = loaded_images.imagens_obtaculos['PortalSaida']
        super().__init__(image, pos)


class Orb(Obstaculo):

    def __init__(self, pos) -> None:
        image = loaded_images.imagens_obtaculos['Orb']
        image = pygame.transform.smoothscale(image, (24, 24))
        super().__init__(image, pos)

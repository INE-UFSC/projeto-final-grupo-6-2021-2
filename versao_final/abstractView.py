from abc import ABC, abstractmethod
from LoadedImages import loaded_images
import pygame

class AbstractView(ABC):
    
    def __init__(self, tela, fundo_tela) -> None:
        self.COR_BASE_TEXTO = (255, 255, 255)
        self.COR_MOUSE = (15, 14, 23)    # (255, 137, 6) -> Amarelo
        self.__tela = tela
        self.__fundo_tela = loaded_images.imagens_telas[fundo_tela]
        self.__fundo_botao = loaded_images.imagens_botoes['Ret_select_rosa']
        self.__fonte_botao = pygame.font.SysFont('calibri', 20)

    @abstractmethod
    def desenha(self):
        pass
    
    @property
    def tela(self):
        return self.__tela

    @tela.setter
    def tela(self, valor):
        self.__tela = valor

    @property
    def fundo_tela(self):
        return self.__fundo_tela

    @fundo_tela.setter
    def fundo_tela(self, status):
        self.__fundo_tela = status

    @property
    def fundo_botao(self):
        return self.__fundo_botao

    @fundo_botao.setter
    def fundo_botao(self, status):
        self.__fundo_botao = status

    @property
    def fonte_botao(self):
        return self.__fonte_botao

    @fonte_botao.setter
    def fonte_botao(self, status):
        self.__fonte_botao = status

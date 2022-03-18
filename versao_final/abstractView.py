from abc import ABC, abstractmethod
from LoadedImages import loaded_images
import pygame


class AbstractView(ABC):

    def __init__(self, tela, fundo_tela) -> None:
        self.COR_BASE_TEXTO = (255, 255, 255)
        self.COR_BASE_TITULO = (0, 0, 0)
        self.COR_BASE_BACKGROUND = (250, 250, 250, 160)
        self.COR_MOUSE = (15, 14, 23)    # (255, 137, 6) -> Amarelo
        self.__tela = tela
        self.__fundo_tela = loaded_images.imagens_telas[fundo_tela] if fundo_tela else None
        self.__fundo_botao = loaded_images.imagens_botoes['Ret_select_rosa']
        self.__fundo_botao_grande = loaded_images.imagens_botoes['Ret_select_rosa_120']
        self.__fonte_botao = pygame.font.SysFont('calibri', 20)
        self.__fonte_titulo = pygame.font.SysFont('calibri', 24)
        self.__fonte_subtitulo = pygame.font.SysFont('calibri', 18)

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
    def fundo_tela(self, fundo):
        self.__fundo_tela = fundo

    @property
    def fundo_botao(self):
        return self.__fundo_botao

    @fundo_botao.setter
    def fundo_botao(self, fundo):
        self.__fundo_botao = fundo

    @property
    def fundo_botao_grande(self):
        return self.__fundo_botao_grande

    @fundo_botao_grande.setter
    def fundo_botao_grande(self, fundo):
        self.__fundo_botao_grande = fundo

    @property
    def fonte_botao(self):
        return self.__fonte_botao

    @fonte_botao.setter
    def fonte_botao(self, fonte):
        self.__fonte_botao = fonte

    @property
    def fonte_titulo(self):
        return self.__fonte_titulo

    @fonte_titulo.setter
    def fonte_titulo(self, fonte):
        self.__fonte_titulo = fonte

    @property
    def fonte_subtitulo(self):
        return self.__fonte_subtitulo

    @fonte_titulo.setter
    def fonte_subtitulo(self, fonte):
        self.__fonte_subtitulo = fonte

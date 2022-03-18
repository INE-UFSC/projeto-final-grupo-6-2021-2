import pygame
from pygame.locals import *
from botao_menu import Botao
from LoadedImages import loaded_images
from abstractView import AbstractView


class MenuSkin(AbstractView):

    def __init__(self, tela, lista_skins):
        super().__init__(tela, 'Menu_skin')

        self.__skin_selec = lista_skins[0].arquivo

        x_botao, y_botao = 250, 225

        self.lista_botoes = []

        # Aviso: view nao automatizada para terceira linha.
        for skin in lista_skins:
            if skin.nome == 'Cubo Mágico':
                fundo_botao_grande = loaded_images.imagens_botoes['Ret_select_rosa_120']
                self.lista_botoes.append(
                    (Botao(imagem=fundo_botao_grande, x_pos=x_botao, y_pos=y_botao,
                           mensagem=skin.nome, fonte=self.fonte_botao,
                           cor_base_texto=self.COR_BASE_TEXTO, cor_mouse=self.COR_MOUSE), lista_skins.index(skin)))
            else:
                self.lista_botoes.append(
                    (Botao(imagem=self.fundo_botao, x_pos=x_botao, y_pos=y_botao,
                           mensagem=skin.nome, fonte=self.fonte_botao,
                           cor_base_texto=self.COR_BASE_TEXTO, cor_mouse=self.COR_MOUSE), lista_skins.index(skin)))

            x_botao += 150
            if x_botao > 550:
                x_botao = 250  # volta pro x inicial
                y_botao = 350

        self.lista_botoes.append(
            (Botao(imagem=self.fundo_botao, x_pos=55, y_pos=25,
                   mensagem='Voltar', fonte=self.fonte_botao,
                   cor_base_texto=self.COR_BASE_TEXTO, cor_mouse=self.COR_MOUSE), 'Voltar'))

    def __converte(self, arquivo, size_x, size_y):
        return pygame.transform.smoothscale(
            arquivo.convert(), (size_x, size_y))

    def seleciona_skin(self, skin):
        '''Recebe imagem da skin loaded e muda atributo self.skin'''
        self.__skin_selec = skin
        return skin

    def desenha(self):
        self.tela.blit(self.fundo_tela, (0, 0))
        self.tela.blit(self.__converte(self.__skin_selec, 30, 30), (700, 75))

        x_skin, y_skin = 235, 150
        for skin in loaded_images.imagens_skins.values():
            self.tela.blit(self.__converte(skin, 30, 30), (x_skin, y_skin))
            x_skin += 150

            if x_skin > 535:
                x_skin = 235
                y_skin = 275

        for botao in self.lista_botoes:
            botao[0].update(self.tela)
            botao[0].muda_cor()

        pygame.display.update()

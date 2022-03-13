import pygame
from pygame.locals import *
from botao_menu import Botao
from skin import Skin
from filePaths import file_paths
from LoadedImages import loaded_images
from containerSkins import ContainerSkins


class MenuSkin():

    def __init__(self, tela, lista_skins):
        self.__tela = tela

        fonte_botao = pygame.font.SysFont('calibri', 20)
        self.fundo_menu = loaded_images.imagens_telas['Menu_skin']
        self.fundo_botao = loaded_images.imagens_botoes['Ret_select_rosa']

        self.__skin_selec = lista_skins[0].arquivo

        x_botao, y_botao = 250, 225

        self.lista_botoes = []

        # aviso: view nao automatizada para terceira linha.
        for skin in lista_skins:
            self.lista_botoes.append(
                (Botao(imagem=self.fundo_botao, x_pos=x_botao, y_pos=y_botao,
                       mensagem=skin.nome, fonte=fonte_botao,
                       cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)), lista_skins.index(skin)))

            x_botao += 150
            if x_botao > 550:
                x_botao = 250  # volta pro x inicial
                y_botao = 350

        self.lista_botoes.append(
            (Botao(imagem=self.fundo_botao, x_pos=55, y_pos=25,
                   mensagem='Voltar', fonte=fonte_botao,
                   cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)), 'Voltar'))

    def __converte(self, arquivo, size_x, size_y):
        # imagem = pygame.image.load( f"{file_paths.imagens}/{arquivo}")
        return pygame.transform.smoothscale(
            arquivo.convert(), (size_x, size_y))

    def seleciona_skin(self, skin):
        '''recebe imagem loaded'''
        self.__skin_selec = skin
        return skin

    def desenha(self):
        self.__tela.blit(self.fundo_menu, (0, 0))
        self.__tela.blit(self.__converte(self.__skin_selec, 30, 30), (700, 75))

        x_skin, y_skin = 235, 150
        for skin in loaded_images.imagens_skins.values():
            self.__tela.blit(self.__converte(skin, 30, 30), (x_skin, y_skin))
            x_skin += 150

            if x_skin > 535:
                x_skin = 235
                y_skin = 275

        for botao in self.lista_botoes:
            botao[0].update(self.__tela)
            botao[0].muda_cor()

        pygame.display.update()

import pygame
from pygame.locals import *
from botao_menu import Botao
from skin import Skin
from filePaths import file_paths


class MenuSkin():

    def __init__(self, tela):
        self.__tela = tela

        fonte_botao = pygame.font.SysFont('calibri', 20)
        self.fundo_menu = self.__adiciona_e_transforma_imagem(
            'fundo_menuskins.png', 800, 480)
        self.fundo_botao = self.__adiciona_e_transforma_imagem(
            'ret_menu.png', 100, 30)

        self.__skin_selec = Skin('Padrão', 'geo.png')
        self.skins = [
            Skin('Padrão', 'geo.png'),
            Skin('Azul', 'geo blue.jpg'),
            Skin('Beta', 'quadrado preto.png'),
            Skin('Beta', 'quadrado preto.png')
        ]

        x_botao = 250
        y_botao = 225

        self.lista_botoes = []

        # aviso: view nao automatizada para terceira linha.
        for skin in self.skins:
            self.lista_botoes.append(
                (Botao(imagem=self.fundo_botao, x_pos=x_botao, y_pos=y_botao,
                       mensagem=skin.nome, fonte=fonte_botao,
                       cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)), skin))

            x_botao += 150
            if x_botao > 550:
                x_botao = 250  # volta pro x inicial
                y_botao = 350

        self.lista_botoes.append(
            (Botao(imagem=self.fundo_botao, x_pos=50, y_pos=25,
                   mensagem='Voltar', fonte=fonte_botao,
                   cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)), 'Voltar'))

    def __adiciona_e_transforma_imagem(self, file_name, size_x, size_y):
        image = pygame.image.load(
            f'{file_paths.imagens}/menu_view/{file_name}')
        return pygame.transform.smoothscale(
            image.convert(), (size_x, size_y))

    def __adiciona_e_transforma_skin(self, arquivo, size_x, size_y):
        imagem = pygame.image.load(
            f"{file_paths.imagens}/{arquivo}")
        return pygame.transform.smoothscale(
            imagem.convert(), (size_x, size_y))

    def selecina_skin(self, skin):
        self.__skin_selec = skin
        return skin

    def desenha(self):
        self.__tela.blit(self.fundo_menu, (0, 0))
        self.__tela.blit(self.__adiciona_e_transforma_skin(
            self.__skin_selec.arquivo, 30, 30), (700, 75))

        x_skin = 235
        y_skin = 150
        for skin in self.skins:
            self.__tela.blit(self.__adiciona_e_transforma_skin(
                skin.arquivo, 30, 30), (x_skin, y_skin))
            x_skin += 150

            if x_skin > 535:
                x_skin = 235
                y_skin = 275

        for botao in self.lista_botoes:
            botao[0].update(self.__tela)
            botao[0].muda_cor()

        pygame.display.update()

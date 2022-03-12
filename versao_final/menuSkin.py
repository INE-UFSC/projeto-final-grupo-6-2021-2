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
            Skin('Beta', 'quadrado preto.png')
        ]
        self.lista_botoes = [
            Botao(imagem=self.fundo_botao, x_pos=250, y_pos=225,
                  mensagem='Padrão', fonte=fonte_botao,
                  cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)),
            Botao(imagem=self.fundo_botao, x_pos=400, y_pos=225,
                  mensagem='Azul', fonte=fonte_botao,
                  cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)),
            Botao(imagem=self.fundo_botao, x_pos=550, y_pos=225,
                  mensagem='Beta', fonte=fonte_botao,
                  cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)),
            Botao(imagem=self.fundo_botao, x_pos=250, y_pos=350,
                  mensagem='Skin4', fonte=fonte_botao,
                  cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)),
            Botao(imagem=self.fundo_botao, x_pos=400, y_pos=350,
                  mensagem='Skin5', fonte=fonte_botao,
                  cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)),
            Botao(imagem=self.fundo_botao, x_pos=550, y_pos=350,
                  mensagem='Skin6', fonte=fonte_botao,
                  cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)),
            Botao(imagem=self.fundo_botao, x_pos=50, y_pos=25,
                  mensagem='Voltar', fonte=fonte_botao,
                  cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6))
        ]
    
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

    def selecina_skin(self, nome):
        for skin in self.skins:
            if skin.nome == nome:
                self.__skin_selec = skin
                return skin
    
    def desenha(self):
        self.__tela.blit(self.fundo_menu, (0, 0))
        self.__tela.blit(self.__adiciona_e_transforma_skin(self.__skin_selec.arquivo, 30, 30), (700, 75))
        self.__tela.blit(self.__adiciona_e_transforma_skin(self.skins[0].arquivo, 30, 30), (235, 150))
        self.__tela.blit(self.__adiciona_e_transforma_skin(self.skins[1].arquivo, 30, 30), (385, 150))
        self.__tela.blit(self.__adiciona_e_transforma_skin(self.skins[2].arquivo, 30, 30), (535, 150))

        for botao in self.lista_botoes:
            botao.update(self.__tela)
            botao.muda_cor(pygame.mouse.get_pos())

        pygame.display.update()

    def lista_nomes_skins(self):
        lista = []
        for skin in self.skins:
            lista.append(skin.nome)
        return lista

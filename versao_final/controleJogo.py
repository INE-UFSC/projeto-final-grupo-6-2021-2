import pygame
from pygame.locals import *
from pygame import mixer
from random import choice
from filePaths import file_paths
from jogador import Jogador
from fase import Fase
from partida import Partida
from menuView import menuView
from skin import Skin
from updater import Updater
from escolhaFasesView import EscolhaFasesView


class ControleJogo():

    def __init__(self):

        pygame.init()

        self.tela = pygame.display.set_mode((800, 480))
        self.__jogador = Jogador()
        self.__skins = [Skin('Quadrado Preto', 'quadrado preto.png'),
                        Skin('Azul', 'geo blue.jpg')]
        self.__fase = None
        self.__menu_view = menuView(self.tela)
        self.escolha_fase_view = EscolhaFasesView(self.tela)
        self.__partida = Partida(self.__fase, self.__jogador, self.tela)
        self.__updater = Updater(self.__jogador, self.__partida)
        self.FPS = 60

    @property
    def jogador(self):
        return self.__jogador

    @property
    def colisao(self):
        return self.__colisao

    @property
    def fase(self):
        return self.__fase

    @property
    def partida(self):
        return self.__partida

    def inicio_jogo(self):
        clock = pygame.time.Clock()
        while True:
            mouse_pos = pygame.mouse.get_pos()
            detecta_mouse = self.__menu_view.desenha(mouse_pos)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()
                # detectao de cliques
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for botao in self.__menu_view.lista_botoes:
                        if botao.detecta_mouse(mouse_pos):
                            detecta_mouse = botao.detecta_mouse(
                                mouse_pos), botao
                            break
                    if detecta_mouse is not None:
                        if detecta_mouse[0]:
                            if detecta_mouse[1].mensagem == 'Jogar':
                                return self.escolha_fase()
                            elif detecta_mouse[1].mensagem == 'Skins':
                                if self.__jogador.skin_atual.nome == 'Padrão':
                                    self.__jogador.muda_skin(
                                        choice(self.__skins))
                                else:
                                    self.__jogador.muda_skin(
                                        Skin('Padrão', 'geo.png'))
                                print('Feedback: Mudou de skin!')

                            elif detecta_mouse[1].mensagem == 'Sair':
                                pygame.display.quit()
                                pygame.quit()
                                exit()

            clock.tick(self.FPS)

    def escolha_fase(self):
        clock = pygame.time.Clock()
        while True:
            mouse_pos = pygame.mouse.get_pos()
            detecta = self.escolha_fase_view.desenha(mouse_pos)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()
                # detectao de cliques
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for botao_tup in self.escolha_fase_view.lista_botoes:
                        if botao_tup[0].detecta_mouse(mouse_pos):
                            detecta = botao_tup[0].detecta_mouse(
                                mouse_pos), botao_tup[1]
                            break
                    if detecta is not None:
                        if detecta[0] and detecta[1] == 'Voltar':
                            return self.inicio_jogo()
                        elif detecta[0]:
                            self.__fase = detecta[1]
                            self.__partida.fase = self.__fase
                            return self.iniciar_partida()

            clock.tick(self.FPS)

    def iniciar_partida(self):
        clock = pygame.time.Clock()
        # bg_surface = pygame.image.load(f'{file_path_image}/bg.png')
        self.partida.inicia()

        jogador_group = pygame.sprite.Group()
        jogador_group.add(self.jogador)

        while True:

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.jogador.resetar()
                        self.partida.para_musica()
                        return self.inicio_jogo()

            keys_pressed = pygame.key.get_pressed()

            if self.jogador.morte or self.jogador.vitoria:
                self.partida.desenha_fim_de_jogo()

            else:

                if keys_pressed[pygame.K_SPACE]:
                    if self.jogador.nochao:
                        self.jogador.pular()

                # self.partida.tela.blit(bg_surface, (0, 0))
                self.partida.draw_bg()
                self.partida.desenhar_elementos()
                self.__updater.update_partida(self.jogador.velocidade.x)
                jogador_group.draw(self.partida.tela)
                self.__updater.update_jogador(
                    self.partida.elementos, keys_pressed)

            if keys_pressed[pygame.K_r]:
                self.jogador.resetar()
                self.partida.para_musica()
                self.iniciar_partida()

            clock.tick(self.FPS)

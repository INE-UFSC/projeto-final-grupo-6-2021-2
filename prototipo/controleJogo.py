import pygame
from pygame.locals import *
from pygame import mixer
import os
from jogador import Jogador
from fase import Fase
from partida import Partida


current_directory = os.path.dirname(__file__)
file_path_musica = os.path.join(current_directory, 'musicas')
file_path_fonts = os.path.join(current_directory, 'fonts')
file_path_image = os.path.join(current_directory, 'imagens/tinified')
file_path_mapa = os.path.join(current_directory, 'mapas')


class ControleJogo():
    def __init__(self):
        self.__jogador = Jogador()
        self.__fase = Fase(
            'Fase 1',
            f'{file_path_musica}/undertale-megalovania.mp3',
            f'{file_path_mapa}/mapa_teste4.json')
        self.__partida = Partida(self.__fase, self.__jogador)
        self.__end_game = pygame.display.set_mode((800, 480))

    @property
    def jogador(self):
        return self.__jogador

    @property
    def fase(self):
        return self.__fase

    @property
    def partida(self):
        return self.__partida

    def tela_de_morte(self):
        pygame.mixer.music.stop()
        texto_morte = 'MoRrEuU'
        texto_opcoes = 'Aperte R para reiniciar e ESC para sair'
        fontesys60 = pygame.font.SysFont(pygame.font.get_default_font(), 60)
        fontesys40 = pygame.font.SysFont(pygame.font.get_default_font(), 24)
        tela_texto_morte = fontesys60.render(texto_morte, 1, (255, 255, 255))
        tela_texto_opcoes = fontesys40.render(texto_opcoes, 1, (255, 255, 255))
        self.__end_game.blit(tela_texto_morte, (300, 200))
        self.__end_game.blit(tela_texto_opcoes, (250, 260))
        pygame.display.update()

    def iniciar_partida(self):
        pygame.init()

        FPS = 60
        clock = pygame.time.Clock()

        self.__partida.elements.clear()
        bg_surface = pygame.image.load(f'{file_path_image}/bg.png')
        bg_surface = pygame.transform.smoothscale(
            bg_surface.convert(), (800, 480))
        mapa = self.__partida.fase.mapear_fase()
        self.__partida.desenhar_level(mapa)
        self.__partida.fase.toca_musica()  # toca a musica especifica da fase
        jogador_group = pygame.sprite.Group()
        jogador_group.add(self.__jogador)

        while True:

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()

            keys_pressed = pygame.key.get_pressed()

            if self.jogador.morte:
                self.tela_de_morte()

            else:
                if keys_pressed[pygame.K_SPACE]:
                    self.__jogador.pular()

                self.__partida.screen.blit(bg_surface, (0, 0))
                self.__partida.desenhar_elementos()
                self.__partida.atualizar_level(self.jogador.velocidade.x)
                jogador_group.draw(self.__partida.screen)
                jogador_group.update(self.__partida.elements)

            if keys_pressed[pygame.K_ESCAPE]:
                pygame.display.quit()
                pygame.quit()
                exit()

            if keys_pressed[pygame.K_r]:
                self.jogador.resetar()
                self.iniciar_partida()

            clock.tick(FPS)

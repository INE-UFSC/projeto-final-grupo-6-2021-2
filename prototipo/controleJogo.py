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
        texto_morte = 'Você morreu!'
        texto_opcoes = 'Aperte R para reiniciar e ESC para sair'
        fontesys60 = pygame.font.SysFont('calibri', 60)
        fontesys40 = pygame.font.SysFont('calibri', 24)
        tela_texto_morte = fontesys60.render(texto_morte, 1, (255, 255, 255))
        tela_texto_opcoes = fontesys40.render(texto_opcoes, 1, (255, 255, 255))
        self.__end_game.blit(tela_texto_morte, (240, 200))
        self.__end_game.blit(tela_texto_opcoes, (220, 280))
        pygame.display.update()

    def iniciar_partida(self):
        pygame.init()

        FPS = 60
        clock = pygame.time.Clock()

        self.partida.elementos.clear()
        bg_surface = pygame.image.load(f'{file_path_image}/bg.png')
        bg_surface = pygame.transform.smoothscale(
            bg_surface.convert(), (800, 480))
        mapa = self.partida.fase.mapear_fase()
        self.partida.desenhar_nivel(mapa)
        self.partida.fase.toca_musica()
        jogador_group = pygame.sprite.Group()
        jogador_group.add(self.jogador)

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
                    self.jogador.pular()

                self.partida.tela.blit(bg_surface, (0, 0))
                self.partida.desenhar_elementos()
                self.partida.atualizar_nivel(self.jogador.velocidade.x)
                jogador_group.draw(self.partida.tela)
                jogador_group.update(self.partida.elementos)

            if keys_pressed[pygame.K_ESCAPE]:
                pygame.display.quit()
                pygame.quit()
                exit()

            if keys_pressed[pygame.K_r]:
                self.jogador.resetar()
                self.iniciar_partida()

            clock.tick(FPS)

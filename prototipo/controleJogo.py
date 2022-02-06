import pygame
from pygame.locals import *
from pygame import mixer
import os
from jogador import Jogador
from fase import Fase
from partida import Partida


current_directory = os.path.dirname(__file__)
file_path_image = os.path.join(current_directory, 'imagens')
file_path_mapa = os.path.join(current_directory, 'Mapas')
file_path_musica = os.path.join(current_directory, 'musicas')
file_path_fonts = os.path.join(current_directory, 'fonts')


class ControleJogo():
    def __init__(self):
        self.__jogador = Jogador()
        self.__fase = Fase(
            'Fase 1', f'{file_path_musica}/undertale-megalovania.mp3', f'{file_path_mapa}/mapa_teste4.json')
        self.__partida = Partida(self.__fase, self.__jogador)

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
        self.__partida.elements.clear()
        # opcoes: tirar o jogador da tela também? mensagem explicando para apertar R?

    def iniciar_partida(self):
        pygame.init()

        FPS = 60
        clock = pygame.time.Clock()

        self.__partida.elements.clear()
        bg_surface = pygame.image.load(f'{file_path_image}/bg.png')
        bg_surface = pygame.transform.smoothscale(bg_surface, (800, 480))
        mapa = self.__partida.fase.mapear_fase()
        self.__partida.desenhar_level(mapa)
        self.__partida.fase.toca_musica()  # toca a musica especifica da fase
        jogador_group = pygame.sprite.Group()
        jogador_group.add(self.__jogador)

        while True:

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_SPACE]:
                self.__jogador.pular()

            if self.jogador.morte:  # estado morto do jogador
                self.tela_de_morte()

            if keys_pressed[pygame.K_r] and self.jogador.morte:
                self.__jogador.resetar()
                self.iniciar_partida()

            self.__partida.screen.blit(bg_surface, (0, 0))
            self.__partida.desenhar_elementos()
            self.__partida.atualizar_level(self.jogador.velocidade.x)
            jogador_group.draw(self.__partida.screen)
            jogador_group.update(self.__partida.elements)

            clock.tick(FPS)

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
            f'{file_path_mapa}/mapa_teste4.json',
            f'{file_path_image}/bg.png')
        self.__partida = Partida('fase nao setada', self.__jogador)
        self.__fim_jogo = pygame.display.set_mode((800, 480))
        self.__tela_menu = pygame.display.set_mode(
            (800, 480))  # provavel mudar para classe view

    @property
    def jogador(self):
        return self.__jogador

    @property
    def fase(self):
        return self.__fase

    @property
    def partida(self):
        return self.__partida

    def tela_fim_de_jogo(self):
        pygame.mixer.music.stop()
        if self.jogador.morte:
            texto_mensagem = 'Você morreu!'
        else:
            texto_mensagem = 'Você venceu!'
        texto_opcoes = 'Aperte R para reiniciar e ESC para sair'
        fontesys60 = pygame.font.SysFont('calibri', 60)
        fontesys24 = pygame.font.SysFont('calibri', 24)
        tela_texto_mensagem = fontesys60.render(
            texto_mensagem, 1, (255, 255, 255))
        tela_texto_opcoes = fontesys24.render(texto_opcoes, 1, (255, 255, 255))
        self.__fim_jogo.blit(tela_texto_mensagem, (240, 200))
        self.__fim_jogo.blit(tela_texto_opcoes, (220, 280))
        pygame.display.update()

    def inicia_jogo(self):
        '''metodo para abrir a janela e dar switch entre modos'''
        pygame.init()

        FPS = 60
        clock = pygame.time.Clock()
        gamemode = 'on_menu'
        reinicia = False
        while True:
            print(gamemode)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if gamemode == 'on_menu':
                            pygame.display.quit()
                            pygame.quit()
                            exit()
                        elif gamemode == 'on_partida':
                            gamemode = 'on_menu'

            keys_pressed = pygame.key.get_pressed()

            # ativacao de partida
            if (keys_pressed[pygame.K_TAB] and gamemode == 'on_menu') or reinicia:
                # no inicia_variaveis eu seto uma fase para self.partida !
                jogador_group = self.partida.inicia_variaveis(self.__fase)
                gamemode = 'on_partida'

            # loops
            if gamemode == 'on_partida':
                reinicia = self.iniciar_partida(
                    jogador_group, keys_pressed)
            elif gamemode == 'on_menu':
                self.inicia_menu()
            clock.tick(FPS)

    def inicia_menu(self):
        '''metodo com o menu. APENAS PARA TESTES, MODIFICAR, TALVEZ CRIAR CLASSE.'''
        self.jogador.resetar()
        pygame.mixer.music.stop()
        self.__tela_menu.fill((0, 0, 0))
        texto_mensagem = 'MENU'
        texto_opcoes = 'Aperte tab para iniciar e ESC para sair'
        fontesys60 = pygame.font.SysFont('calibri', 60)
        fontesys24 = pygame.font.SysFont('calibri', 24)
        tela_texto_mensagem = fontesys60.render(
            texto_mensagem, 1, (255, 255, 255))
        tela_texto_opcoes = fontesys24.render(texto_opcoes, 1, (255, 255, 255))
        self.__tela_menu.blit(tela_texto_mensagem, (240, 200))
        self.__tela_menu.blit(tela_texto_opcoes, (220, 280))
        pygame.display.update()  # tela

    def iniciar_partida(self, jogador_group, keys_pressed):
        if self.jogador.morte or self.jogador.vitoria:
            self.tela_fim_de_jogo()

        else:
            if keys_pressed[pygame.K_SPACE]:
                self.jogador.pular()

            # self.partida.tela.blit(bg_surface, (0, 0))
            self.partida.draw_bg()
            self.partida.desenhar_elementos()
            self.partida.atualizar_nivel(self.jogador.velocidade.x)
            jogador_group.draw(self.partida.tela)
            jogador_group.update(self.partida.elementos)

        if keys_pressed[pygame.K_r]:
            self.jogador.resetar()
            return True
        else:
            return False

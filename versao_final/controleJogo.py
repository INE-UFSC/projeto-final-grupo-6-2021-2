import pygame
from pygame.locals import *
from random import choice
from jogador import Jogador
from partida import Partida
from menuView import menuView
from skin import Skin
from updater import Updater
from escolhaFasesView import EscolhaFasesView
from pauseView import pauseView


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
        self.__pause_view = pauseView()
        self.__partida = Partida(self.__fase, self.__jogador, self.tela)
        self.__updater = Updater(self.__jogador, self.__partida)
        self.FPS = 60

    @property
    def jogador(self):
        return self.__jogador

    @property
    def fase(self):
        return self.__fase

    @property
    def partida(self):
        return self.__partida

    def inicio_jogo(self):
        clock = pygame.time.Clock()
        while True:
            self.__menu_view.desenha()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    botao_selecionado = next(
                        (botao.mensagem for botao in self.__menu_view.lista_botoes if botao.is_clicked()), False)

                    if botao_selecionado == 'Jogar':
                        return self.escolha_fase()

                    if botao_selecionado == 'Sair':
                        pygame.display.quit()
                        pygame.quit()
                        exit()
                        
                    if botao_selecionado == 'Skins':
                        if self.__jogador.skin_atual.nome == 'Padrão':
                            self.__jogador.muda_skin(
                                choice(self.__skins))
                        else:
                            self.__jogador.muda_skin(
                                Skin('Padrão', 'geo.png'))
                        print('Feedback: Mudou de skin!')

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
        self.partida.inicia()

        jogador_group = pygame.sprite.Group()
        jogador_group.add(self.jogador)
        pausar_jogo = False

        while True:
            pygame.display.update()
            if not pausar_jogo:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.display.quit()
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            pausar_jogo = True

            keys_pressed = pygame.key.get_pressed()

            if pausar_jogo:
                jogo_pausado = self.pausar_jogo()
                if jogo_pausado: pausar_jogo = False

            if self.jogador.morte or self.jogador.vitoria:
                self.partida.desenha_fim_de_jogo()

            else:

                if keys_pressed[K_SPACE]:
                    if self.jogador.nochao:
                        self.jogador.pular()

                self.partida.draw_bg()
                self.partida.desenhar_elementos()
                self.__updater.update_partida(self.jogador.velocidade.x)
                jogador_group.draw(self.partida.tela)
                self.__updater.update_jogador(
                    self.partida.elementos, keys_pressed)

            if keys_pressed[K_r]:
                self.jogador.resetar()
                self.partida.para_musica()
                self.iniciar_partida()

            clock.tick(self.FPS)
            
    def pausar_jogo(self):
        self.partida.para_musica()
        self.jogador.parar_jogador()

        self.partida.tela.blit(self.__pause_view.tela, (150, 140))
        self.__pause_view.desenha(self.partida.tela)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                botao_selecionado = next(
                    (botao.mensagem for botao in self.__pause_view.lista_botoes if botao.is_clicked()), False)

                if botao_selecionado == 'Continuar':
                    self.jogador.continuar_jogador()
                    self.partida.toca_musica()
                    return True
                    
                if botao_selecionado == 'Menu':
                    self.jogador.resetar()
                    self.partida.para_musica()
                    self.inicio_jogo()
                
                if botao_selecionado == 'Resetar':
                    self.jogador.resetar()
                    self.partida.para_musica()
                    self.iniciar_partida()
                    
                if botao_selecionado == 'Sair':
                    self.jogador.resetar()
                    self.partida.para_musica()
                    pygame.display.quit()
                    pygame.quit()
                    exit()

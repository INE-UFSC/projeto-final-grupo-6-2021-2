import pygame
from pygame.locals import *
from jogador import Jogador
from partida import Partida
from menuView import menuView
from updater import Updater
from escolhaFasesView import EscolhaFasesView
from pauseView import pauseView
from menuSkin import MenuSkin
from LoadedImages import loaded_images
from containerSkins import ContainerSkins
from instrucoesView import InstrucoesView
from containerFases import ContainerFases


class ControleJogo():

    def __init__(self):
        pygame.init()
        self.tela = loaded_images.tela
        self.__container_skin = ContainerSkins()
        self.__container_fase = ContainerFases()
        self.__jogador = Jogador(self.__container_skin)
        self.__menu_view = menuView(self.tela)
        self.__escolha_fase_view = EscolhaFasesView(
            self.tela, self.__container_fase.fases)
        self.__pause_view = pauseView()
        self.__partida = Partida(None, self.__jogador, self.tela)
        self.__updater = Updater(self.__jogador, self.__partida)
        self.__intrucoes_view = InstrucoesView(self.tela)
        self.__menu_skin = MenuSkin(
            self.tela, self.__container_skin.skins_quadrado)

        self.FPS = 60

    @property
    def jogador(self):
        return self.__jogador

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

                    elif botao_selecionado == 'Skins':
                        return self.selecao_skin()

                    elif botao_selecionado == 'Instruções':
                        return self.mostra_intrucoes()

                    elif botao_selecionado == 'Sair':
                        pygame.display.quit()
                        pygame.quit()
                        exit()

            clock.tick(self.FPS)

    def mostra_intrucoes(self):
        clock = pygame.time.Clock()
        while True:
            self.__intrucoes_view.desenha()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    if self.__intrucoes_view.botao_voltar.is_clicked():
                        return self.inicio_jogo()

            clock.tick(self.FPS)

    def selecao_skin(self):
        clock = pygame.time.Clock()
        while True:
            self.__menu_skin.desenha()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    for botao_tup in self.__menu_skin.lista_botoes:
                        if botao_tup[0].is_clicked() and botao_tup[0].mensagem == 'Voltar':
                            return self.inicio_jogo()
                        elif botao_tup[0].is_clicked():
                            # clicou em um botão e não é o de voltar
                            skin = self.__container_skin.skins_quadrado[botao_tup[1]]
                            self.__jogador.muda_skin(skin)
                            self.__menu_skin.seleciona_skin(skin.arquivo)

            clock.tick(self.FPS)

    def escolha_fase(self):
        clock = pygame.time.Clock()
        while True:
            self.__escolha_fase_view.desenha()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()
                # detectao de cliques
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for botao_tup in self.__escolha_fase_view.lista_botoes:
                        if botao_tup[0].is_clicked() and botao_tup[0].mensagem == 'Voltar':
                            return self.inicio_jogo()

                        elif botao_tup[0].is_clicked():
                            # clicou em um botão e não é o de voltar
                            self.__partida.fase = self.__container_fase.fases[botao_tup[1]]
                            return self.iniciar_partida()

            clock.tick(self.FPS)

    def iniciar_partida(self):
        clock = pygame.time.Clock()
        self.jogador.muda_skin(self.jogador.skin_atual)
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

            if self.jogador.morte or self.jogador.vitoria:
                self.partida.desenha_fim_de_jogo()

            else:
                if keys_pressed[K_SPACE]:
                    if self.jogador.voo:
                        self.jogador.velocidade.y = 0
                        self.jogador.pular()
                    else:
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

            if pausar_jogo:
                jogo_pausado = self.pausar_jogo()
                if jogo_pausado:
                    pausar_jogo = False

            clock.tick(self.FPS)

    def pausar_jogo(self):
        self.partida.pausa_musica()
        self.jogador.parar_jogador()

        self.partida.tela.blit(self.__pause_view.tela, (150, 140))
        self.__pause_view.desenha(self.partida.tela)

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
                    self.partida.despausa_musica()
                    return True

                elif botao_selecionado == 'Menu':
                    self.jogador.resetar()
                    self.partida.para_musica()
                    self.inicio_jogo()

                elif botao_selecionado == 'Resetar':
                    self.jogador.resetar()
                    self.partida.para_musica()
                    self.iniciar_partida()

                elif botao_selecionado == 'Sair':
                    self.jogador.resetar()
                    self.partida.para_musica()
                    pygame.display.quit()
                    pygame.quit()
                    exit()

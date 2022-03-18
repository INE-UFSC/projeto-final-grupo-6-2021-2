import pygame
from pygame.locals import *
from fimDeFaseView import fimDeFaseView
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
from proximaFaseView import proximaFaseView
from fimDeJogoView import fimDeJogoView


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
        self.fim_de_fase = fimDeFaseView()
        self.proxima_fase = proximaFaseView()
        self.fim_de_jogo = fimDeJogoView()
        self.flag_transparencia = False

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
                        if botao_tup[0].is_clicked(
                        ) and botao_tup[0].mensagem == 'Voltar':
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
                        if botao_tup[0].is_clicked(
                        ) and botao_tup[0].mensagem == 'Voltar':
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
        flag_pausar_jogo = False
        jogando = True

        while True:
            pygame.display.update()
            if not flag_pausar_jogo and not self.jogador.morte and not self.jogador.vitoria:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.display.quit()
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            if not self.jogador.morte and not self.jogador.vitoria and not flag_pausar_jogo:
                                self.partida.tela.blit(
                                    self.__pause_view.tela, (150, 140))
                                flag_pausar_jogo = True
                                jogando = False

            keys_pressed = pygame.key.get_pressed()

            if flag_pausar_jogo:
                jogando = False
                sair_do_jogo_pausado = self.pausar_jogo()
                if sair_do_jogo_pausado:
                    flag_pausar_jogo = False
                    jogando = True

            if self.jogador.morte:
                jogando = False
                self.tela.blit(self.fim_de_fase.tela, (150, 140)
                               ) if not self.flag_transparencia else None
                self.flag_transparencia = True
                self.perdeu_a_fase()

            index_fase_atual = self.__container_fase.fases.index(self.__partida.fase)
            if self.jogador.vitoria and index_fase_atual+1 == len(self.__container_fase.fases):
                jogando = False
                self.tela.blit(self.fim_de_jogo.tela, (150, 140)
                               ) if not self.flag_transparencia else None
                self.flag_transparencia = True
                self.terminou_o_jogo()

            if self.jogador.vitoria and not index_fase_atual+1 == len(self.__container_fase.fases):
                jogando = False
                self.tela.blit(self.proxima_fase.tela, (150, 140)
                               ) if not self.flag_transparencia else None
                self.flag_transparencia = True
                self.passou_de_fase()

            if jogando:
                self.flag_transparencia = False
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

            clock.tick(self.FPS)

    def perdeu_a_fase(self):
        self.partida.para_musica()
        self.fim_de_fase.desenha_mensagem(self.tela)
        self.fim_de_fase.desenha(self.tela)
        botao_selecionado = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    botao_selecionado = next(
                        (botao.mensagem for botao in self.fim_de_fase.lista_botoes if botao.is_clicked()), False)

        if botao_selecionado:
            if botao_selecionado == 'Menu':
                self.jogador.resetar()
                self.partida.para_musica()
                self.inicio_jogo()

            elif botao_selecionado == 'Reiniciar':
                self.jogador.resetar()
                self.partida.para_musica()
                self.iniciar_partida()

            elif botao_selecionado == 'Sair':
                self.jogador.resetar()
                self.partida.para_musica()
                pygame.display.quit()
                pygame.quit()
                exit()

    def passou_de_fase(self):
        self.partida.para_musica()
        self.proxima_fase.desenha_mensagem(self.tela)
        self.proxima_fase.desenha(self.tela)
        botao_selecionado = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    botao_selecionado = next(
                        (botao.mensagem for botao in self.proxima_fase.lista_botoes if botao.is_clicked()), False)

        if botao_selecionado:
            if botao_selecionado == 'Proxima fase':
                self.jogador.resetar()
                self.partida.para_musica()
                index_fase_atual = self.__container_fase.fases.index(self.__partida.fase)
                self.__partida.fase = self.__container_fase.fases[index_fase_atual+1]
                self.partida.fase = self.__fase
                self.iniciar_partida()

            if botao_selecionado == 'Menu':
                self.jogador.resetar()
                self.partida.para_musica()
                self.inicio_jogo()

            elif botao_selecionado == 'Reiniciar':
                self.jogador.resetar()
                self.partida.para_musica()
                self.iniciar_partida()

            elif botao_selecionado == 'Sair':
                self.jogador.resetar()
                self.partida.para_musica()
                pygame.display.quit()
                pygame.quit()
                exit()

    def terminou_o_jogo(self):
        self.partida.para_musica()
        self.fim_de_jogo.desenha_mensagem(self.tela)
        self.fim_de_jogo.desenha(self.tela)
        botao_selecionado = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    botao_selecionado = next(
                        (botao.mensagem for botao in self.fim_de_jogo.lista_botoes if botao.is_clicked()), False)

        if botao_selecionado:
            if botao_selecionado == 'Reiniciar':
                self.jogador.resetar()
                self.partida.para_musica()
                self.iniciar_partida()

            elif botao_selecionado == 'Menu':
                self.jogador.resetar()
                self.partida.para_musica()
                self.inicio_jogo()

            elif botao_selecionado == 'Sair':
                self.jogador.resetar()
                self.partida.para_musica()
                pygame.display.quit()
                pygame.quit()
                exit()

    def pausar_jogo(self):
        self.partida.pausa_musica()
        self.jogador.parar_jogador()
        self.__pause_view.desenha(self.partida.tela)
        botao_selecionado = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    botao_selecionado = next(
                        (botao.mensagem for botao in self.__pause_view.lista_botoes if botao.is_clicked()), False)

        if botao_selecionado:
            if botao_selecionado == 'Continuar':
                self.jogador.continuar_jogador()
                self.partida.despausa_musica()
                return True

            elif botao_selecionado == 'Menu':
                self.jogador.resetar()
                self.partida.para_musica()
                self.inicio_jogo()

            elif botao_selecionado == 'Reiniciar':
                self.jogador.resetar()
                self.partida.para_musica()
                self.iniciar_partida()

            elif botao_selecionado == 'Sair':
                self.jogador.resetar()
                self.partida.para_musica()
                pygame.display.quit()
                pygame.quit()
                exit()

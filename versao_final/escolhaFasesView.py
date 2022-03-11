import pygame
from pygame.locals import *
from botao_menu import Botao
from filePaths import file_paths
from fase import Fase


class EscolhaFasesView():

    def __init__(self, tela) -> None:
     # devo pegar fases do container no futuro. e instanciar em outro lugar
        self.fase01 = Fase(
            'Fase 1',
            f'{file_paths.musicas}/undertale-megalovania.mp3',
            f'{file_paths.mapas}/mapa_teste4.json',
            f'{file_paths.imagens}/bg.png')

        fonte_botao = pygame.font.SysFont('calibri', 20)
        self.__tela = tela

        self.fundo = pygame.image.load(
            f'{file_paths.imagens}/menu_view/tela_fases.png')
        self.fundo = pygame.transform.smoothscale(
            self.fundo.convert(), (800, 500))

        # só colocar texto não funcionou por enquanto
        self.fundo_fase = pygame.image.load(
            f'{file_paths.imagens}/menu_view/ret_menu.png')

        self.fundo_fase = pygame.transform.smoothscale(
            self.fundo_fase.convert(), (100, 100))

        # Lista deve ser automatizada no futuro. Atualmente, tuple com botao e fase (ou key voltar)
        self.lista_botoes = [
            (Botao(self.fundo_fase, 100, 100, 'Fase 01', fonte_botao,
             (255, 255, 255), (255, 137, 6)), self.fase01),

            (Botao(
                self.fundo_fase, 100, 300, 'Voltar', fonte_botao, (255, 255, 255), (255, 137, 6)), 'Voltar')
        ]

        # BOTÕES: jogar, skins, instrucoes, sair

    '''param :mouse_pos: entregue pelo pygame dentro do loop'''

    def desenha(self, mouse_pos):
        self.__tela.blit(self.fundo, (0, 0))

        for botao_tup in self.lista_botoes:
            botao_tup[0].update(self.__tela)
            botao_tup[0].muda_cor(mouse_pos)

        pygame.display.update()  # tela
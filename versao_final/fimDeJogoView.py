import pygame
from pygame.locals import *
from botao_menu import Botao
from LoadedImages import loaded_images


class fimDeJogoView():

    def __init__(self) -> None:
        tela = pygame.Surface((500, 200), pygame.SRCALPHA)
        pygame.draw.rect(tela, (250, 250, 250, 50), tela.get_rect(), 99)
        self.tela = tela

        texto_parabens = 'Parabéns!'
        texto_mensagem = 'Você terminou o jogo'

        fontesys24 = pygame.font.SysFont('calibri', 24)
        fontesys18 = pygame.font.SysFont('calibri', 18)
        self.tela_texto_parabens = fontesys24.render(
            texto_parabens, 1, (0, 0, 0))
        self.tela_texto_mensagem = fontesys18.render(
            texto_mensagem, 1, (0, 0, 0))

        fonte_botao = pygame.font.SysFont('calibri', 20)
        fundo_botao = loaded_images.imagens_botoes['Ret_select_rosa']

        self.lista_botoes = [
            Botao(imagem=fundo_botao, x_pos=300, y_pos=280,
                  mensagem='Reiniciar', fonte=fonte_botao,
                  cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)),
            Botao(imagem=fundo_botao, x_pos=410, y_pos=280,
                  mensagem='Menu', fonte=fonte_botao,
                  cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)),
            Botao(imagem=fundo_botao, x_pos=520, y_pos=280,
                  mensagem='Sair', fonte=fonte_botao,
                  cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)),
        ]

    def desenha_mensagem(self, tela):
        tela.blit(self.tela_texto_parabens, (350, 160))
        tela.blit(self.tela_texto_mensagem, (320, 200))

    def desenha(self, tela):
        for botao in self.lista_botoes:
            botao.update(tela)
            botao.muda_cor()

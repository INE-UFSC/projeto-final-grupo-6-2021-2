import pygame
from pygame.locals import *
from botao_menu import Botao
from LoadedImages import loaded_images


class proximaFaseView():

    def __init__(self) -> None:
        fonte_botao = pygame.font.SysFont('calibri', 20)

        tela = pygame.Surface((500, 200), pygame.SRCALPHA)
        pygame.draw.rect(tela, (250, 250, 250, 50), tela.get_rect(), 99)
        self.tela = tela

        texto_mensagem = 'Você ganhou!'
        fontesys24 = pygame.font.SysFont('calibri', 24)
        self.tela_texto_mensagem = fontesys24.render(texto_mensagem, 1, (0, 0, 0))

        self.fundo_botao = loaded_images.imagens_botoes['Ret_select_rosa']
        self.fundo_botao_grande = loaded_images.imagens_botoes['Ret_select_rosa_120']

        self.lista_botoes = [
            Botao(imagem=self.fundo_botao_grande, x_pos=240, y_pos=280,
                  mensagem='Proxima fase', fonte=fonte_botao,
                  cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)),
            Botao(imagem=self.fundo_botao, x_pos=360, y_pos=280,
                  mensagem='Reiniciar', fonte=fonte_botao,
                  cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)),
            Botao(imagem=self.fundo_botao, x_pos=470, y_pos=280,
                  mensagem='Menu', fonte=fonte_botao,
                  cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6)),
            Botao(imagem=self.fundo_botao, x_pos=580, y_pos=280,
                  mensagem='Sair', fonte=fonte_botao,
                  cor_base_texto=(255, 255, 255), cor_mouse=(255, 137, 6))
        ]

    def desenha(self, tela):
        for botao in self.lista_botoes:
            botao.update(tela)
            botao.muda_cor()

        tela.blit(self.tela_texto_mensagem, (320, 200))

        pygame.display.update()

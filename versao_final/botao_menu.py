
import pygame


class Botao():
    # FALTA ENCAPSULAR
    def __init__(self, imagem, x_pos, y_pos, mensagem, fonte,
                 cor_base_texto, cor_mouse):
        self.imagem = imagem
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.mensagem = mensagem
        self.fonte_texto = fonte
        self.cor_base_texto = cor_base_texto
        self.cor_mouse = cor_mouse
        self.text = self.fonte_texto.render(
            self.mensagem, True, self.cor_base_texto)

        if self.imagem is None:
            self.__cria_botao_com_texto()

        self.rect = self.imagem.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def __cria_botao_com_texto(self):
        self.imagem = self.mensagem

    def update(self, tela):
        if self.imagem is not None:
            tela.blit(self.imagem, self.rect)
        tela.blit(self.text, self.text_rect)

    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

    '''
	Mesma funcionalidade da função acima, porém é feita para rodar sempre
	no loop principal para mudar a cor do texto caso o mouse esteja sobre o botão
	'''

    def muda_cor(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.text = self.fonte_texto.render(
                self.mensagem, True, self.cor_mouse)
        else:
            self.text = self.fonte_texto.render(
                self.mensagem, True, self.cor_base_texto)

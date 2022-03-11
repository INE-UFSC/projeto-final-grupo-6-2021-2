from obstaculos import *
from pygame import mixer


class Partida():

    def __init__(self, fase, jogador, tela) -> None:
        self.fase = fase
        self.elementos = []
        self.jogador = jogador
        self.tela = tela
        self.bg_x = 0

    def inicia(self):
        '''chama todos seus métodos necessários'''
        self.elementos.clear()
        mapa = self.fase.mapear_fase()
        self.desenhar_nivel(mapa)
        self.toca_musica()

    def draw_bg(self):
        # desenha o fundo da fase com x variavel para dar movimento
        self.tela.blit(self.fase.bg, (self.bg_x, 0))
        self.tela.blit(self.fase.bg, (self.bg_x+990, 0))

    def desenhar_nivel(self, mapa):
        # Lê a matriz do mapa e instancia os objetos
        x = 0
        y = 0
        for row in mapa:
            for col in row:

                if col == 2:
                    objeto = Block((x, y))
                    self.elementos.append(objeto)
                elif col == 1:
                    objeto = Spike((x, y))
                    self.elementos.append(objeto)
                elif col == 3:
                    objeto = Win((x, y))
                    self.elementos.append(objeto)
                elif col == 4:
                    objeto = Orb((x, y))
                    self.elementos.append(objeto)
                x += 24
            y += 24
            x = 0

    def atualizar_nivel(self, velocidade):
        # Movimenta o mapa inteiro para dar impressão de movimento
        for sprite in self.elementos:
            sprite.rect.x -= velocidade

    def desenhar_elementos(self):
        for x in self.elementos:
            self.tela.blit(x.image, (x.rect.x, x.rect.y))

    def desenha_fim_de_jogo(self):
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
        self.tela.blit(tela_texto_mensagem, (240, 200))
        self.tela.blit(tela_texto_opcoes, (220, 280))
        pygame.display.update()

    def toca_musica(self):
        mixer.init()
        mixer.music.load(self.fase.musica)
        mixer.music.play()

    def para_musica(self):
        # diferente de pausar, ela para e da unload.
        mixer.music.stop()
        mixer.music.unload()

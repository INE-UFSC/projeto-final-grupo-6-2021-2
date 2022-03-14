from fimDeJogoView import fimDeJogoView
from obstaculos import *
from pygame import mixer


class Partida():

    def __init__(self, fase, jogador, tela) -> None:
        self.fase = fase
        self.elementos = []
        self.jogador = jogador
        self.tela = tela
        self.bg_x = 0
        self.floor_x = 0

    def inicia(self):
        '''chama todos seus métodos necessários'''
        self.elementos.clear()
        self.desenhar_nivel(self.fase.mapa)
        self.toca_musica()

    def draw_bg(self):
        # desenha o fundo da fase com x variavel para dar movimento
        self.tela.blit(self.fase.bg, (self.bg_x, 0))
        self.tela.blit(self.fase.bg, (self.bg_x + 990, 0))
        self.tela.blit(self.fase.floor, (self.floor_x, 456))
        self.tela.blit(self.fase.floor, (self.floor_x + 990, 456))

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
                elif col == 5:
                    objeto = Portal((x, y))
                    self.elementos.append(objeto)
                elif col == 6:
                    objeto = PortalSaida((x, y))
                    self.elementos.append(objeto)
                x += 24
            y += 24
            x = 0

    def desenhar_elementos(self):
        for x in self.elementos:
            self.tela.blit(x.image, (x.rect.x, x.rect.y))

    def toca_musica(self):
        mixer.init()
        mixer.music.load(self.fase.musica)
        mixer.music.set_volume(self.fase.volume_musica)
        mixer.music.play()

    def para_musica(self):
        # diferente de pausar, ela para e da unload.
        mixer.music.stop()
        mixer.music.unload()

    def pausa_musica(self):
        mixer.music.pause()

    def despausa_musica(self):
        mixer.music.unpause()

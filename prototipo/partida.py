from jogador import Jogador
from fase import Fase
import os
from obstaculos import *

current_directory = os.path.dirname(__file__)
file_path_mapa = os.path.join(current_directory, 'Mapas')


class Partida():


    def __init__(self, fase, player) -> None:
        self.fase = fase
        self.elements = []
        self.player = player
        self.screen = pygame.display.set_mode((800, 480))

    def iniciar_partida(self):
        pygame.init()

        FPS = 60
        clock = pygame.time.Clock()

        PRETO = (34, 40, 49)
        BRANCO = (240, 240, 240)

        bg_surface = pygame.image.load(f'{file_path_image}/bg.png')
        bg_surface = pygame.transform.smoothscale(bg_surface, (800, 480))
        mapa = self.fase.mapear_fase()
        self.desenhar_level(mapa)
        jogador_group = pygame.sprite.Group()
        jogador_group.add(self.player)
        while True: 
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
            

            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_SPACE]:
                self.player.pular()

            self.screen.blit(bg_surface,(0,0))
            self.desenhar_elementos()
            self.atualizar_level(self.player.vel.x)
            jogador_group.draw(self.screen)
            jogador_group.update(self.elements)
            clock.tick(FPS)

    def desenhar_level(self, mapa):

        """this is similar to 2d lists. it goes through a list of lists, and creates instances of certain obstacles
        depending on the item in the list"""
        x = 0
        y = 0
        for row in mapa:
            for col in row:
                
                if col == 1:
                    objeto = Block((x, y))
                    self.elements.append(objeto)
                if col == 2:
                    objeto = Spike((x, y))
                    self.elements.append(objeto)
                x += 24
            y += 24
            x = 0

    def atualizar_level(self, velocidade):
        for sprite in self.elements:
            sprite.rect.x -= velocidade
            #if sprite.rect.x <= -50:
            #    self.elements.remove(sprite)
        
    def desenhar_elementos(self):
        for x in self.elements:
            self.screen.blit(x.image, (x.rect.x, x.rect.y))

player = Jogador()
fase = Fase('teste', '', f'{file_path_mapa}/mapa_teste3.json')

JOGO = Partida(fase, player)

JOGO.iniciar_partida()
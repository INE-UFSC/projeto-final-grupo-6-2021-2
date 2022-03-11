from colisao import Colisao


class Updater():

    def __init__(self, jogador, partida) -> None:
        self.__jogador = jogador
        self.__partida = partida
        self.__colisor = Colisao(
            self.__jogador, self.__partida.tela, self.__partida.elementos)

    def update_jogador(self, grupo, key):
        jogador = self.__jogador
        # Caso não encoste no chão, a gravidade começa a agir no jogador
        if not jogador.morte:
            if not jogador.nochao:
                jogador.velocidade.y += jogador.gravidade
                # Verifica colisão no eixo X
                self.__colisor.collide(0, key)

            if jogador.velocidade.y == - 8.5:
                jogador.image, jogador.rect = jogador.rotate(
                    jogador.image, jogador.rect, -90)

            jogador.rect.top += jogador.velocidade.y
            jogador.nochao = False
            # Verifica colisão no eixo Y
            self.__colisor.collide(jogador.velocidade.y, key)

    def update_partida(self, velocidade):
        # Movimenta o mapa inteiro para dar impressão de movimento
        for sprite in self.__partida.elementos:
            sprite.rect.x -= velocidade

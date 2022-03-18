from colisao import Colisao


class Updater():

    def __init__(self, jogador, partida) -> None:
        self.__jogador = jogador
        self.__partida = partida
        self.__colisor = Colisao(
            self.__jogador, self.__partida.tela, self.__partida.elementos)

    def update_jogador(self, key) -> None:
        '''
        Atualiza o jogador em cima da gravidade e das colisões que ele faz.

            Parameters:
                key (int): Tecla clicada no teclado

            Returns:
                None
        '''
        jogador = self.__jogador

        # Caso não encoste no chão, a gravidade começa a agir no jogador
        if not jogador.morte:
            if not jogador.nochao:
                jogador.velocidade.y += jogador.gravidade
                # Verifica colisão no eixo X
                self.__colisor.collide(0, key)

            jogador.rect.top += jogador.velocidade.y
            jogador.nochao = False

            # Verifica colisão no eixo Y
            if jogador.rect.bottom >= 456:
                jogador.nochao = True
                jogador.rect.bottom = 456
                jogador.velocidade.y = 0
                if self.__jogador.voo:
                    self.__jogador.morte = True

            self.__colisor.collide(jogador.velocidade.y, key)

    def update_partida(self, velocidade) -> None:
        '''
        Atualiza a partida e movimenta o mapa para dar impressão de movimento.

            Parameters:
                velocidade (int): Velocidade do jogador na abscissa

            Returns:
                None
        '''
        for sprite in self.__partida.elementos:
            sprite.rect.x -= velocidade
        self.__partida.floor_x -= velocidade
        if self.__partida.floor_x <= -990:
            self.__partida.floor_x = 0

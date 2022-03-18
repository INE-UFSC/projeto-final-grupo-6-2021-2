from colisao import Colisao


class Updater():

    def __init__(self, jogador, partida) -> None:
        self.__jogador = jogador
        self.__partida = partida
        self.__colisor = Colisao(
            self.__jogador, self.__partida.tela, self.__partida.elementos)

    @property
    def jogador(self):
        return self.__jogador
    
    @property
    def partida(self):
        return self.__partida

    @property
    def colisor(self):
        return self.__colisor
    
    def update_jogador(self, key) -> None:
        '''
        Atualiza o jogador em cima da gravidade e das colisões que ele faz.

            Parameters:
                key (int): Tecla clicada no teclado

            Returns:
                None
        '''
        jogador = self.jogador
        colisor = self.colisor

        # Caso não encoste no chão, a gravidade começa a agir no jogador
        if not jogador.morte:
            if not jogador.nochao:
                jogador.velocidade.y += jogador.gravidade
                # Verifica colisão no eixo X
                colisor.collide(0, key)

            jogador.rect.top += jogador.velocidade.y
            jogador.nochao = False

            #Define um chão
            if jogador.rect.bottom >= 456:
                jogador.nochao = True
                jogador.rect.bottom = 456
                jogador.velocidade.y = 0
                if jogador.voo:
                   jogador.morte = True
            
            #Não deixa o modo voador passar do teto
            if jogador.rect.top <= -20 and jogador.voo:
                jogador.morte = True

            # Verifica colisão no eixo Y
            colisor.collide(jogador.velocidade.y, key)

    def update_partida(self, velocidade) -> None:
        '''
        Atualiza a partida e movimenta o mapa para dar impressão de movimento.

            Parameters:
                velocidade (int): Velocidade do jogador na abscissa

            Returns:
                None
        '''
        for sprite in self.partida.elementos:
            sprite.rect.x -= velocidade
        self.partida.floor_x -= velocidade
        if self.partida.floor_x <= -990:
            self.partida.floor_x = 0

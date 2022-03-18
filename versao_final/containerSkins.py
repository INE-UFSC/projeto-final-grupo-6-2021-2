from skin import Skin
from LoadedImages import loaded_images


class ContainerSkins():
    def __init__(self) -> None:
        self.skins_quadrado = [
            Skin('Padrão', loaded_images.imagens_skins['Padrão']),
            Skin('Azul', loaded_images.imagens_skins['Azul']),
            Skin('Glitch', loaded_images.imagens_skins['Glitch']),
            Skin('Mine', loaded_images.imagens_skins['Mine']),
            Skin('Cubo Mágico', loaded_images.imagens_skins['Cubo Mágico']),
            Skin('Pride', loaded_images.imagens_skins['Pride'])
        ]

        self.skin_nave = Skin('Nave', loaded_images.skin_nave)

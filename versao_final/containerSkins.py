from skin import Skin
from LoadedImages import loaded_images


class ContainerSkins():
    def __init__(self) -> None:
        # Skin('Nave', 'nave teste.png')
        self.skins_quadrado = [
            Skin('Padrão', loaded_images.imagens_skins['Padrão']),
            Skin('Azul', loaded_images.imagens_skins['Azul']),
            Skin('Beta', loaded_images.imagens_skins['Beta']),
            Skin('Beta', loaded_images.imagens_skins['Beta'])
        ]

        self.skin_nave = Skin('Nave', loaded_images.skin_nave)

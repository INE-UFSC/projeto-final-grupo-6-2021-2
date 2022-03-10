
class Skin():
    
    def __init__(self, nome: str, arquivo: str):
        self.__nome = nome
        self.__arquivo = arquivo

    def __str__(self):
        return self.__nome
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def arquivo(self):
        return self.__arquivo

    @arquivo.setter
    def arquivo(self, value):
        self.__arquivo = value
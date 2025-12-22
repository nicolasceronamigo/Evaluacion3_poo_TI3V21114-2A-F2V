from abc import ABC, abstractmethod


class Vehiculo(ABC):
    def __init__(self, patente: str):
        self.__patente = patente
        self.__tipo = type(self).__name__
    
    def get_patente(self):
        return self.__patente
    
    def get_tipo(self):
        return self.__tipo
    
    @abstractmethod
    def cobrar(self, tiempo):
        return 
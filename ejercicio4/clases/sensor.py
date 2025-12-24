from abc import ABC, abstractmethod


class Sensor(ABC):
    def __init__(self, id_sensor: int):
        self.__id_sensor = id_sensor
        self.__lista_mediciones = []
    
    def get_lista_mediciones(self):
        return self.__lista_mediciones
    
    def get_id_sensor(self):
        return self.__id_sensor
    
    @abstractmethod
    def medir(self):
        pass
    
    @abstractmethod
    def medir_unidad(self):
        pass
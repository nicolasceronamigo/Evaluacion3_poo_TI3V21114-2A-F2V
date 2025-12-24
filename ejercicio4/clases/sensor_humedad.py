from clases.sensor import Sensor


import random

class SensorHumedad(Sensor):
    def __init__(self, id_sensor):
        super().__init__(id_sensor)
        self.__unidad_medida = "%" #en realidad no es una unidad de medida
        self.__valor_maximo = 100 #valor por defecto
        self.__valor_minimo = 0
    
    def set_val_max(self, val_max):
        if val_max > 100:
            return f"Valor máximo de humedad no puede ser mayor que 100"
        self.__valor_maximo = val_max
    
    def set_val_min(self, val_min):
        if val_min < 0:
            return f"Valor mínimo de humedad no pede ser menor que 0"
        self.__valor_minimo = val_min
    
    def medir(self):
        valor_medicion = random.random() #medicion simulada
        return valor_medicion
    
    def medir_unidad(self):
        valor_medicion = self.medir() * self.__valor_maximo
        self.get_lista_mediciones().append(valor_medicion)
        return valor_medicion
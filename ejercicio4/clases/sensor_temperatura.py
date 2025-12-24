from clases.sensor import Sensor

import random

from herramientas.herramientas import kelvin_a_celsius, kelvin_a_fahr


class SensorTemperatura(Sensor):
    def __init__(self, id_sensor):
        super().__init__(id_sensor)
        self.__unidad_medida = "K" #por defecto se mide en Kelvin
        self.__valor_maximo = 1000 
        self.__valor_minimo = 0
    
    def set_unidad_medida(self, un_med):
        match un_med:
            case "K":
                self.__unidad_medida = "K"
                return f"Sensor {self.__id_sensor} calibrado a K"
            case "C":
                self.__unidad_medida = "C"
                return f"Sensor {self.__id_sensor} calibrado a grados °C"
            case "F":
                self.__unidad_medida = "F"
                return f"Sensor {self.__id_sensor} calibrado a grados °F"
            case _:
                return f"Unidad {un_med} desconocida"
    
    def set_val_max(self, val_max):
        self.__valor_maximo = val_max
    
    def set_val_min(self, val_min):
        if val_min >= 0: #cero absoluto, las temperaturas en kelvin siempre son positivas
            self.__valor_minimo = val_min
    
    def medir(self):
        valor_medicion = random.random() #medicion simulada
        valor_medicion = valor_medicion * (self.__valor_maximo - self.__valor_minimo)
        return valor_medicion
    
    def medir_unidad(self):
        match self.__unidad_medida:
            case "K":
                valor_medicion = self.medir()
                self.get_lista_mediciones().append({self.__unidad_medida: valor_medicion})
                return valor_medicion
            case "C":
                valor_medicion = kelvin_a_celsius(self.medir())
                self.get_lista_mediciones().append({self.__unidad_medida: valor_medicion})
                return valor_medicion
            case "F":
                valor_medicion = kelvin_a_fahr(self.medir())
                self.get_lista_mediciones().append({self.__unidad_medida: valor_medicion})
                return valor_medicion
            case _:
                return f"Unidad {self.__unidad_medida} desconocida"
from clases.vehiculo import Vehiculo
from herramientas.herramientas import interseccion_intervalos
import datetime
import math


inicio_horario_punta = datetime.datetime(2025, 12, 21, hour = 12)
fin_horario_punta = datetime.datetime(2025, 12, 21, hour = 16)
recargo_horario_punta = 5001

class Estadia:
    def __init__(self, vehiculo: Vehiculo, hora_entrada: datetime, hora_salida: datetime):
        self.__patente = vehiculo.get_patente()
        self.__tipo = vehiculo.get_tipo()
        self.__vehiculo = vehiculo
        self.__hora_entrada = hora_entrada
        self.__hora_salida = hora_salida
    
    def get_patente(self):
        return self.__patente
    
    def get_tipo(self):
        return self.__tipo
    
    def get_hora_entrada(self):
        return self.__hora_entrada
    
    def get_hora_salida(self):
        return self.__hora_salida
    
    def en_horario_punta(self) -> bool:
        return interseccion_intervalos(self.__hora_entrada, self.__hora_salida, inicio_horario_punta, fin_horario_punta)
    
    def calc_horas(self):
        diferencia = self.__hora_salida - self.__hora_entrada
        return math.ceil(diferencia.seconds / 3600)
    
    def calc_cobro(self):
        tiempo = self.calc_horas()
        cobro = self.__vehiculo.cobrar(tiempo)
        if self.en_horario_punta():
            cobro += recargo_horario_punta
        return cobro
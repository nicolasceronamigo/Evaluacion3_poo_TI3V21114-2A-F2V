from clases.sensor import Sensor


import random

class SensorMovimiento(Sensor):
    def medir(self):
        valor_medido = random.randint(0, 1) #solo detecta si hay o no movimiento
        return valor_medido
    
    def medir_unidad(self):
        valor_medido = self.medir()
        self.get_lista_mediciones().append(valor_medido)
        return valor_medido
from clases.sensor import Sensor


import random

class SensorMovimiento(Sensor):
    def medir(self):
        valor_medido = random.randint(0, 1) #solo detecta si hay o no movimiento
        return valor_medido
    
    def medir_unidad(self):
        valor_medido = self.medir()
        match valor_medido:
            case 0:
                valor_medicion = False
                self.get_lista_mediciones().append(valor_medicion)
                return valor_medicion
            case 1:
                valor_medicion = True
                self.get_lista_mediciones().append(valor_medicion)
                return valor_medicion
            case _:
                return f"Valor inesperado {valor_medido}"
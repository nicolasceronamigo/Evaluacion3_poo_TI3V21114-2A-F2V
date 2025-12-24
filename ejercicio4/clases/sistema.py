from clases.sensor_humedad import SensorHumedad
from clases.sensor_movimiento import SensorMovimiento
from clases.sensor_temperatura import SensorTemperatura


from herramientas.herramientas import celsius_a_kelvin, fahr_a_kelvin

class Sistema:
    def __init__(self, id_sistema: int):
        self.__id_sistema = id_sistema
        self.__dicc_sensores_temp = {}
        self.__dicc_sensores_hum = {}
        self.__dicc_sensores_mov = {}
        self.__unidad_temperatura = "K"
        self.__id_sensor_sis = 0
    
    def crear_sensor_humedad(self, id_sensor: int):
        for sensor_hum in self.__dicc_sensores_hum.values():
            if id_sensor == sensor_hum.get_id_sensor():
                return f"Ya existe un sensor con id {id_sensor}"
        self.__id_sensor_sis += 1
        self.__dicc_sensores_hum[str(self.__id_sensor_sis)] = SensorHumedad(id_sensor)
        return f"Sensor humedad {id_sensor} creado y registrado en sistema {self.__id_sistema}"
    
    def crear_sensor_movimiento(self, id_sensor: int):
        for sens_mov in self.__dicc_sensores_mov.values():
            if id_sensor == sens_mov.get_id_sensor():
                return f"Ya existe un sensor con id {id_sensor}"
        self.__id_sensor_sis += 1
        self.__dicc_sensores_mov[str(self.__id_sensor_sis)] = SensorMovimiento(id_sensor)
        return f"Sensor movimiento {id_sensor} creado y registrado en sistema {self.__id_sistema}"
    
    def crear_sensor_temperatura(self, id_sensor: int):
        for sens_temp in self.__dicc_sensores_temp.values():
            if id_sensor == sens_temp.get_id_sensor():
                return f"Ya existe un sensor con id {id_sensor}"
        self.__id_sensor_sis += 1
        self.__dicc_sensores_temp[str(self.__id_sensor_sis)] = SensorTemperatura(id_sensor)
        return f"Sensor temperatura {id_sensor} creado y registrado en sistema {self.__id_sistema}"
    
    def get_sensor(self, id_sensor):
        for sensor in self.__dicc_sensores.values():
            if id_sensor == sensor.get_id_sensor():
                return sensor
        return f"Sensor id {id_sensor} no esta registrado en le sistema id {self.__id_sistema}"
    
    def generar_num_lecturas(self, num_lect: int):
        lista_dicc = [self.__dicc_sensores_temp, self.__dicc_sensores_hum, self.__dicc_sensores_mov]
        for dicc_sensores in lista_dicc:
            for sensor in dicc_sensores.values():
                for i in range(num_lect):
                    sensor.medir_unidad()
        return f"Mediciones realizadas en sensores: {num_lect * 3}"
    
    def generar_num_lecturas_dicc(self, num_lect: int, id_sensor_sis: int):#<-----arreglar o eliminar
        if id_sensor_sis in self.__dicc_sensores.keys():
            for i in range(num_lect):
                self.__dicc_sensores[str(id_sensor_sis)].medir_unidad(self)
            return f"Mediciones realizadas en sensor {id_sensor_sis}"
        return f"Sensor {id_sensor_sis} no está registrado"
    
    def dicc_estad_temp(self):
        lista_temp = []
        suma = 0
        num_mediciones = 0
        dicc_sens_temp = self.__dicc_sensores_temp
        for sensor in dicc_sens_temp.values():
            for dicc_medicion in sensor.get_lista_mediciones():
                for unidad in dicc_medicion.keys():
                    match unidad:
                        case "K":
                            lista_temp.append(dicc_medicion[unidad])
                            suma += dicc_medicion[unidad]
                            num_mediciones += 1
                        case "C":
                            lista_temp.append(celsius_a_kelvin(dicc_medicion[unidad]))
                            suma += celsius_a_kelvin(dicc_medicion[unidad])
                            num_mediciones += 1
                        case "F":
                            lista_temp.append(fahr_a_kelvin(dicc_medicion[unidad]))
                            suma += fahr_a_kelvin(dicc_medicion[unidad])
                            num_mediciones += 1
        return {"prom": suma / num_mediciones, "max": max(lista_temp), "min": min(lista_temp)}
    
                    
    def dicc_estad_humedad(self):
        lista_hum = []
        suma = 0
        num_mediciones = 0
        dicc_sens_hum = self.__dicc_sensores_hum
        for sensor in dicc_sens_hum.values():
            for dicc_medicion in sensor.get_lista_mediciones():
                for medicion in dicc_medicion.values():
                    lista_hum.append(medicion)
                    suma += medicion
                    num_mediciones += 1
        return {"prom": suma / num_mediciones, "max": max(lista_hum), "min": min(lista_hum)}
    
    def reporte(self):
        dicc_estad_temp = self.dicc_estad_temp()
        dicc_estad_hum = self.dicc_estad_humedad()
        reporte = f"Reporte Temperatura y Humedad \n\n"
        estad_temp = f"| Promedio Temperatura: {dicc_estad_temp["prom"]} | Máximo Temperatura: {dicc_estad_temp["max"]} | Mínimo Temperatura: {dicc_estad_temp["min"]} |\n"
        estad_hum = f"| Promedio Humedad: {dicc_estad_hum["prom"]} | Máximo Humedad: {dicc_estad_hum["max"]} | Mínimo Humedad: {dicc_estad_hum["min"]} |\n"
        reporte += estad_temp + estad_hum
        return reporte
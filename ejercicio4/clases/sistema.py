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
    
    def generar_num_lecturas_sensor(self, num_lect: int, id_sensor_sis: int):
        lista_dicc = [self.__dicc_sensores_temp, self.__dicc_sensores_hum, self.__dicc_sensores_mov]
        for dicc_sensor in lista_dicc:
            if str(id_sensor_sis) in dicc_sensor.keys():
                for i in range(num_lect):
                    dicc_sensor[str(id_sensor_sis)].medir_unidad()
                return f"Mediciones realizadas en sensor {id_sensor_sis}: {num_lect}"
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
        return {"prom": suma / num_mediciones, "max": max(lista_temp), "min": min(lista_temp), "num": num_mediciones}
    
    def dicc_estad_humedad(self):
        lista_hum = []
        suma = 0
        num_mediciones = 0
        dicc_sens_hum = self.__dicc_sensores_hum
        for sensor in dicc_sens_hum.values():
            for medicion in sensor.get_lista_mediciones():
                lista_hum.append(medicion)
                suma += medicion
                num_mediciones += 1
        return {"prom": suma / num_mediciones, "max": max(lista_hum), "min": min(lista_hum), "num": num_mediciones}
    
    def dicc_estad_mov(self):
        lista_mov = []
        num_detecciones = 0
        num_mediciones = 0
        dicc_sens_mov = self.__dicc_sensores_mov
        for sensor in dicc_sens_mov.values():
            for medicion in sensor.get_lista_mediciones():
                lista_mov.append(medicion)
                num_detecciones += medicion
                num_mediciones += 1
        return {"detecc_med": num_detecciones / num_mediciones, "num_detect": num_detecciones, "num": num_mediciones}
    
    def reporte(self):
        dicc_estad_temp = self.dicc_estad_temp()
        dicc_estad_hum = self.dicc_estad_humedad()
        dicc_estad_mov = self.dicc_estad_mov()
        reporte = f"Reporte Temperatura y Humedad \n\n"
        estad_temp = f"| Promedio Temperatura: {dicc_estad_temp["prom"]} | Máximo Temperatura: {dicc_estad_temp["max"]} | Mínimo Temperatura: {dicc_estad_temp["min"]} | Número de mediciones: {dicc_estad_temp["num"]} |\n"
        estad_hum = f"| Promedio Humedad: {dicc_estad_hum["prom"]} | Máximo Humedad: {dicc_estad_hum["max"]} | Mínimo Humedad: {dicc_estad_hum["min"]} | Número de mediciones: {dicc_estad_hum["num"]} |\n"
        estad_mov = f"| Promedio movimientos por medición: {dicc_estad_mov["detecc_med"]} | Número de movimientos: {dicc_estad_mov["num_detect"]} | Número de mediciones: {dicc_estad_mov["num"]} |\n"
        reporte += estad_temp + estad_hum + estad_mov
        return reporte
from clases_menu.menu import Menu


class MenuSensor(Menu):
    def crear_sensor_hum(self):
        try:
            id_sensor = int(input("Ingrese el id del sensor: "))
            print(self.get_sistema().crear_sensor_humedad(id_sensor))
            return True
        except Exception as exception:
            print(exception)
            return True
    
    def crear_sensor_mov(self):
        try:
            id_sensor = int(input("Ingrese el id del sensor: "))
            print(self.get_sistema().crear_sensor_movimiento(id_sensor))
            return True
        except Exception as exception:
            print(exception)
            return True
        
    def crear_sensor_temp(self):
        try:
            id_sensor = int(input("Ingrese el id del sensor: "))
            print(self.get_sistema().crear_sensor_temperatura(id_sensor))
            return True
        except Exception as exception:
            print(exception)
            return True
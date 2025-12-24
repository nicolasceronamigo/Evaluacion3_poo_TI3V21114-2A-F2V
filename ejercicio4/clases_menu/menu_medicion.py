from clases_menu.menu import Menu


class MenuMedicion(Menu):
    def generar_mediciones(self):
        try:
            cantidad = int(input("Introduzca la cantidad de mediciones: "))
            print(self.get_sistema().generar_num_lecturas(cantidad))
            return True
        except Exception as exception:
            print(exception)
            return True
    
    def generar_mediciones_sensor(self):
        try:
            id_sensor_sis = int(input("Ingrese el id del sensor en el sistema: "))
            cantidad_mediciones = int(input("Ingrese la cantidad de mediciones a realizar: "))
            print(self.get_sistema().generar_num_lecturas_sensor(cantidad_mediciones, id_sensor_sis))
            return True
        except Exception as exception:
            print(exception)
            return True
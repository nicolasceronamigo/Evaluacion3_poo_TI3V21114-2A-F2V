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
from clases_menu.menu import Menu


class MenuReportes(Menu):
    def mostrar_reporte_final(self):
        print("------------------------------------------------------------------------------------------------------------")
        print(self.get_estacionamientos().reporte_final())
        input("Presione cualquier tecla para continuar")
    
    def mostrar_reporte_total(self):
        print("------------------------------------------------------------------------------------------------------------")
        print(self.get_estacionamientos().lista_cobros())
        input("Presione cualquier tecla para continuar")
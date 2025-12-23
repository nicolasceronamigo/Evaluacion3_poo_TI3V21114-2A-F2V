from clases_menu.menu import Menu


class MenuReporte(Menu):
    def reporte_final(self):
        print(self.get_tienda().reporte_final())
        input("Presione cualquier tecla para continuar")
        return True
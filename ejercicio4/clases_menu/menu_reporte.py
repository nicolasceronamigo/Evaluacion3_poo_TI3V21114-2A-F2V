from clases_menu.menu import Menu


class MenuReporte(Menu):
    def generar_reporte(self):
        print(self.get_sistema().reporte())
        input("Presione cualquier tecla para continuar")
        return True
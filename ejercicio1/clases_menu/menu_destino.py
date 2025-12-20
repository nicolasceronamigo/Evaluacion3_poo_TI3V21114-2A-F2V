from clases_menu.menu import Menu
import re

class MenuDestino(Menu):
    def opc_agregar_destinos(self):
        destino = input("Ingrese el destino: ")
        print(self.get_sistema().agregar_destino(destino))
        return self.get_sistema().agregar_destino(destino)
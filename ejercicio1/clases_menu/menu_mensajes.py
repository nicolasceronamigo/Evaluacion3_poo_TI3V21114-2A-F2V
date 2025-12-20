from clases_menu.menu import Menu

class MenuMensaje(Menu):
    def escribir_mensaje(self):
        mensaje = input("Escriba un mensaje no vacío: ")
        mensaje = self.get_sistema().enviar_mensaje_canales(mensaje)
        print("----------------------------------------------------------------------------------------")
        print(mensaje)
        print("----------------------------------------------------------------------------------------")
        self.obtener_resumen()
        print("----------------------------------------------------------------------------------------")
        return mensaje
    
    def obtener_resumen(self):
        print(self.get_sistema().obtener_resumen())
        print("----------------------------------------------------------------------------------------")
        input("Presione cualquier tecla para continuar: ")
        print("----------------------------------------------------------------------------------------")
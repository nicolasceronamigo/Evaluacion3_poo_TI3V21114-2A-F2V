from clases_menu.menu import Menu
#from clases_menu.menu_pago import MenuPago

#from main import menu_pago


class MenuVenta(Menu):
    def __init__(self, titulo, tienda):
        super().__init__(titulo, tienda)
        #self.__monto_venta = 0
    
    #def get_monto_venta(self):
    #    return self.__monto_venta
    
    def registrar_monto_venta(self):
        try:
            monto_venta = float(input("Ingrese monto de la venta: "))
            #menu_pago = MenuPago("Menu Pago", self.__tienda)
            #menu_pago.agregar_opcion(0, "Salir", menu_pago.salir)
            #menu_pago.agregar_opcion(1, "Billetera Digital", menu_pago.venta_b_digital)
            #menu_pago.agregar_opcion(2, "Tarjeta", menu_pago.venta_sin_confirmacion)
            #menu_pago.agregar_opcion(3, "Transferencia", menu_pago.venta_sin_confirmacion)
            self.get_tienda().set_monto_venta(monto_venta)
            #return menu_pago.ciclo_menu(monto_venta)
        except Exception as exception:
            print(exception)
            return f"Formato inválido de monto. El monto debe ser un número."
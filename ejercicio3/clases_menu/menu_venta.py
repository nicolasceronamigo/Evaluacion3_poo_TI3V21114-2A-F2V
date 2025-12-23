from clases_menu.menu import Menu


class MenuVenta(Menu):
    def registrar_monto_venta(self):
        try:
            monto_venta = float(input("Ingrese monto de la venta: "))
            self.get_tienda().set_monto_venta(monto_venta)
            print(f"Monto de venta {monto_venta} guardado. Seleccione el medio de pago.")
            return True
        except Exception as exception:
            print(exception)
            print(f"Formato inválido de monto. El monto debe ser un número.")
            return True
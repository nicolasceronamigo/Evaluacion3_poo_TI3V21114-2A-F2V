from clases_menu.menu import Menu


class MenuPago(Menu):
    def venta_b_digital(self):
        try:
            monto_venta = self.get_tienda().get_monto_venta()
            id_pago = int(input("Ingrese el número id del medio de pago: "))
            if str(id_pago) in self.get_tienda().get_dicc_pagos().keys():
                pago = self.get_tienda().get_dicc_pagos()[str(id_pago)]
                if type(pago).__name__ == "PagoBDigital":
                    confirmacion = input("Presione [y] para confirmar pago, presione [n] para rechazar: ")
                    print("\n")
                    if confirmacion == "y":
                        pago.confirmar()
                        self.get_tienda().set_monto_venta(0)
                        print(self.get_tienda().crear_venta(monto_venta, pago))
                        return False
                    print(f"Pago rechazado por falta de confirmación")
                    return True
                print(f"Id de pago no corresponde con el medio de pago [Billetera Digital]")
                return True
            print(f"Id de pago {id_pago} no existe")
            return True
        except Exception as exception:
            print(exception)
            print(f"Formato inválido de id. El id debe ser un número.")
            return True
    
    def venta_tarjeta(self):
        try:
            monto_venta = self.get_tienda().get_monto_venta()
            id_pago = int(input("Ingrese el número id del medio de pago: "))
            print("\n")
            if str(id_pago) in self.get_tienda().get_dicc_pagos().keys():
                pago = self.get_tienda().get_dicc_pagos()[str(id_pago)]
                if type(pago).__name__ == "PagoTarjeta":
                    self.get_tienda().set_monto_venta(0)
                    print(self.get_tienda().crear_venta(monto_venta, pago))
                    return False
                print(f"Id de pago no corresponde con el medio de pago [Tarjeta]")
                return True
            print(f"Id de pago {id_pago} no existe")
            return True
        except Exception as exception:
            print(exception)
            print(f"Formato inválido de id. El id debe ser un número.")
            return True
    
    def venta_transferencia(self):
        try:
            monto_venta = self.get_tienda().get_monto_venta()
            id_pago = int(input("Ingrese el número id del medio de pago: "))
            print("\n")
            if str(id_pago) in self.get_tienda().get_dicc_pagos().keys():
                pago = self.get_tienda().get_dicc_pagos()[str(id_pago)]
                if type(pago).__name__ == "PagoTransferencia":
                    self.get_tienda().set_monto_venta(0)
                    print(self.get_tienda().crear_venta(monto_venta, pago))
                    return False
                print(f"Id de pago no corresponde con el medio de pago [Transferencia]")
                return True
            print(f"Id de pago {id_pago} no existe")
            return True
        except Exception as exception:
            print(exception)
            print(f"Formato inválido de id. El id debe ser un número.")
            return True
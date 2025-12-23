from clases_menu.menu import Menu

#from clases.pago import Pago

#from main import dicc_pagos

class MenuPago(Menu):
    #def __init__(self, titulo, tienda):
    #    super().__init__(titulo, tienda)
    #    self.__dicc_pagos = {}
    
    #def agregar_pago(self, pago: Pago):
    #    id_pago = str(pago.get_id_pago())
    #    if id_pago in self.__dicc_pagos.keys():
    #        return f"Id pago {id_pago} ya existe"
    #    self.__dicc_pagos[id_pago] = pago
    #    return f"Pago id: {id_pago} agregado"
    
    #def selecc_opcion(self, monto_venta):
    #    num_opcion = input("Seleccione una opción digitando el número: ")
    #    if num_opcion not in self.__dicc_opciones.keys():
    #        print(f"Opcion {num_opcion} no existe. Intente nuevamente.")
    #        return self.selecc_opcion()
    #    funcion = self.__dicc_opciones[num_opcion]["func_opcion"](monto_venta)
    #    return funcion
    
    #def salir(self, monto_venta):
    #    return False
    
    #def ciclo_menu(self, monto_venta):
    #    seguir = True
    #    while seguir:
    #        print("----------------------------------------------------------------------------------------")
    #        print(self.mostrar_menu())
    #        print("----------------------------------------------------------------------------------------")
    #        seguir = self.selecc_opcion(monto_venta)
    #        print("\n")
    #        if seguir == None: #No se por qué, pero en algún momento y por alguna razón, seguir = None
    #            seguir = True
    
    def venta_b_digital(self):
        try:
            monto_venta = self.get_tienda().get_monto_venta()
            id_pago = int(input("Ingrese el número id del medio de pago: "))
            if str(id_pago) in self.get_tienda().get_dicc_pagos().keys():
                pago = self.get_tienda().get_dicc_pagos()[str(id_pago)]
                confirmacion = input("Presione [y] para confirmar pago, presione [n] para rechazar: ")
                if confirmacion == "y":
                    pago.confirmar()
                    self.get_tienda().set_monto_venta(0) #<--------------revisar si vcambia el valo de la venta a registrar
                    return self.get_tienda().crear_venta(monto_venta, pago)
                return f"Pago rechazado por falta de confirmación"
            return f"Id de pago {id_pago} no existe"
        except Exception as exception:
            print(exception)
            return f"Formato inválido de id. El id debe ser un número."
    
    def venta_sin_confirmacion(self):
        try:
            monto_venta = self.get_tienda().get_monto_venta()
            id_pago = int(input("Ingrese el número id del medio de pago: "))
            if str(id_pago) in self.get_tienda().get_dicc_pagos().keys():
                pago = self.get_tienda().get_dicc_pagos()[str(id_pago)]
                self.get_tienda().set_monto_venta(0)
                return self.get_tienda().crear_venta(monto_venta, pago)
            return f"Id de pago {id_pago} no existe"
        except Exception as exception:
            print(exception)
            return f"Formato inválido de id. El id debe ser un número."
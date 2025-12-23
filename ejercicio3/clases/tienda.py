from clases.venta import Venta
from clases.pago import Pago


class Tienda:
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__dicc_ventas = {}
        self.__dicc_pagos = {}
        self.__id_venta = 0
        self.__monto_venta = 0
    
    def get_monto_venta(self):
        return self.__monto_venta
    
    def set_monto_venta(self, monto_venta):
        self.__monto_venta = monto_venta
    
    def agregar_pago(self, pago: Pago):
        id_pago = str(pago.get_id_pago())
        if id_pago in self.__dicc_pagos.keys():
            return f"Id pago {id_pago} ya existe"
        self.__dicc_pagos[id_pago] = pago
        return f"Pago id: {id_pago} agregado"
    
    def get_dicc_pagos(self):
        return self.__dicc_pagos
    
    def crear_venta(self, monto_venta: float, pago: Pago):
        if pago.retiro_posible(monto_venta):
            self.__id_venta += 1
            id_dicc_venta = str(self.__id_venta)
            pago.retirar(monto_venta)
            venta = Venta(self.__id_venta, monto_venta, pago)
            self.__dicc_ventas[id_dicc_venta] = venta
            return self.generar_comprobante(venta)
        return f"No es posible crear la venta. No es posible realizar el retiro de {monto_venta} de medio de pago: {pago.get_id_pago()}"
    
    def generar_comprobante(self, venta: Venta):
        comprobante = f"Comprobante venta: {venta.get_id_venta()}, con {venta.get_medio_pago()}, en tienda {self.__nombre}\n"
        total_venta = f"Total: {self.__dicc_ventas[str(venta.get_id_venta())].get_monto_venta()}\n"
        return comprobante + total_venta
    
    def lista_comprobantes(self):
        lista_comprobantes = f"Lista de todos los comprobantes \n"
        for id_venta in self.__dicc_ventas.keys():
            venta = self.__dicc_ventas[id_venta]
            lista_comprobantes += self.generar_comprobante(venta) + "\n"
        return lista_comprobantes

    def calc_total(self):
        total = 0
        for id_venta in self.__dicc_ventas.keys():
            total += self.__dicc_ventas[id_venta].get_monto_venta()
        return total
    
    def calc_total_recargos(self):
        recargos = 0
        for id_venta in self.__dicc_ventas.keys():
            recargos += self.__dicc_ventas[id_venta].get_monto_recargo()
        return round(recargos)
    
    def reporte_final(self):
        reporte = f"Reporte final tienda {self.__nombre} \n"
        total_recaudado = f"Total recaudado: {self.calc_total()} \n"
        total_recargos = f"Total recargos: {self.calc_total_recargos()} \n\n"
        lista_comprobantes = self.lista_comprobantes()
        reporte += total_recaudado + total_recargos + lista_comprobantes
        return reporte
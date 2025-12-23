from clases.pago import Pago


class Venta:
    def __init__(self, id_venta: int, monto_venta: float, pago: Pago):
        self.__id_venta = id_venta
        self.__monto_venta = monto_venta
        self.__monto_recargo = pago.calc_recargo(monto_venta)
        self.__medio_pago = type(pago).__name__
    
    def get_id_venta(self):
        return self.__id_venta
    
    def get_monto_venta(self):
        return self.__monto_venta
    
    def get_monto_recargo(self):
        return self.__monto_recargo
    
    def get_medio_pago(self):
        return self.__medio_pago
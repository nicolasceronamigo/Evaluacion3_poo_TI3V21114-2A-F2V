from abc import ABC, abstractmethod


class Pago(ABC):
    def __init__(self, id_pago: int, num_cuenta: int, saldo: float):
        self.__id_pago = id_pago
        self.__num_cuenta = num_cuenta
        self.__saldo = saldo
    
    def get_id_pago(self):
        return self.__id_pago
    
    def get_num_cuenta(self):
        return self.__num_cuenta
        
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, monto):
        self.__saldo = monto
    
    def depositar(self, monto):
        if monto <= 0:
            return f"Monto a depositar debe ser positivo"
        self.set_saldo(self.get_saldo() + monto)
        return f"Monto {monto} depositado en cuenta {self.get_num_cuenta()}"
    
    @abstractmethod
    def calc_recargo(self, monto_venta):
        pass
    
    @abstractmethod
    def retiro_posible(self, monto):
        pass
    
    @abstractmethod
    def retirar(self, monto):
        pass
    
    @abstractmethod
    def confirmar(self):
        pass
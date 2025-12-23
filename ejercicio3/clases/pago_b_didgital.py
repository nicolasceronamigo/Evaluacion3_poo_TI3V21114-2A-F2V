from clases.pago import Pago

recargo_fijo = 100

class PagoBDigital(Pago):
    def __init__(self, id_pago: int, num_cuenta: int, saldo: float):
        super().__init__(id_pago, num_cuenta, saldo)
        self.__confirmacion = False
    
    def calc_recargo(self, monto):
        return recargo_fijo
    
    def confirmar(self):
        self.__confirmacion = True
    
    def retiro_posible(self, monto):
        saldo_final = self.get_saldo() - monto - recargo_fijo
        if not self.__confirmacion:
            return False
        if monto <= 0:
            return False
        if saldo_final < 0:
            return False
        return True
    
    def retirar(self, monto):
        if self.retiro_posible(monto):
            saldo_final = self.get_saldo() - monto - recargo_fijo
            self.set_saldo(saldo_final)
            return f"Monto {monto} retirado de cuenta {self.get_num_cuenta()}"
        return f"No es posible realizar el retiro de {monto}"
    
    def retirar(self, monto: float):
        saldo_final = self.get_saldo() - monto - recargo_fijo
        if monto <= 0:
            return f"Monto a retirar debe ser positivo"
        if saldo_final < 0:
            return f"Saldo insuficiente para retirar {monto} de cuenta {self.get_num_cuenta()}"
        elif self.__confirmacion:
            self.set_saldo(saldo_final)
            self.__confirmacion = False
            return f"Monto {monto} retirado de cuenta {self.get_num_cuenta()}"
            
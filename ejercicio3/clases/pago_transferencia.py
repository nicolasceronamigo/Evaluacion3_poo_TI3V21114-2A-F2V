from clases.pago import Pago


recargo_fijo = 300

class PagoTransferencia(Pago):
    def calc_recargo(self, monto_venta):
        return recargo_fijo
    
    def retiro_posible(self, monto):
        saldo_final = self.get_saldo() - monto - recargo_fijo
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
    
    def confirmar(self):
        pass
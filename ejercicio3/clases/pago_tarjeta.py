from clases.pago import Pago


recargo_porcentual = 0.05
cupo = 5000

class PagoTarjeta(Pago):
    def calc_recargo(self, monto_venta):
        recargo = monto_venta * recargo_porcentual
        return recargo
    
    def retiro_posible(self, monto):
        saldo_final = self.get_saldo() - monto * (1 + recargo_porcentual)
        if monto <= 0:
            return False
        if saldo_final < - cupo:
            return False
        return True
    
    def retirar(self, monto):
        if self.retiro_posible(monto):
            saldo_final = self.get_saldo() - monto * (1 + recargo_porcentual)
            self.set_saldo(saldo_final)
            return f"Monto {monto} retirado de cuenta {self.get_num_cuenta()}"
        return f"No es posible realizar el retiro de {monto}"
    
    def confirmar(self):
        pass
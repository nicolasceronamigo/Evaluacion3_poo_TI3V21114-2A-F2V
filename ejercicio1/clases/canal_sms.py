from clases.canal_notificacion import CanalNotificacion


costo_fijo = 100
largo_maximo = 100
patron_telefono = r"^\+?(56)?\s?(9\d{8}|[2-8]\d{7})$"

class CanalSMS(CanalNotificacion):
    def largo_maximo(self):
        return largo_maximo
    
    def verificar_destino(self, destino: str):
        return self.string_patron(destino, patron_telefono)
    
    def calcular_costo(self, mensaje: str):
        return costo_fijo
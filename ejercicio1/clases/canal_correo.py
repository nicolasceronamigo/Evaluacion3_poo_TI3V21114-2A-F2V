from clases.canal_notificacion import CanalNotificacion


cargo_caracter = 10
cargo_fijo = 1000
largo_maximo = 500
patron_correo = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

class CanalCorreo(CanalNotificacion):
    def largo_maximo(self):
        return largo_maximo
    
    def verificar_destino(self, destino: str):
        return self.string_patron(destino, patron_correo)
    
    def calcular_costo(self, mensaje):
        return cargo_fijo + cargo_caracter * len(mensaje)
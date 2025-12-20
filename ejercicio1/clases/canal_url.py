from clases.canal_notificacion import CanalNotificacion


costo_caracter = 15
largo_maximo = 200
patron_url = r"https?://\S+|www\.\S+" 

class CanalURL(CanalNotificacion):
    def largo_maximo(self):
        return largo_maximo
    
    def verificar_destino(self, destino: str):
        return self.string_patron(destino, patron_url)
    
    def calcular_costo(self, mensaje):
        return costo_caracter * len(mensaje)
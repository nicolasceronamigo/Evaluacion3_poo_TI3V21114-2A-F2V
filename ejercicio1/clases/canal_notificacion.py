from abc import ABC, abstractmethod
import re


class CanalNotificacion(ABC):
    def __init__(self):
        self.__dicc_destino_mensaje = {}
    
    def get_dicc_destino_mensaje(self):
        return self.__dicc_destino_mensaje
    
    def agregar_destino(self, destino: str):
        if destino in self.get_dicc_destino_mensaje().keys():
            return f"Destino {destino} ya existe."
        self.get_dicc_destino_mensaje()[destino] = None
        return f"Destino {destino} agregado."
    
    def string_patron(self, string: str, patron: str) -> bool:
        '''Devuelva True si el string coincide con el patrón.\n
        Si no, devuelve False'''
        string_valido = re.match(patron, string)
        if string_valido:
            return True
        return False
    
    def mensaje_valido(self, mensaje: str):
        patron_valido = r"\S"
        if len(mensaje) <= self.largo_maximo() and self.string_patron(mensaje, patron_valido):
            return True
        return False
    
    def enviar_mensaje(self, mensaje: str):
        resultado = f"\n Mensaje: [{mensaje}] \n"
        if self.mensaje_valido(mensaje):
            for key_destino in self.__dicc_destino_mensaje.keys():
                self.__dicc_destino_mensaje[key_destino] = mensaje
                resultado += f"enviado por {key_destino} \n"
        else:
            for key_destino in self.__dicc_destino_mensaje.keys():
                self.__dicc_destino_mensaje[key_destino] = None
                resultado += f"no enviado por {key_destino} \n"
        return resultado
    
    def dicc_resumen(self) -> dict:
        dicc_resultado = {"exitos": 0, "fallos": 0, "costo": 0}
        for mensaje in self.__dicc_destino_mensaje.values():
            if mensaje:
                dicc_resultado["exitos"] += 1
                dicc_resultado["costo"] += self.calcular_costo(mensaje)
            else:
                dicc_resultado["fallos"] += 1
        return dicc_resultado
    
    @abstractmethod
    def largo_maximo(self):
        pass
    
    @abstractmethod
    def verificar_destino(self, destino: str):
        pass
    
    @abstractmethod
    def calcular_costo(self, mensaje: str):
        pass
    

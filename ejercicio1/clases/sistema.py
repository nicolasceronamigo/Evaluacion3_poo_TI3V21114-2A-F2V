from clases.canal_notificacion import CanalNotificacion
from clases.canal_correo import CanalCorreo
from clases.canal_sms import CanalSMS
from clases.canal_url import CanalURL


class Sistema:
    def __init__(self):
        self.__dicc_canales = {"correo": CanalCorreo(), "sms": CanalSMS(), "url": CanalURL()}
    
    def agregar_destino(self, destino: str):
        for canal in self.__dicc_canales.values():
            if canal.verificar_destino(destino):
                return canal.agregar_destino(destino)
        return f"Destino {destino} no tiene un formato válido."
    
    def enviar_mensaje_canales(self, mensaje):
        resultado = ""
        for canal in self.__dicc_canales.values():
            resultado += canal.enviar_mensaje(mensaje)
        return resultado
    
    def obtener_resumen(self):
        resumen = f"Resumen envíos: \n \n"
        resultado = {"exitos": 0, "fallos": 0, "costo": 0}
        for canal in self.__dicc_canales.values():
            resumen_canal = canal.dicc_resumen()
            for key in resultado.keys():
                resultado[key] += resumen_canal[key]
        resumen += f"| N° envíos exitosos: {resultado["exitos"]} | N° envíos fallidos: {resultado["fallos"]} | Costo total envío: {resultado["costo"]} |"
        return resumen
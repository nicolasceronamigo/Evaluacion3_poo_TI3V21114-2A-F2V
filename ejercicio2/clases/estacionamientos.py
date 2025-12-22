from clases.estadia import Estadia
from clases.vehiculo import Vehiculo
from clases.auto import Auto
from clases.camion import Camion
from clases.moto import Moto
from herramientas.herramientas import interseccion_intervalos
import datetime


class Estacionamientos:
    def __init__(self):
        self.__dicc_estadias = {}
    
    def crear_vehiculo(self, patente: str, tipo: str):
        if tipo == "auto":
            return Auto(patente)
        elif tipo == "camion":
            return Camion(patente)
        elif tipo == "moto":
            return Moto(patente)
        return f"Tipo {tipo} no se reconoce en el sistema."
    
    def crear_estadia(self, vehiculo: Vehiculo, hora_entrada: datetime, hora_salida: datetime):
        if vehiculo.get_patente() in self.__dicc_estadias.keys():
            estadia_patente = self.__dicc_estadias[vehiculo.get_patente()]
            h_entrada = estadia_patente.get_hora_entrada()
            h_salida = estadia_patente.get_hora_salida()
            if interseccion_intervalos(hora_entrada, hora_salida, h_entrada, h_salida):
                return f"Vehiculo {vehiculo.get_patente()} no puede estar en dos estadias al mismo tiempo"
        estadia = Estadia(vehiculo, hora_entrada, hora_salida)
        patente = estadia.get_patente()
        self.__dicc_estadias[patente] = estadia
        return f"Estadia vehiculo patente {patente} agregada"
    
    def total_recaudado(self):
        total = 0
        for patente in self.__dicc_estadias.keys():
            estadia = self.__dicc_estadias[patente]
            total += estadia.calc_cobro()
        return total
    
    def dicc_top_cobros(self):
        lista_cobros = []
        for patente in self.__dicc_estadias.keys():
            cobro_patente = self.__dicc_estadias[patente].calc_cobro()
            lista_cobros.append(cobro_patente)
        lista_cobros.sort(reverse = True)
        dicc_top_cobros= {}
        for cobro in lista_cobros:
            for patente in self.__dicc_estadias.keys():
                cobro_patente = self.__dicc_estadias[patente].calc_cobro()
                if cobro_patente == cobro:
                    dicc_top_cobros[patente] = cobro_patente
        return dicc_top_cobros
    
    def dicc_top_num(self, dicc: dict, num: int):
        dicc_top_num = {}
        posicion = 1
        for key in dicc.keys():
            dicc_top_num[str(posicion)] = {key: dicc[key]}
            posicion += 1
            if posicion > num:
                break
        return dicc_top_num
    
    def dicc_cant_tipos(self):
        dicc_cant_tipos = {}
        for patente in self.__dicc_estadias.keys():
            tipo = self.__dicc_estadias[patente].get_tipo()
            if tipo in dicc_cant_tipos.keys():
                dicc_cant_tipos[tipo] += 1
            else:
                dicc_cant_tipos[tipo] = 1
        return dicc_cant_tipos
    
    def lista_cobros(self):
        lista_cobros = f"Lista de cobros de todos los vehículos \n\n"
        for patente in self.__dicc_estadias.keys():
            estadia = self.__dicc_estadias[patente]
            lista_cobros += f"| Patente: {patente} | Tiempo: {estadia.calc_horas()} hora/s | Cobro: {estadia.calc_cobro()} | \n"
        return lista_cobros
        
    def reporte_final(self):
        reporte = f"Reporte final \n\n"
        total = f"Total recaudado: {self.total_recaudado()} \n\n"
        dicc_top_cobros = self.dicc_top_cobros()
        dicc_top_3 = self.dicc_top_num(dicc_top_cobros, 3)
        top_3 = f"Top 3 patentes en cobros: \n"
        for posicion in dicc_top_3.keys():
            dicc_estadia = dicc_top_3[posicion]
            for patente in dicc_estadia.keys():
                top_3 += f"| Posición: {posicion} | Patente: {patente} | Cobro: {dicc_estadia[patente]} | \n"
        cant_tipo = f"\n Cantidad de vehiculos por tipo \n"
        dicc_cant_tipo = self.dicc_cant_tipos()
        for tipo in dicc_cant_tipo.keys():
            cant_tipo += f"| Tipo: {tipo} | Cantidad: {dicc_cant_tipo[tipo]} | \n"
        reporte += total + top_3 + cant_tipo
        return reporte
        
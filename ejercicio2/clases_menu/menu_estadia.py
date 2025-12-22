from clases_menu.menu import Menu

from clases.auto import Auto
from clases.camion import Camion
from clases.moto import Moto

from clases.estadia import Estadia

import datetime

formato_hora = "%m/%d/%y %H:%M:%S"

fecha_actual = datetime.datetime.now().strftime("%x")

class MenuEstadia(Menu):
    def crear_estadia_auto(self):
        patente = input("Ingrese la patente del auto: ")
        auto = Auto(patente)
        try:
            string_h_entrada = input("Ingrese la hora de entrada en formato HH:MM:SS : ")
            string_h_salida = input("Ingrese la hora de salida en formato HH:MM:SS : ")
            h_entrada = datetime.datetime.strptime(fecha_actual + " " + string_h_entrada, formato_hora)
            h_salida = datetime.datetime.strptime(fecha_actual + " " + string_h_salida, formato_hora)
            return self.get_estacionamientos().crear_estadia(auto, h_entrada, h_salida)
        except Exception as exception:
            print("Formato incorrecto de hora, intente nuevamente")
            print(exception)
            return self.crear_estadia_auto()
    
    def crear_estadia_camion(self):
        patente = input("Ingrese la patente del camion: ")
        camion = Camion(patente)
        try:
            string_h_entrada = input("Ingrese la hora de entrada en formato HH:MM:SS : ")
            string_h_salida = input("Ingrese la hora de salida en formato HH:MM:SS : ")
            print(string_h_entrada)
            print(string_h_salida)
            h_entrada = datetime.datetime.strptime(fecha_actual + " " + string_h_entrada, formato_hora)
            h_salida = datetime.datetime.strptime(fecha_actual + " " + string_h_salida, formato_hora)
            return self.get_estacionamientos().crear_estadia(camion, h_entrada, h_salida)
        except Exception as exception:
            print("Formato incorrecto de hora, intente nuevamente")
            print(exception)
            return self.crear_estadia_camion()
    
    def crear_estadia_moto(self):
        patente = input("Ingrese la patente del moto: ")
        moto = Moto(patente)
        try:
            string_h_entrada = input("Ingrese la hora de entrada en formato HH:MM:SS : ")
            string_h_salida = input("Ingrese la hora de salida en formato HH:MM:SS : ")
            print(string_h_entrada)
            print(string_h_salida)
            h_entrada = datetime.datetime.strptime(fecha_actual + " " + string_h_entrada, formato_hora)
            h_salida = datetime.datetime.strptime(fecha_actual + " " + string_h_salida, formato_hora)
            return self.get_estacionamientos().crear_estadia(moto, h_entrada, h_salida)
        except Exception as exception:
            print("Formato incorrecto de hora, intente nuevamente")
            print(exception)
            return self.crear_estadia_moto()


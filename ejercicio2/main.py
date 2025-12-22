from clases.estacionamientos import Estacionamientos

from clases.auto import Auto
from clases.camion import Camion
from clases.moto import Moto

from clases_menu.menu import Menu
from clases_menu.menu_estadia import MenuEstadia
from clases_menu.menu_reportes import MenuReportes

import datetime

# Prueba

estacionamientos1 = Estacionamientos()

auto1 = Auto("patente_auto1")
h_entrada_auto1 = datetime.datetime(2025, 12, 21, 1, 1, 1)
h_salida_auto1 = datetime.datetime(2025, 12, 21, 11, 21, 31)

auto2 = Auto("patente_auto2")
h_entrada_auto2 = datetime.datetime(2025, 12, 21, 2, 2, 2)
h_salida_auto2 = datetime.datetime(2025, 12, 21, 12, 22, 32)

auto3 = Auto("patente_auto3")
h_entrada_auto3 = datetime.datetime(2025, 12, 21, 3, 3, 3)
h_salida_auto3 = datetime.datetime(2025, 12, 21, 13, 23, 33)

auto4 = Auto("patente_auto4")
h_entrada_auto4 = datetime.datetime(2025, 12, 21, 4, 4, 4)
h_salida_auto4 = datetime.datetime(2025, 12, 21, 14, 24, 34)

moto1 = Moto("patente_moto1")
h_entrada_moto1 = datetime.datetime(2025, 12, 21, 5, 5, 5)
h_salida_moto1 = datetime.datetime(2025, 12, 21, 15, 25, 35)

moto2 = Moto("patente_moto2")
h_entrada_moto2 = datetime.datetime(2025, 12, 21, 6, 6, 6)
h_salida_moto2 = datetime.datetime(2025, 12, 21, 16, 26, 36)

moto3 = Moto("patente_moto3")
h_entrada_moto3 = datetime.datetime(2025, 12, 21, 7, 7, 7)
h_salida_moto3 = datetime.datetime(2025, 12, 21, 17, 27, 37)

moto4 = Moto("patente_moto4")
h_entrada_moto4 = datetime.datetime(2025, 12, 21, 8, 8, 8)
h_salida_moto4 = datetime.datetime(2025, 12, 21, 18, 28, 38)

camion1 = Camion("patente_camion1")
h_entrada_camion1 = datetime.datetime(2025, 12, 21, 9, 9, 9)
h_salida_camion1 = datetime.datetime(2025, 12, 21, 19, 29, 39)

camion2 = Camion("patente_camion2")
h_entrada_camion2 = datetime.datetime(2025, 12, 21, 10, 10, 10)
h_salida_camion2 = datetime.datetime(2025, 12, 21, 20, 30, 40)

camion3 = Camion("patente_camion3")
h_entrada_camion3 = datetime.datetime(2025, 12, 21, 11, 11, 11)
h_salida_camion3 = datetime.datetime(2025, 12, 21, 21, 31, 41)

camion4 = Camion("patente_camion4")
h_entrada_camion4 = datetime.datetime(2025, 12, 21, 12, 12, 12)
h_salida_camion4 = datetime.datetime(2025, 12, 21, 22, 32, 42)

print("------------------------------------------------------------------------------------------------------------")

print(estacionamientos1.crear_estadia(auto1, h_entrada_auto1, h_salida_auto1))
print(estacionamientos1.crear_estadia(auto2, h_entrada_auto2, h_salida_auto2))
print(estacionamientos1.crear_estadia(auto3, h_entrada_auto3, h_salida_auto3))
print(estacionamientos1.crear_estadia(auto4, h_entrada_auto4, h_salida_auto4))

print("------------------------------------------------------------------------------------------------------------")

print(estacionamientos1.crear_estadia(moto1, h_entrada_moto1, h_salida_moto1))
print(estacionamientos1.crear_estadia(moto2, h_entrada_moto2, h_salida_moto2))
print(estacionamientos1.crear_estadia(moto3, h_entrada_moto3, h_salida_moto3))
print(estacionamientos1.crear_estadia(moto4, h_entrada_moto4, h_salida_moto4))

print("------------------------------------------------------------------------------------------------------------")

print(estacionamientos1.crear_estadia(camion1, h_entrada_camion1, h_salida_camion1))
print(estacionamientos1.crear_estadia(camion2, h_entrada_camion2, h_salida_camion2))
print(estacionamientos1.crear_estadia(camion3, h_entrada_camion3, h_salida_camion3))
print(estacionamientos1.crear_estadia(camion4, h_entrada_camion4, h_salida_camion4))

print("------------------------------------------------------------------------------------------------------------")

print(estacionamientos1.lista_cobros())

print("------------------------------------------------------------------------------------------------------------")

print(estacionamientos1.reporte_final())

print("------------------------------------------------------------------------------------------------------------")


#Interacción con el usuario

estacionamientos2 = Estacionamientos()

menu_principal = Menu("Menú principal", estacionamientos2)
menu_estadia = MenuEstadia("Estacionar", estacionamientos2)
menu_reportes = MenuReportes("Rsportes", estacionamientos2)

menu_principal.agregar_opcion(0, "Salir", menu_principal.salir)
menu_principal.agregar_opcion(1, "Estacionar", menu_estadia.ciclo_menu)
menu_principal.agregar_opcion(2, "Obtener reportes", menu_reportes.ciclo_menu)

menu_estadia.agregar_opcion(0, "Salir", menu_estadia.salir)
menu_estadia.agregar_opcion(1, "Auto", menu_estadia.crear_estadia_auto)
menu_estadia.agregar_opcion(2, "Camion", menu_estadia.crear_estadia_camion)
menu_estadia.agregar_opcion(3, "Moto", menu_estadia.crear_estadia_moto)

menu_reportes.agregar_opcion(0, "Salir", menu_reportes.salir)
menu_reportes.agregar_opcion(1, "Reporte final", menu_reportes.mostrar_reporte_final)
menu_reportes.agregar_opcion(2, "Reporte total", menu_reportes.mostrar_reporte_total)


menu_principal.ciclo_menu()
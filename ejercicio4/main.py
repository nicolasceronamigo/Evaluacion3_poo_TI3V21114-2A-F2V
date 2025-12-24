from clases.sistema import Sistema

from clases_menu.menu import Menu
from clases_menu.menu_reporte import MenuReporte
from clases_menu.menu_medicion import MenuMedicion
from clases_menu.menu_sensor import MenuSensor

#Prueba

sistema1 = Sistema(1)

print(sistema1.crear_sensor_humedad(1))
print(sistema1.crear_sensor_humedad(2))

print(sistema1.crear_sensor_movimiento(3))
print(sistema1.crear_sensor_movimiento(4))

print(sistema1.crear_sensor_temperatura(5))
print(sistema1.crear_sensor_temperatura(6))

print(sistema1.generar_num_lecturas(10))

print(sistema1.reporte())

#Interacción con el usuario

menu_principal = Menu("Menú principal", sistema1)
menu_reporte = MenuReporte("Menú reporte", sistema1)
menu_medicion = MenuMedicion("Menú medición", sistema1)
menu_sensor = MenuSensor("Menú sensores", sistema1)


menu_principal.agregar_opcion(0, "Salir", menu_principal.salir)
menu_principal.agregar_opcion(1, "Menú reporte", menu_reporte.ciclo_menu)
menu_principal.agregar_opcion(2, "Menú mediciones", menu_medicion.ciclo_menu)
menu_principal.agregar_opcion(3, "Menu sensores", menu_sensor.ciclo_menu)

menu_reporte.agregar_opcion(0, "Salir", menu_reporte.salir)
menu_reporte.agregar_opcion(1, "Generar reporte", menu_reporte.generar_reporte)

menu_medicion.agregar_opcion(0, "Salir", menu_medicion.salir)
menu_medicion.agregar_opcion(1, "Generar mediciones", menu_medicion.generar_mediciones)
menu_medicion.agregar_opcion(2, "Generar medición en sensor", menu_medicion.generar_mediciones_sensor)

menu_sensor.agregar_opcion(0, "Salir", menu_sensor.salir)
menu_sensor.agregar_opcion(1, "Crear sensor humedad", menu_sensor.crear_sensor_hum)
menu_sensor.agregar_opcion(2, "Crear sensor movimiento", menu_sensor.crear_sensor_mov)
menu_sensor.agregar_opcion(3, "Crear sensor temperatura", menu_sensor.crear_sensor_temp)


menu_principal.ciclo_menu()
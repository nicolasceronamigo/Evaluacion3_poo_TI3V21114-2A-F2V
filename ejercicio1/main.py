from clases.canal_correo import CanalCorreo
from clases.canal_sms import CanalSMS
from clases.sistema import Sistema
from clases_menu.menu import Menu
from clases_menu.menu_destino import MenuDestino
from clases_menu.menu_mensajes import MenuMensaje


#Ejecución de prueba
sistema1 = Sistema()

correo1 = "correo1@email.com"
correo2 = "correo2@email.com"

url1 = "https://www.url1.com"
url2 = "www.url2.com"

telefono1 = "+56912345678"
telefono2 = "987654321"

mensaje1 = "        "
mensaje2 = "string_mensaje2_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
mensaje3 = "string mensaje 3"

lista_destinos = [correo1, correo2, url1, url2, telefono1, telefono2]

print("----------------------------------------------------------------------------------------")

for destino in lista_destinos:
    print(sistema1.agregar_destino(destino))

print("----------------------------------------------------------------------------------------")

print(sistema1.enviar_mensaje_canales(mensaje1))
print(sistema1.obtener_resumen())

print("----------------------------------------------------------------------------------------")

print(sistema1.enviar_mensaje_canales(mensaje2))
print(sistema1.obtener_resumen())

print("----------------------------------------------------------------------------------------")

print(sistema1.enviar_mensaje_canales(mensaje3))
print(sistema1.obtener_resumen())

print("----------------------------------------------------------------------------------------")

#--------------------------------------------------------------------------------------------------------------------#

#Interacción con el usuario

sistema2 = Sistema()

menu_principal = Menu("Menú principal", sistema2)
menu_destinos = MenuDestino("Administrar destinos", sistema2)
menu_mensajes = MenuMensaje("Enviar mensaje", sistema2)

menu_principal.agregar_opcion(0, "Salir", menu_principal.salir)
menu_principal.agregar_opcion(1, "Administrar destinos", menu_destinos.ciclo_menu)
menu_principal.agregar_opcion(2, "Enviar mensaje", menu_mensajes.ciclo_menu)
menu_principal.agregar_opcion(3, "Obtener resumen del último mensaje enviado", menu_mensajes.obtener_resumen)

menu_destinos.agregar_opcion(0, "Atrás", menu_destinos.salir)
menu_destinos.agregar_opcion(1, "Agregar correo, teléfono o url: ", menu_destinos.opc_agregar_destinos)

menu_mensajes.agregar_opcion(0, "Atrás", menu_mensajes.salir)
menu_mensajes.agregar_opcion(1, "Todos los destinos", menu_mensajes.escribir_mensaje)


menu_principal.ciclo_menu()
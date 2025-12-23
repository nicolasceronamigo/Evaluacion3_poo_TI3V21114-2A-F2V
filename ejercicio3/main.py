from clases.pago_b_didgital import PagoBDigital
from clases.pago_tarjeta import PagoTarjeta
from clases.pago_transferencia import PagoTransferencia

from clases.tienda import Tienda

from clases_menu.menu import Menu
from clases_menu.menu_venta import MenuVenta
from clases_menu.menu_pago import MenuPago
from clases_menu.menu_reporte import MenuReporte


#Prueba

pago_b_dig1 = PagoBDigital(1, 1, 100000)
pago_b_dig2 = PagoBDigital(2, 2, 200000)

pago_tarj1 = PagoTarjeta(3, 1, 300000)
pago_tarj2 = PagoTarjeta(4, 2, 400000)

pago_trans1 = PagoTransferencia(5, 1, 500000)
pago_trans2 = PagoTransferencia(6, 2, 600000)

tienda1 = Tienda("nombre_tienda1")

print("-----------------------------------------------------------------------------------------------------\n")

pago_b_dig1.confirmar()
print(tienda1.crear_venta(10000, pago_b_dig1))
pago_b_dig2.confirmar()
print(tienda1.crear_venta(20000, pago_b_dig2))

print("-----------------------------------------------------------------------------------------------------\n")

print(tienda1.crear_venta(30000, pago_tarj1))
print(tienda1.crear_venta(40000, pago_tarj2))

print("-----------------------------------------------------------------------------------------------------\n")

print(tienda1.crear_venta(50000, pago_trans1))
print(tienda1.crear_venta(60000, pago_trans2))

print("-----------------------------------------------------------------------------------------------------\n")

print(tienda1.reporte_final())

print("-----------------------------------------------------------------------------------------------------\n")


#Interacción con el usuario

lista_pagos = [pago_b_dig1, pago_b_dig1, pago_tarj1, pago_tarj2, pago_trans1, pago_trans2]

#los medios de pago se deben agregar a la tienda para que puedan ser seleccionados en el menú
#los medios de pago se seleccionan según su id_pago

for pago in lista_pagos:
    tienda1.agregar_pago(pago)

menu_principal = Menu("Menú Principal", tienda1)
menu_venta = MenuVenta("Menú Venta. Introduzca el monto de la venta antes de seleccionar el medio de pago", tienda1)
menu_pago = MenuPago("Menu Pago", tienda1)
menu_reporte = MenuReporte("Menú Reporte", tienda1)

menu_principal.agregar_opcion(0, "Salir", menu_principal.salir)
menu_principal.agregar_opcion(1, "Crear Venta", menu_venta.ciclo_menu)
menu_principal.agregar_opcion(2, "Menu Reporte", menu_reporte.ciclo_menu)

menu_venta.agregar_opcion(0, "Salir", menu_venta.salir)
menu_venta.agregar_opcion(1, "Introducir monto", menu_venta.registrar_monto_venta)
menu_venta.agregar_opcion(2, "Seleccionar medio de pago", menu_pago.ciclo_menu)

menu_pago.agregar_opcion(0, "Salir", menu_pago.salir)
menu_pago.agregar_opcion(1, "Billetera Digital", menu_pago.venta_b_digital)
menu_pago.agregar_opcion(2, "Tarjeta", menu_pago.venta_sin_confirmacion)
menu_pago.agregar_opcion(3, "Transferencia", menu_pago.venta_sin_confirmacion)

menu_reporte.agregar_opcion(0, "Salir", menu_reporte.salir)
menu_reporte.agregar_opcion(1, "Reporte Final", menu_reporte.reporte_final)

menu_principal.ciclo_menu()
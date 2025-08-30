from gestion_parque.parque import *



nombre, edad, atraccion_1, atraccion_2, atraccion_3 = registrar_visita()

atracciones_permitidas = ""
total = 0
atracciones_compradas = 0

if atraccion_1 != "":
    if puede_subir(edad, atraccion_1):
        atracciones_compradas += 1
        atracciones_permitidas += (f"{atraccion_1},")
        total += calcular_precio(atraccion_1)
    else:
        print("No puedes acceder a", atraccion_1, "por restricciones de edad.")

if atraccion_2 != "":
    if puede_subir(edad, atraccion_2):
        atracciones_compradas += 1
        atracciones_permitidas += (f"{atraccion_2},")
        total += calcular_precio(atraccion_2)
    else:
        print("No puedes acceder a", atraccion_2, "por restricciones de edad.")

if atraccion_3 != "":
    if puede_subir(edad, atraccion_3):
        atracciones_compradas += 1
        atracciones_permitidas +=  (f"{atraccion_3}")
        total += calcular_precio(atraccion_3)
    else:
        print("No puedes acceder a", atraccion_3, "por restricciones de edad.")

if atracciones_compradas >= 3:
    total = total - (total *0.10)
    print ("usted ha recibido un descuento del 10 %")


mostrar_resumen(nombre, edad, total, atracciones_permitidas)

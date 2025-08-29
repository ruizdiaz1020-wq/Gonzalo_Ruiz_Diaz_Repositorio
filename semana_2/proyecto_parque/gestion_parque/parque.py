def mostrar_atraccion():
    print("atracciones disponibles")
    print("1-montaña rusa")
    print("2-casa de terror")
    print("3-carrusel")

def puede_subir(edad, atraccion):
    if atraccion == "montaña rusa":
        return edad >= 12
    elif atraccion == "casa de terror":
        return edad >= 6
    elif atraccion == "carrusel":
        return True
    else:
        return False


def calcular_precio(atraccion):
    if atraccion == "montaña rusa":
        return 1500
    elif atraccion == "casa de terror":
        return 1200
    else:
        return 800
    




def registrar_visita():
    nombre = input("ingrese su nombre")
    edad = int(input("ingrese su edad"))

    mostrar_atraccion()  
    atracciones_elegidas = ""
    atracciones_compradas = 0
    total = 0

    if puede_subir(edad,"montaña rusa"):
        respuesta = input("¿Desea subir a la Montaña Rusa? (s/n): ")
        if respuesta == "s" or respuesta == "S":
            atracciones_elegidas += "montaña rusa;"
            total = total + calcular_precio("Montaña Rusa")
            atracciones_compradas += 1
    else:
        print("No puede subir a la Montaña Rusa por su edad.")


    if puede_subir(edad, "Casa de Terror"):
        respuesta = input("¿Desea subir a la Casa de Terror? (s/n): ")
        if respuesta == "s" or respuesta == "S":
            atracciones_elegidas += "casa de terror,"
            total = total + calcular_precio("Casa de Terror")
            atracciones_compradas += 1
    else:
        print("No puede subir a la Casa de Terror por su edad.")

    
    if puede_subir(edad, "Carrusel"):
        respuesta = input("¿Desea subir a la Carrusel? (s/n): ")
        if respuesta == "s" or respuesta == "S":
            atracciones_elegidas
            total = total + calcular_precio("Carrusel")
            atracciones_compradas += 1
    else:
        print("No puede subir a la Carrusel por su edad.")
    if atracciones_compradas >= 3:
        total = total - (total * 0.10)
         
    return nombre, edad, atracciones_elegidas, total

   
def mostrar_resumen(nombre, edad, total, atracciones_elegidas):
    print("----resumen de la visita----")
    print(f"nombre:{nombre}")
    print(f"edad:{edad}")
    print(f"atracciones elegidas:{atracciones_elegidas}")
    print(f"costo total de la visita: {total}")
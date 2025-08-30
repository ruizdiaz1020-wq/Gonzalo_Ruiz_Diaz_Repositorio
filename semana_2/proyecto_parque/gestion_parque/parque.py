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

    cantidad = int(input("cuantas atracciones desea utilizar?"))

    atraccion_1 = "" 
    atraccion_2 = ""
    atraccion_3 = ""

    for i in range(1, cantidad + 1):
        atr = input(f"ingrese el nombre de su atraccion Nº {i}")
        if i == 1:
            atraccion_1 = atr
        elif i == 2:
            atraccion_2 = atr
        elif i == 3:
            atraccion_3 = atr
        else :
            print("numero de atraccion no valido")
    
    print(f"nombre: {nombre}")
    print(f"edad: {edad}")
    print(f"cantidad de atracciones elegidas; {cantidad}")
    print(f"atracciones elegidas: {atraccion_1}, {atraccion_2}, {atraccion_3}")

    return nombre, edad, atraccion_1, atraccion_2, atraccion_3


    



   
def mostrar_resumen(nombre, edad, total, atracciones_permitidas):
    print("----resumen de la visita----")
    print(f"nombre:{nombre}")
    print(f"edad:{edad}")
    print(f"atracciones elegidas:{atracciones_permitidas}")
    print(f"costo total de la visita: {total}")
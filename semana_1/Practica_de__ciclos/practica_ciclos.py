nombre = input("como te llamas?")
edad = int(input("cual es tu edad?"))
num_atracciones = int(input("cuantas atracciones quiere usar?(maximo 3)"))

print("atracciones disponibles")
print("montaña rusa, casa del terror y/o carrusel")

costo_total = 0
contador = 0 
atracciones_elegidas = ""
atracciones_permitidas = ""

while contador < num_atracciones:
    eleccion = input("que atraccion desea utilizar?")

    if eleccion == "montaña rusa":
        atracciones_elegidas += "montaña rusa,"
        contador += 1
        if edad >= 12:
            costo_total +=1500
            atracciones_permitidas += "montaña rusa"
            print("puedes usar la montaña rusa")
        else:
            print("no puedes usar la montaña rusa")
    elif eleccion == "casa del terror":
        atracciones_elegidas += "casa del terror"
        contador += 1
        if edad >= 6:
            costo_total += 1200
            atracciones_permitidas += "casa del terror"
            print("puedes usar la casa del terror")
        else:
            print("no puedes usar la casa del terror")
    elif eleccion == "carrusel":
        contador += 1
        atracciones_elegidas += "carrusel"
        atracciones_permitidas += "carrusel"
        costo_total += 800
        print("puedes usar el carrusel")
    else:
        print("atraccion no valida")

print("----resumen de entrada----")
print(f"nombre del visitante:{nombre}")
print(f"edad del visitante:{edad}")
print(f"atracciones elegidas:{atracciones_elegidas}")
print(f"atracciones permitidas:{atracciones_permitidas}")
print(f"costo total a pagar:{costo_total}")



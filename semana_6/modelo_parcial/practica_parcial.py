maximo = 10

listas_personas = [""] * maximo
listas_puntuaciones = [0] * maximo
listas_comentarios = [""] * maximo


def cargar_datos(arrayPer, arrayPun, arrayCome):
    for i in range(len(arrayPer)):
       
        while True:
            persona = input(f"ingrese nombre de la persona {i + 1}")
            if persona != "":
                arrayPer[i] = persona
                break
            else:
                print("nombre de persona no puede estar vacio")
        
        while True:
            puntuacion = int(input(f"ingrese la puntuacion de la persona{i +1}"))
            if puntuacion >= 1 and puntuacion <= 10:
                arrayPun[i] = puntuacion
                break
            else:
                print("puntuacion no valida")
            
        while True:
            comentario = input(f"ingrese comentario de la persona {i + 1}")
            if comentario != "":
                arrayCome[i] = comentario
                break
            else:
                print("comentario no puede estar vacio")
            

        opcion = input("desea agregar otro usuario?(s/n)")
        if opcion == "s":
            continue
        else:
            break



def mostrar_puntuacion_y_comentarios(arrayper,arraypun,arraycome):
    promedio = 0
    division = 0
    for i in range(len(arrayper)):
        if (arrayper[i] != "" and arraycome[i] != ""):
            print(f"usuario{i + 1}")
            print(f"nombr:{arrayper[i]}")
            print(f"puntucaione:{arraypun[i]}")
            print(f"comentario: {arraycome[i]}")
            promedio += arraypun[i]
            division += 1
        else:
            break
    
    print(f"el promedio de puntuaciones es {promedio / division }")


def ordenar(arrayper, arraypun, arraycome):

    tam_valido = 0
    for i in range(len(arrayper)):
        if arrayper[i] != "" and arraycome[i] != "":
            tam_valido += 1
        else:
            break
    
    for i in range(tam_valido - 1):
        intercambio = False
        for j in range(tam_valido - i - 1):
            if (arrayper[j] != "" and arraycome[j] != ""):
             if arraypun[j] > arraypun[j + 1]:
                    arraypun[j], arraypun[j + 1] = arraypun[j + 1], arraypun[j]
                    arrayper[j], arrayper[j + 1] = arrayper[j + 1], arrayper[j]
                    arraycome[j], arraycome[j + 1] = arraycome[j + 1], arraycome[j]
                    intercambio = True
            else:
                break
        if not intercambio:
         break
    
    for k in range((tam_valido)):
        if (arrayper[k] != "" and arraycome[k] != ""):
            print(f"usuario{k + 1}")
            print(f"nombr:{arrayper[k]}")
            print(f"puntucaione:{arraypun[k]}")
            print(f"comentario: {arraycome[k]}")
        else:
            break





#-----------------------------------------------------------
while True:
    print("----menu----")
    print("1)ingresar datos de los participantes")
    print("2)mostrar puntuaciones y comentarios")
    print("3)ordenar participantes por puntuacion(menor a mayor)")
    print("4)salir")

    opcion = int(input("que opcion desea elegir?"))

    if opcion == 1:
        cargar_datos(listas_personas,listas_puntuaciones, listas_comentarios)
    elif opcion == 2:
        mostrar_puntuacion_y_comentarios(listas_personas,listas_puntuaciones,listas_comentarios)
    elif opcion == 3:
        ordenar(listas_personas,listas_puntuaciones,listas_comentarios)
    elif opcion == 4:
        break
    else:
        print("opcion invalida")
def cargar_titulosyejemplares():
    array_1 = [""] * 20
    array_2 = [0] * 20
    for i in range(len(array_1)):
        respuesta = input("desea agregar un libro? (s/n)")
        if respuesta == "s":
            array_1[i] = input("ingrese nombre del libro: ")
            array_2[i] = int(input("ingrese el numero de ejemplares de dicho libro: "))
            
        else:
            break
    return array_1, array_2


def mostrar_catalogo(array_1, array_2):
    for i in range(len(array_1)):
        if array_1[i] != "":
            print(f"{array_1[i]} tiene {array_2[i]} ejemplares")
        else:
            continue

def consultar_disponibilidad(array_1, array_2):
    respuesta = input("que titulo quiere consultar?")
    contador = 0 
    for i in range(len(array_1)):
        if array_1[i] == respuesta:
            contador += 1
            print(f"el libro {respuesta} tiene {array_2[i]} copias")
        else:
            continue
    if contador == 0:
        print("libro invalido")


def listar_titulos_agotados(array_1, array_2):
    for i in range(len(array_1)):
        if array_1[i] != "" and array_2[i] == 0:
            print(array_1[i])

def agregar_nuevo_libro(array_1, array_2):
    contador = 0
    for i in range(len(array_1)):
        if array_1[i] == "":
            contador += 1
            array_1[i] = input("ingrese nombre del nuevo libro: ")
            array_2[i] = int(input("ingrese numero de ejemplares del mencionado: "))
            break
        else: 
            continue
    if contador == 0:
        print("ya se alcanzo el maximo de 20")
    
def actualizar_ejemplares(array_1, array_2):
    respuesta = input("de que libro desea actualizar los ejemplares?:")
    for i in range(len(array_1)):
        if respuesta == array_1[i]:
            array_2[i] = int(input("ingrese la nueva cantidad de ejemplares:"))
        else:
            continue

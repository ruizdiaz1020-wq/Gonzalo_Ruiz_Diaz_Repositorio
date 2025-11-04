def cargar(archivo):
    with open(archivo, "a") as archivo:
        while True:
            nombre = input("agrega un nombre: ")
            if nombre == "":
                break
            archivo.write(nombre + "\n")

def mostrar_sin_nombre(archivo, nombre):
    with open(archivo, "r") as archivo:
        lista_nombre = archivo.readlines()

        for i in lista_nombre:
            if i.strip().lower() != nombre.strip().lower():
                print("\t" + i)
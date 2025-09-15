
from funciones_bibloteca.funciones import *
array_libros = [""] * 20
array_ejemplares = [0] * 20
array_libros[1] = "libro x"

while True:
    print("---opciones----")
    print("(1)cargar titulos y ejemplares")
    print("(2)mostrar catalogo completo")
    print("(3)consultar disponibilidad")
    print("(4)listar titulos agotados")
    print("(5)agregar un nuevo titulo")
    print("(6)actualizar ejemplares")
    print("(7)salir")

    opcion = int(input("que opcion desea elegir?: "))

    if opcion == 1:

        array_libros, array_ejemplares = cargar_titulosyejemplares()
    elif opcion == 2:
        mostrar_catalogo(array_libros,array_ejemplares)
    elif opcion == 3:
        consultar_disponibilidad(array_libros, array_ejemplares)
    elif opcion == 4:
        listar_titulos_agotados(array_libros, array_ejemplares)
    elif opcion == 5:
        agregar_nuevo_libro(array_libros, array_ejemplares)
    elif opcion == 6:
        actualizar_ejemplares(array_libros, array_ejemplares)
    elif opcion == 7:
        break
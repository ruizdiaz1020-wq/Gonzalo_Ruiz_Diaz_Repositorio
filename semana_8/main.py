from funciones import *

#arc = open ("archivo.txt", "w" )
#arc.write("probando escritura")
#arc.close()



#with open("archivo.txt", "a") as arc:
#    arc.write("agregando algo")


archivo = "nombre_archivo.txt"

cargar(archivo)

nombre_excluido = input("escriba nombre a excluir: ")

mostrar_sin_nombre(archivo, nombre_excluido)
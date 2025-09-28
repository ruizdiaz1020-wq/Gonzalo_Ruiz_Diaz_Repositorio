##Ejercicio 1: Registro de Temperaturas
#Cargar en una matriz 7x3 las temperaturas (números enteros) y mostrar:
#    El promedio de temperatura de cada día.
#    El promedio general de toda la semana.



#FILAS = 7
#COLUMNAS = 3


#matriz = [[0.0 for _ in range(COLUMNAS)]for _ in range(FILAS)]


#def cargar_matriz(mat):
#    for i in range(FILAS):
#        for j in range(COLUMNAS):
#           
#         mat[i][j] = float(input(f"ingrese la temperatura del horario{j + 1} del dia {i + 1}:"))

#cargar_matriz(matriz)

#def promedio_dia(mat):
#   for i in range(FILAS):
#      total_dia = 0
#      for j in range(COLUMNAS):
#       
#         total_dia += mat[i][j]
#      print(f"el promedio de temperatura del dia {i} es {total_dia / COLUMNAS}")

#promedio_dia(matriz)

#def promedio_semana(mat):
#   total_semana = 0
#   for i in range(FILAS):
#      for j in range(COLUMNAS):
#     
#         total_semana += mat[i][j]
#   return print(f"el promedio de temperatura de la semana es {total_semana / (FILAS * COLUMNAS)}")


#promedio_semana(matriz)

#ejercicio 2
#filas = 4
#columnas = 5
#matriz = [[0]* columnas for _ in range(filas)]


#for i in range(filas):
#    print(f"equipo {i + 1}")
#    for j in range(columnas):
#        matriz[i][j] = int(input(f"ingrese puntaje de ronda {j + 1}:"))
#puntaje_de_cada_equipo = [0] * filas
#for i in range(filas):
#    puntaje = 0
#    for j in range (columnas):
#        puntaje += matriz[i][j]
#    puntaje_de_cada_equipo[i] = puntaje
#    print(f"puntaje del equipo {i + 1} es {puntaje}")

#puntaje_mayor = puntaje_de_cada_equipo[0]
#for i in range(filas):
#    if puntaje_de_cada_equipo[i] > puntaje_mayor:
#        puntaje_mayor = puntaje_de_cada_equipo[i]
#    else:
#        continue

#print(puntaje_mayor)
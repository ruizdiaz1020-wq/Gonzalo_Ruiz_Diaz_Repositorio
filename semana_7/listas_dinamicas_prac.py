#lista_nombres = []
#for i in range(5):
#    nuevo_nombre = input("ingrese un nombre:\n ")
#    lista_nombres.append(nuevo_nombre)
#print(lista_nombres)

#nombre_agregado = input("agrega un nombre a la segunda posicon:\n")

#lista_nombres.insert(1, nombre_agregado)

#print(lista_nombres)

#nombre_a_eliminar = input("ingresa nombre a eliminar:\n")

#contador = 0
#for i in range(len(lista_nombres)):
#    if lista_nombres[i] == nombre_a_eliminar:
#        lista_nombres.remove(lista_nombres[i])
#        contador += 1
#        break

#if contador == 0:
#    print("el nombre no esta en la lista")


#print(lista_nombres)

#if "juan" in lista_nombres:
#    print("juan esta en la lista")

#nombre_a_buscar = input("ingrese nombre a buscar:\n")
#verificador = False
#for j in range(len(lista_nombres)):
#    if lista_nombres[j] == nombre_a_buscar:
#       posicion = lista_nombres.index(nombre_a_buscar)
#       print(f"{nombre_a_buscar} se encuentra en la posicion {posicion + 1}")
#       verificador = True
#       break

#if not verificador:
#    print("el nombre no se encuentra en la lista")

lista_estudiante = ["maria","gomez", 32456]
print(lista_estudiante)
lista_notas = [2, 3, 4]

lista_estudiante.append(lista_notas)

print(lista_estudiante)

lista_estudiante[3].append(9.5)
print(lista_estudiante)

lista_estudiante_2 = ["lucas", "fernandez", 7890]

lista_estudiante.extend(lista_estudiante_2)

print(lista_estudiante)

lista_estudiante.clear()
print(lista_estudiante)
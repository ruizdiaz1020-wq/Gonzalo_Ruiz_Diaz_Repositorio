#diccionario = dict()


#diccionario["valor1"] = 2

#print(diccionario)

#while True:
#    elementonuevo = input("agrega nuevo elemento a dicc: ")

#    if elementonuevo != "":
#        diccionario[2] = elementonuevo
#        break

#print(diccionario)

lista_diccionario = [
    {"valor1": 1,
     "valor2": 2},
    {"valor3":3,
     "valor4":4}
]


elemento = lista_diccionario[0]["valor1"]

print(elemento)

clave = lista_diccionario[0].keys()
listaclaves = list(clave)
print(clave)

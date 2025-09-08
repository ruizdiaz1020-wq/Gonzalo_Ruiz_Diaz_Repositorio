def buscar_numero(array, num):
    contador_de_posicion = 0
    posicion = 0
  
    for i in range(len(array)):
        contador_de_posicion += 1
        if array[i] == num:
            posicion = contador_de_posicion
            print(f"la primera aparicion de {num} es en la posicion {posicion}")
        else:
            continue
        
    if posicion == 0:
        print("-1")
    
numero = int(input("ingrese numero"))
array = [1,2,3,4,5,6,7,8]

buscar_numero(array, numero)

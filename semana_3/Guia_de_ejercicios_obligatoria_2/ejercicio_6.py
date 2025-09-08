array = [2, 7, 4, 8, 10, 6, 5]

num_mayor = 0
posicion = 0
posicion_mayor = 0
for i in range(len(array)):
    posicion += 1
    if array[i] > num_mayor:
        num_mayor = array[i]
        posicion_mayor = posicion
    else:
        continue

print(f"el numero mayor es {num_mayor} y esta en la posicion {posicion_mayor}")
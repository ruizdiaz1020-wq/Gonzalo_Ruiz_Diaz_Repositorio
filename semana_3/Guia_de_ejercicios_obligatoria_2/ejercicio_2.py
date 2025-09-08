array = [0] * 10
suma_total = 0
for i in range(len(array)):
    array[i] = int(input("ingrese numero"))
    
    suma_total += array[i]

print(suma_total)
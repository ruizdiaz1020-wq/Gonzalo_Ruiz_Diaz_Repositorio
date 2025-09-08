array = [0.0] * 6
suma_total = 0.0

for i in range(len(array)):
    array[i] = float(input("ingrese numero: "))
    suma_total += array [i]

promedio = suma_total / len(array)

print(f"{promedio:.2f}")


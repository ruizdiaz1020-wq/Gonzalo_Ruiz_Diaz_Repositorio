array_1 = [0] * 5
array_2 = [0] * 5
contador = 0

for i in range(len(array_1)):
    array_1[i] = int(input("ingrese un numero para array_1: "))


for k in range(len(array_2)):
    array_2[k] = int(input("ingrese un numero para array_2: "))

for j in range(len(array_1)):
    if array_1[j] == array_2[j]:
        contador += 1
    else:
        continue

if contador == len(array_1):
    print("array_1 y array_2 son iguales")
else:
    print("array_1 y array_2 no son iguales")

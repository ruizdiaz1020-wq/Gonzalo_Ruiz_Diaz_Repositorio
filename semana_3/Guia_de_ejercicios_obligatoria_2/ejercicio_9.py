array = [0] * 10

for i in range(len(array)):
    array[i] = int(input("ingrese un numero: "))

for j in range(len(array)):
    if array[j] % 2 == 0:
        array[j] = 0
    else:
        continue

print(array)
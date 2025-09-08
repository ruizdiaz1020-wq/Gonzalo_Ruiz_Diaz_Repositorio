array = [4, 6, 34, 23, 65, 3, 1, 89, 12, 100]


num = int(input("ingrese un numero: "))
verificador = False
for i in range(len(array)):
    if num == array[i]:
        verificador = True
        print(f"su numero esta en el array  numero {i + 1}")
    else:
        continue

if not verificador:
    print("nu numero no esta en el array")
else:
    pass
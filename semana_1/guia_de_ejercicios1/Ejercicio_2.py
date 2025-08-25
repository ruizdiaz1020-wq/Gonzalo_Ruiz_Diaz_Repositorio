def operaciones(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    return suma, resta, multiplicacion

num1 = int(input("elija un numero"))
num2 = int(input("elija otro numero"))

print(operaciones(num1, num2))


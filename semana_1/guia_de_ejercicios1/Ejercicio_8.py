def calcular_edad(anio_nacimiento):
    edad = 2025 - anio_nacimiento
    return edad

anio_nacimiento = int(input("ingrese anio de nacimiento"))

print(calcular_edad(anio_nacimiento))

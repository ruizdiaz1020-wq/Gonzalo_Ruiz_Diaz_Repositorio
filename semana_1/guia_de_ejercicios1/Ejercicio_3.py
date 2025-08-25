def area_triangulo(base, altura):
    area = base * altura / 2
    return area

base = float(input("ingrese la base del triangulo"))
altura = float(input("ingrese la altura del triangulo"))

print(area_triangulo(base, altura))

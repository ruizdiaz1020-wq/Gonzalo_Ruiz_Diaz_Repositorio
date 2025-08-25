def buscar_mayor(a, b, c):
    if a >= b and a >= c:
        if b >= c:
            return [a, b, c]
        else:
            return [a, c, b]
    elif b >= a and b >= c:
        if a >= c:
            return [b, a, c]
        else:
            return [b, c, a]
    else: 
        if a >= b:
            return [c, a, b]
        else:
            return [c, b, a]
        
a = int(input("ingrese un numero"))
b = int(input("inrese otro numero"))
c = int(input("ingrese el numero final"))

print(buscar_mayor(a, b, c))
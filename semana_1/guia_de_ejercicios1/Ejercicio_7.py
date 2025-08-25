def verificar_acceso(edad):
    return edad >= 18

    
edad = int(input("ingrese su edad"))

if verificar_acceso(edad):
    print("eres mayor")
else:
    print("eres menor")
    

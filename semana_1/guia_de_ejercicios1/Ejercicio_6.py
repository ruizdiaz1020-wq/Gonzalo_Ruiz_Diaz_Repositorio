def convertir_minutos(minutos):
    horas = minutos // 60
    minutos_sobrantes = minutos % 60
    return horas, minutos_sobrantes

minutos = int(input("ingrese cantidad de minutos"))

print(convertir_minutos(minutos))
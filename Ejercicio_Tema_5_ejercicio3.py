"""
Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
"""

def es_bisiesto(fecha):
    if fecha % 4 == 0 and fecha % 100 != 0 or fecha % 400 == 0:
        print('Año bisiesto')
    else:
        print('Año no bisiesto')


es_bisiesto(int(input('Introduce el año: ')))
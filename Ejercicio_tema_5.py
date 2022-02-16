"""
Escribe una función que calcule el área de un triángulo,
recibiendo la altura y la base como parámetros
y otra función que calcule el área de un círculo recibiendo el radio del mismo.
"""
base = float(input('Introduzca la base: '))
altura = float(input('Introduzca la altura: '))
radio = int(input("Ingresa el valor del radio: "))
pi = 3.141592653589793238462643383279502884197

def area_triangulo(base, altura):
    area = base * altura / 2
    return area

def area_circulo(radio):
    area = (radio ** 2) * pi
    return area


area_total_circulo = area_circulo(radio)
area_total_triangulo = area_triangulo(base, altura)

print("El area del Triangulo es:", area_total_triangulo)
print("El area de circulo es:", area_total_circulo)
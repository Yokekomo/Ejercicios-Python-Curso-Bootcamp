"""
Crea un script que le pida al usuario una lista de países (separados por comas).
Éstos se deben almacenar en una lista.
No debería haber países repetidos (haz uso de set).
Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.


Por otro lado, tienes que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro
 con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.

"""
from functools import reduce

lista_paises = []

try:
    paises = input('Introduce países separados por una coma: ')
    separar = paises.split(',')
    for pais in separar:
        lista_paises.append(pais.strip())
except:
    print('Ha ocurrido un error al ingresar los países')

lista_sin_repetidos = set(lista_paises)
lista_ordenada = sorted(lista_sin_repetidos)
print(', '.join(lista_ordenada))


# --------------------------------------------------------------------------------------------------------- Partes dos


def funcion_impares(numero):
    return numero % 2 == 1


lista = [6, 7, 3, 1, 0, 4, 7, 2, 8, 9, 11, 10, 17, 12, 15]

filtrada = list(filter(funcion_impares, lista))


def funcion_sumar(numero1, numero2):
    return numero1 + numero2


print(reduce(funcion_sumar, filtrada))



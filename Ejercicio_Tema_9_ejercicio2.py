"""
En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una
lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.
"""
from functools import reduce


def funcion_impares(numero):
    return numero % 2 == 1


lista = [6, 7, 3, 1, 0, 4, 7, 2, 8, 9, 11, 10, 17, 12, 15]

filtrada = list(filter(funcion_impares, lista))


def funcion_sumar(numero1, numero2):
    return numero1 + numero2


print(reduce(funcion_sumar, filtrada))
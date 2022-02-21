"""
Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.
"""


class CrearNumeros:
    numero = 100
    lista_numeros = []

    while numero >= 0:
        lista_numeros.append(numero)
        numero -= 1

    cadena = 'La lista de números en orden inverso es:\n'
    print(f'{cadena}\n{lista_numeros}')


if __name__ == '__main__':
    CrearNumeros()

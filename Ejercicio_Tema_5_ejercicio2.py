"""
Escribe una función que pueda decirte si un número (número entero) es primo o no.
"""


def es_primo(numero):
    for num in range(2, numero):
        if numero % num == 0:
            print(f'{numero} no es primo, {num} es divisor')
            return False
    print(f'El número {numero}, es primo!!!!!')
    return True


es_primo(int(input('Introduce el número a comprobar: ')))

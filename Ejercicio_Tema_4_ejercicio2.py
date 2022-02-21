"""
Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.

Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]
"""


def imprime_en_pantalla(lista_impares):
    return f"\n{50 * '-'}\nLa lista de números impares es: \n{lista_impares}\n{50 * '-'}"


class BuscarImpares:
    print('Vamos a buscar los impares de un grupo de números que tu vas a definir')
    numero_inicio = int(input('Introduce el número inicial: '))
    numero_final = int(input('Y el número final: '))
    lista_numeros = []

    while numero_inicio != numero_final:
        lista_numeros.append(numero_inicio)
        numero_inicio += 1

    lista_numeros.append(numero_final)
    lista_impares = []

    for numero in lista_numeros:
        if numero % 2 == 1:
            lista_impares.append(numero)

    print(imprime_en_pantalla(lista_impares))


if __name__ == '__main__':
    BuscarImpares()
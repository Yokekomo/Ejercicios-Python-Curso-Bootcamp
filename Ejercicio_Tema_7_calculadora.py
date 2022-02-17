
def sumar(valor_1, valor_2):
    resultado = valor_1 + valor_2
    print(f'{valor_1} más {valor_2} es: {resultado}')


def restar(valor_1, valor_2):
    resultado = valor_1 - valor_2
    print(f'{valor_1} menos {valor_2} es: {resultado}')


def dividir(valor_1, valor_2):
    if valor_1 == 0 or valor_2 == 0:
        print('No se puede dividir por 0')
    else:
        resultado = valor_1 / valor_2
        print(f'{valor_1} entre {valor_2} es: {resultado}')


def multiplicar(valor_1, valor_2):
    resultado = valor_1 * valor_2
    print(f'{valor_1} por {valor_2} es: {resultado}')
"""
En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora:
 sumar, restar, multiplicar y dividir.

Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas.
 Los resultados tenéis que mostrarlos por consola.
"""
from Ejercicio_Tema_7_calculadora import *


class Main:

    def __init__(self):
        while True:
            try:
                valor_1 = int(input('Introduzca el primer número: '))
                valor_2 = int(input('Introduzca el segundo número: '))
                if len(str(valor_1)) > 0 and len(str(valor_2)) > 0:
                    valor_3 = input('\nQue operación desea realizar:'
                                    ' \n1.- Sumar'
                                    '\n2.- Restar'
                                    '\n3.- Multiplicar'
                                    '\n4.- Dividir'
                                    '\n5.- Salir'
                                    '\n\nIntroduzca una opción: ').upper()

                    if (valor_3 == '1') or (valor_3 == 'SUMAR'):
                        sumar(valor_1, valor_2)
                    elif (valor_3 == '2') or (valor_3 == 'RESTAR'):
                        restar(valor_1, valor_2)
                    elif (valor_3 == '3') or (valor_3 == 'MULTIPLICAR'):
                        multiplicar(valor_1, valor_2)
                    elif (valor_3 == '4') or (valor_3 == 'DIVIDIR'):
                        dividir(float(valor_1), float(valor_2))
                    elif (valor_3 == '5') or (valor_3 == 'SALIR'):
                        exit()
                    else:
                        print('\n\nDebe elegir una opción del menu')
            except:
                print('Ha ocurrido un error')


if __name__ == '__main__':
    Main()

"""
Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""
while True:
    try:
        edad = int(input('¿Que edad tiene? '))
        if (edad > 0) and (edad <= 120):
            if edad <= 17:
                print('Usted es menor de edad')
                break
            else:
                print('Usted es mayor de edad')
                break
        else:
            print('La edad tiene que estar entre 0 y 120 años')
    except:
        print('Ha ocurrido un error')

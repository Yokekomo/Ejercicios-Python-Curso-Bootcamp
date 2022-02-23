"""
Escribe un programa en la consola de python que pida al usuario su peso (en kg)
y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable,
e imprima por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice
de masa corporal calculado redondeado con dos decimales.

Tienes que subir capturas de pantalla en una carpeta comprimida zip.

"""
edad = int(input('Introduce tu edad: '))
if edad <= 0:
    print('Lo siento pero aun no has nacido')
    exit()
elif edad > 120:
    print('Tienes que estar vivo para calcular el imc')
    exit()
elif edad < 18:
    print('Solo se puede calcular la masa corporal de un adulto.')
    exit()
elif 18 <= edad <= 120:
    pass

genero = input('Introduce tu genero: (Hombre, Mujer) ').upper()
altura = float(input('Su altura en metros por favor: '))
peso = float(input('Su peso en kilogramos por favor: '))
frase_1 = 'Tu índice de masa corporal es '
frase_2 = ': '
imc_1 = 'Delgadez severa'
imc_2 = 'Delgadez moderada'
imc_3 = 'Delgadez leve'
imc_4 = 'Normal'
imc_5 = 'Sobrepeso'
imc_6 = 'Obesidad leve'
imc_7 = 'Obesidad media'
imc_8 = 'Obesidad morbida'

imc_redondeado = round((peso / altura ** 2), 2)

if genero == 'HOMBRE' or genero == 'H':

    if 0 <= imc_redondeado <= 15.99:
        print(frase_1 + imc_1 + frase_2 + str(imc_redondeado))
    elif 16.00 <= imc_redondeado <= 16.99:
        print(frase_1 + imc_2 + frase_2 + str(imc_redondeado))
    elif 17.00 <= imc_redondeado <= 18.49:
        print(frase_1 + imc_3 + frase_2 + str(imc_redondeado))
    elif 18.50 <= imc_redondeado <= 24.99:
        print(frase_1 + imc_4 + frase_2 + str(imc_redondeado))
    elif 25.00 <= imc_redondeado <= 29.99:
        print(frase_1 + imc_5 + frase_2 + str(imc_redondeado))
    elif 30.00 <= imc_redondeado <= 34.99:
        print(frase_1 + imc_6 + frase_2 + str(imc_redondeado))
    elif 35.00 <= imc_redondeado <= 39.00:
        print(frase_1 + imc_7 + frase_2 + str(imc_redondeado))
    elif imc_redondeado >= 40.00:
        print(frase_1 + imc_8 + frase_2 + str(imc_redondeado))

elif genero == 'MUJER' or genero == 'M':

    if 0 <= imc_redondeado <= 12.99:
        print(frase_1 + imc_1 + frase_2 + str(imc_redondeado))
    elif 13.00 <= imc_redondeado <= 13.99:
        print(frase_1 + imc_2 + frase_2 + str(imc_redondeado))
    elif 14.00 <= imc_redondeado <= 15.49:
        print(frase_1 + imc_3 + frase_2 + str(imc_redondeado))
    elif 15.50 <= imc_redondeado <= 19.99:
        print(frase_1 + imc_4 + frase_2 + str(imc_redondeado))
    elif 20.00 <= imc_redondeado <= 23.99:
        print(frase_1 + imc_5 + frase_2 + str(imc_redondeado))
    elif 24.00 <= imc_redondeado <= 28.99:
        print(frase_1 + imc_6 + frase_2 + str(imc_redondeado))
    elif 29.00 <= imc_redondeado <= 36.99:
        print(frase_1 + imc_7 + frase_2 + str(imc_redondeado))
    elif imc_redondeado >= 37.00:
        print(frase_1 + imc_8 + frase_2 + str(imc_redondeado))



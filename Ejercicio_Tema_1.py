"""
Crea un archivo de python donde imprimas varias cadenas de texto.

Las cadenas que debes de imprimir son las siguientes:

- Hola, soy [tu_nombre]
- Estoy empezando el curso de python
- Espero aprender mucho
"""




class Imprimir:
    tu_nombre = input('Introduce tu nombre: ').capitalize()
    cadena1 = f'- Hola, soy {tu_nombre}'
    cadena2 = '- Estoy empezando el curso de python'
    cadena3 = '- Espero aprender mucho'
    ver_en_pantalla = f'{cadena1}\n{cadena2}\n{cadena3}'
    print(ver_en_pantalla)


if __name__ == '__main__':
    Imprimir()
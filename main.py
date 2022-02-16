"""
Para este ejercicio tenéis que crear un archivo main.py y dentro tienes que crear variables que representen los
siguientes datos de un contacto:

- Nombre
- Apellidos
- Edad
- Email
- Teléfono
- Casado (verdadero o falso)
- Con Hijos (verdadero o falso)
- Lista de amigos
- Películas vistas (diccionario con clave y valor. El valor será el título de la película)

Una vez hayas creado todas las variables, muéstralas por consola haciendo uso de la función print().
"""

cadena = 'Ha ocurrido un error en '

nombre = input('Nombre: ').capitalize()
apellidos = input('Apellidos: ').capitalize()

while True:
    try:
        edad = int(input('Edad: '))
        if (edad >= 1) and (edad <= 120):
            break
        else:
            print('Si tienes mas de 120 años o menos 0. Lo siento, no esta vivo')
    except:
        print(f'{cadena}edad')

while True:
    try:
        email = input('Email: ')
        if email.count('@') == 1:
            if email.count('.') == 1:
                break
            else:
                print('El email no contiene ningún punto seguido del dominio dominio')
        else:
            print('Hay mas de una @ en el email o no hay')
    except:
        print(f'{cadena}email')

while True:
    try:
        telefono = int(input('Teléfono: '))
        if len(str(telefono)) == 9:
            break
        else:
            print('El teléfono debe contener 9 digitos')
    except:
        print(f'{cadena}teléfono')

while True:
    try:
        casado = input('Casado: Responda (Si, No) ')
        casado = casado.upper()
        if casado == 'SI':
            casado = 'Si'
            break
        elif casado == 'NO':
            casado = 'No'
            break
    except:
        print(f'{cadena}casado')

while True:
    try:
        con_hijos = input('Con hijos: Responda (Verdadero o Falso) ')
        con_hijos = con_hijos.upper()
        if con_hijos == 'VERDADERO':
            con_hijos = 'Verdadero'
            break
        elif con_hijos == 'FALSO':
            con_hijos = 'Falso'
            break
    except:
        print(f'{cadena}con_hijos')

lista_de_amigos = []

while True:
    try:
        pregunta = input('¿Quiere añadir un amigo? (Si, No) ')
        pregunta = pregunta.upper()
        if pregunta == 'SI':
            lista_de_amigos.append(input('¿Como se llama tu amigo? ').capitalize())
        elif pregunta == 'NO':
            break
    except:
        print(f'{cadena}lista_de_amigos')

peliculas_vistas = {}
numero = 1

while True:
    try:
        pregunta = input('¿Quiere añadir una película? (Si, No) ')
        pregunta = pregunta.upper()
        if pregunta == 'SI':
            peliculas_vistas[input('Que película ha visto: ').capitalize()] = f'{numero}'
            numero += 1
        elif pregunta == 'NO':
            break
    except:
        print(f'{cadena}lista_de_amigos')

cadena = f"""
- Nombre: {nombre}
- Apellidos: {apellidos}
- Edad: {edad}
- Email: {email}
- Teléfono: {telefono}
- ¿Casado?: {casado}
- ¿Con Hijos?: {con_hijos}
"""
print(40 * '-')
print(cadena)

if len(lista_de_amigos) > 0:
    print('Lista de amigos:')
    numero = 1
    for amigo in lista_de_amigos:
        print(f'{numero}.- {amigo}')
        numero += 1

if len(peliculas_vistas) > 0:
    print('\nLista de películas:')
    for value, key in peliculas_vistas.items():
        print(f'{key}.- {value}')
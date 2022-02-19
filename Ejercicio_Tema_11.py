"""
En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas:
la columna id de tipo entero, la columna nombre que será de tipo texto
y la columna apellido que también será de tipo texto.

Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 5 alumnos a la tabla.

Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

"""
import sqlite3
import sys

mi_bbdd = 'alumnos.db'


class conexiones:
    def __init__(self):
        self.conexion_bbdd()
        self.menu()

    def insertar(self, dato1, dato2):
        try:
            query = f'INSERT INTO ALUMNOS VALUES(NULL,?,?)'
            self.mi_conexion(query, (dato1, dato2))
            self.menu()

        except:
            print('Registro insertado con éxito')

    def nuevo_alumno(self):
        nombre = input('Nombre: ').upper()
        apellido = input('Apellido: ').upper()
        self.insertar(nombre, apellido)

    def menu(self):
        while True:
            try:
                pregunta = input('\nSeleccione una opción del menu\n'
                                 '1.- Buscar por nombre\n'
                                 '2.- Buscar por apellido\n'
                                 '3.- Añadir un nuevo alumno\n'
                                 '4.- Salir\n')

                if pregunta == '1':
                    nombre = input('Nombre alumno: ').upper()
                    self.buscar_nombre(nombre)
                    break
                elif pregunta == '2':
                    apellido = input('Apellido alumno: ').upper()
                    self.buscar_apellido(apellido)
                    break
                elif pregunta == '3':
                    self.nuevo_alumno()
                    break
                elif pregunta == '4':
                    self.salir()
                    break
                else:
                    print('\nIntroduce una opción correcta')
            except:
                print('Error al seleccionar una opción en el menu')

    def buscar_nombre(self, dato):
        query = 'SELECT * FROM ALUMNOS WHERE NOMBRE=?'
        respuesta_consulta = self.mi_conexion(query, (dato,))
        alumno = respuesta_consulta.fetchone()
        print(f'ID:{alumno[0]} - Nombre: {alumno[1]} {alumno[2]}')
        self.menu()

    def buscar_apellido(self, dato):
        query = 'SELECT * FROM ALUMNOS WHERE APELLIDO=?'
        respuesta_consulta = self.mi_conexion(query, (dato,))
        alumno = respuesta_consulta.fetchone()
        print(f'ID:{alumno[0]} - Nombre: {alumno[2]}, {alumno[1]}')
        self.menu()

    def conexion_bbdd(self):
        conexion = sqlite3.connect(mi_bbdd)
        cursor = conexion.cursor()

        try:
            cursor.execute('''
                CREATE TABLE ALUMNOS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(15),
                APELLIDO VARCHAR(20))
                ''')
        except:
            print('alumnos.db ya existe')

    def mi_conexion(self, query, parameters=()):
        with sqlite3.connect(mi_bbdd) as conexion:
            cursor = conexion.cursor()
            respuesta = cursor.execute(query, parameters)
            conexion.commit()

        return respuesta

    def salir(self):
        sys.exit()


if __name__ == '__main__':
    conexiones()

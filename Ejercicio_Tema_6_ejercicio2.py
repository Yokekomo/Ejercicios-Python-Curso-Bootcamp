"""
En este segundo ejercicio, tendréis que crear un programa que tenga una clase llama Alumno
que tenga como atributos su nombre y su nota.
Deberéis de definir los métodos para inicializar sus atributos, imprimirlos
y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""


class Alumno:

    def __init__(self):
        self.nombre = ''
        self.nota = 0
        self.nombre_nota()

    def nombre_nota(self):
        self.nombre = input('Nombre: ')
        self.nota = float(input('Nota: '))
        return  self.imprimir(self.nombre, self.nota)

    def imprimir(self, nombre, nota):
        ver_en_pantalla = f"\n{50 * '-'}\n{nombre.capitalize()} a sacado una nota de {nota}\n{50 * '-'}"

        print(ver_en_pantalla)


if __name__ == '__main__':
    Alumno()
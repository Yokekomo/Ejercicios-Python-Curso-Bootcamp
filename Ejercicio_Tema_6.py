"""
En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
- Color
- Ruedas
- Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
- Velocidad
- Cilindrada

Por último, crearéis un objeto de la clase Coche y lo mostraréis por consola.
"""


class Vehiculo:

    def __init__(self, color, ruedas, puertas):
        self.color(color)
        self.ruedas(ruedas)
        self.puertas(puertas)

    @staticmethod
    def color(color):
        color = color
        print('El color es:', color)

    @staticmethod
    def ruedas(numero_ruedas):
        ruedas = numero_ruedas
        print(f'Tiene {ruedas} ruedas')

    @staticmethod
    def puertas(numero_puertas):
        puertas = numero_puertas
        print('El numero de puertas es:', puertas)


class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas, puertas)
        self.velocidad(velocidad)
        self.cilindrada(cilindrada)

    @staticmethod
    def velocidad(maxima):
        velocidad = maxima
        print('Velocidad:  0 a', velocidad)

    @staticmethod
    def cilindrada(potencia):
        cilindrada = potencia
        print(f'Cilindrada: {cilindrada}cc')


numero = 1
print(40 * '-', '\n', ' - Coche', numero, '-')
ferrari = Coche('verde', 4, 2, 320, 400)
numero += 1
print(40 * '-', '\n', ' - Coche', numero, '-')
ford = Coche('Negro', 4, 5, 120, 96)
print(40*'-')

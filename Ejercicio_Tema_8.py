"""
En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt,
lo abráis y escribáis dentro del archivo.
Para ello, tendréis que acceder dos veces al archivo creado.

Por último, tendréis que crear otro archivo py y dentro crearéis una clase Vehículo,
haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.

"""
import pickle
from Ejercicio_Tema_8_objetos import *

try:
    with open('archivo.txt', 'ab') as archivo:
        pickle.dump(un_coche, archivo)
except:
    print('Error creando archivo')

try:
    with open('archivo.txt', "rb") as archivo:
        objeto = pickle.load(archivo)
except:
    print('Error al abrir el archivo')

print(type(objeto))
print(objeto)

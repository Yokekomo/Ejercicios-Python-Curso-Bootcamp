"""
En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado
y que contenga un botón de reinicio para que deje todo como al principio.

Al principio no tiene que haber una opción seleccionada.
"""
from tkinter import *


def imprimir_en_consola(_valor):
    print(_valor)


def reiniciar(_valor):
    return _valor


root = Tk()
root.geometry("300x100")

valor = IntVar(value=0)

Radiobutton(root, text='Opcion 1', variable=valor, value=1).place(x=10, y=5)
Radiobutton(root, text='Opcion 2', variable=valor, value=2).place(x=110, y=5)
Radiobutton(root, text='Opcion 3', variable=valor, value=3).place(x=210, y=5)

consultar = Button(root, text='Imprime',
                   command=lambda: imprimir_en_consola(_valor=valor.get()))
consultar.place(x=70, y=50)

consultar = Button(root, text='Reiniciar',
                   command=lambda: reiniciar(_valor=valor.set(value=0)))
consultar.place(x=160, y=50)

root.mainloop()

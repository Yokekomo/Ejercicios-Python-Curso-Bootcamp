"""
En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener
una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.
"""

from tkinter import *

raiz = Tk()
ventana = Frame(raiz)
ventana.pack()

texto = Label(ventana, text='El texto que queráis')
texto.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)

elemento_1 = Checkbutton(ventana, text='Elemento seleccionable 1')
elemento_1.grid(row=1, column=0, sticky='nsew', pady=5, padx=10)

elemento_2 = Checkbutton(ventana, text='Elemento seleccionable 2')
elemento_2.grid(row=2, column=0, sticky='nsew', pady=5, padx=10)

elemento_3 = Checkbutton(ventana, text='Elemento seleccionable 3')
elemento_3.grid(row=3, column=0, sticky='nsew', pady=5, padx=10)

raiz.mainloop()
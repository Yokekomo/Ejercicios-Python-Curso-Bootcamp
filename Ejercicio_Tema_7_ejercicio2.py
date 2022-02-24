"""
En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa.
Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el
tiempo que queda de trabajo.
"""

from datetime import datetime

ahora = datetime.now()
fecha = datetime.date(ahora)
anyo = int(fecha.strftime("%Y"))
mes = int(fecha.strftime("%m"))
dia = int(fecha.strftime("%d"))

ir_casa = datetime(year=anyo, month=mes, day=dia, hour=19, minute=00, second=00)

consulta = datetime.now().time().strftime('%H:%M:%S')
fecha = datetime(year=anyo, month=mes, day=dia, hour=19, minute=00).strftime('%H:%M:%S')

if consulta >= fecha:
    print('Es la hora de ir a casa, disfruta tu tiempo libre')
else:
    consulta = ir_casa - ahora
    consulta = consulta.total_seconds()
    horas, restante = divmod(consulta, 3600)
    minutos, segundos = divmod(restante, 60)

    print(f'Para acabar tu turno de trabajo te quedan {int(horas)} horas y {int(minutos)} minutos.')

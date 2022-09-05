"""
Beecrowd
Problema 1019 Conversión de Tiempo
Link:https://www.beecrowd.com.br/judge/es/problems/view/1019
Se leen los segundos y se calcula el tiempo formato de horas, minutos y segundos calculando primero los minutos y segundos, y luego las horas.
"""
sec = int(input())

min = sec//60
sec = sec%60
hours = min//60
min = min%60
print(f'{hours}:{min}:{sec}')

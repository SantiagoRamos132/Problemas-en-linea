"""
Beecrowd
Problema 2057 Zona Horaria
Link:https://www.beecrowd.com.br/judge/es/problems/view/2057
Se obtiene e imprime la hora de llegada a ese país sumando la hora de salida + las horas de vuelo + la cantidad de horas
extra que tiene el segundo país respecto al primero.
"""
a,b,c = map(int,input().split())
print((a+b+c)%24)

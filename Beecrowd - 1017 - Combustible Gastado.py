"""
Beecrowd
Problema 1017 Combustible Gastado
Link:https://www.beecrowd.com.br/judge/es/problems/view/1017
Se lee el tiempo en horas y la velocidad media del viaje, se  mide la distancia utilizando los dos datos dados anteriormente
y se calcula la cantidad de litros necesarios para realizar el viaje usando la proporción dada al inicio del enunciado del problema.
"""
t = int(input())
v = int(input())
km = t*v
l = km/12
print(format(l,'.3f'))

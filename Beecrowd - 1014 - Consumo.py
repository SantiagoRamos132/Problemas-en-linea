"""
Beecrowd
Problema 1014 Consumo
Link:https://www.beecrowd.com.br/judge/es/problems/view/1014
Se obtiene el consumo promedio de un coche dividiendo la distancia recorrida entre el combustible gastado y luego se imprime.
"""
X = int(input())
Y = float(input())
prom = X/Y
print (format(prom,'.3f'),"km/l")

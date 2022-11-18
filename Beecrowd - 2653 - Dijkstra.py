"""
Beecrowd
Problema 2653 Dijkstra
Link:https://www.beecrowd.com.br/judge/es/problems/view/2653
Conforme se leen las entradas, si la entrada no se encuentra en una lista con entradas leídas anteriormente,
se agrega a la lista y se aumenta en 1 una variable de respuesta, en caso de que si este, se lee la siguiente entrada.
Una vez leídas las entradas se imprime esta variable.
"""
import sys
jewelry = []
resp = 0
for line in sys.stdin:
    if line not in jewelry:
        resp+=1
        jewelry.append(line)
print(resp)
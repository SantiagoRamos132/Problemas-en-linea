"""
Beecrowd
Problema 1172 Array Replacement I
Link:https://www.beecrowd.com.br/judge/es/problems/view/1172

Se guardan las entradas en una lista, y luego se imprime en el formato dado por el problema la posición de cada elemento
en la lista, y su valor, en caso de que el valor sea menor a 1, se imprime 1 en vez del valor original.
"""

L = []
for i in range(10):
    z = int(input())
    L.append(z)
x = 0
for i in L:
    if i<1:
        L[x] = 1
    print(f"X[{x}] = {L[x]}")
    x+=1
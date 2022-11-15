"""
Beecrowd
Problema 2779 Album of the Cup
Link:https://www.beecrowd.com.br/judge/es/problems/view/2779
Se usa una lista en la que se agregan cuales cartas tiene el usuario, y se obtiene el número de cartas faltantes para
completar el álbum restando la cantidad de cartas totales - la cantidad de cartas guardadas en la lista. 
"""
tot = int(input())
compradas = int(input())
l = []
for _ in range(compradas):
    x = int(input())
    if x not in l:
        l.append(x)
print(tot-len(l))
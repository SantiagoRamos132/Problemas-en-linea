"""
Beecrowd
Problema 2968 Hour for a Run
Link:https://www.beecrowd.com.br/judge/es/problems/view/2968
Se guarda en una variable la multiplicación de la cantidad de vueltas por la cantidad de carteles, y se imprime el 10%,20%,...,90% de esa variable.
"""
from math import ceil
V,C = map(int,input().split())
i = 10
tot = V*C
while i < 91:
    if i!=90:
        print(ceil((tot * i) / 100),end=" ")
    else:
        print(ceil((tot * i) / 100))
    i+=10

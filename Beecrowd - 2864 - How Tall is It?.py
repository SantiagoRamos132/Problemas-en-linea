"""
Beecrowd
Problema 2864 How Tall is It?
Link:https://www.beecrowd.com.br/judge/es/problems/view/2864
Se obtiene el vértice de la función cuadrática y se imprime el punto Y de este vertice.
"""
from math import sqrt
T = int(input())
def PuntoY(a,b,c,x):
    return a*x*x + b*x + c
def PuntoX(a,b):
    return (-1*b)/(2*a)
for _ in range(T):
    a,b,c = map(int,input().split())
    x = PuntoX(a,b)
    print(f"{PuntoY(a,b,c,x):.2f}")
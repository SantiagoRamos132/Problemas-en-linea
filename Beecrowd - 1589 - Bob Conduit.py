"""
Beecrowd
Problema 1589 Bob Conduit
Link:https://www.beecrowd.com.br/judge/es/problems/view/1589
La idea es que por cada entrada leída, se imprima la suma del primer número A con el segundo B, ya que esa suma da
el radio mínimo que necesita un círculo para tener adentro dos círculos de radio A y B, sin que A esté adentro de B.
"""
T = int(input())
for _ in range(T):
    a,b = map(int,input().split())
    print(a+b)
"""
Beecrowd
Problema 2172 Evento
Link:https://www.beecrowd.com.br/judge/es/problems/view/2172
Por cada entrada leída, se imprime el resultado de multiplicar el primer número por el segundo, el programa acaba
cuando los números leídos son ceros.
"""
x,m = map(int,input().split())
while x or m:
    print(x*m)
    x,m = map(int,input().split())
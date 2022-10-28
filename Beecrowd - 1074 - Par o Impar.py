"""
Beecrowd
Problema 1074 Par o Impar
Link:https://www.beecrowd.com.br/judge/es/problems/view/1074
Se leen "N" Números, por cada número se debe imprimir si es par o impar, positivo o negativo, o nulo si es cero. Para
esto se usan varias condicionales (modulo 2 para ver paridad, mayor a 0 para ver signo, igual a 0 para ver si es 
nulo).
"""
N = int(input())
for i in range(N):
    num = int(input())
    if num >0:
        if num%2==0:print("EVEN POSITIVE")
        else: print("ODD POSITIVE")
    elif num<0:
        if num%2==0:print("EVEN NEGATIVE")
        else: print("ODD NEGATIVE")
    if num==0: print("NULL")
"""
Beecrowd
Problema 1116 Dividiendo X por Y
Link:https://www.beecrowd.com.br/judge/es/problems/view/1116
Se lee primero la cantidad de números a dividir. Por cada par de números a dividir, se imprime la división del primer número
entre el segundo. En caso de que se intente dividir por 0, se imprime que la división es imposible.
"""
N = int(input())
for i in range(N):
    X,Y = map(int,input().split())
    if Y == 0: print("divisao impossivel")
    else: 
        div = X/Y
        print("%.1f"%div)

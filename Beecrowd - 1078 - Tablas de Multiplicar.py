"""
Beecrowd
Problema 1078 Tablas de Multiplicar
Link:https://www.beecrowd.com.br/judge/es/problems/view/1078
Iterar los números del 1 al 10, e imprimir en forma de tabla el resultado de cada número iterado por la entrada.
"""
N = int(input())
for i in range(1,11):
    print(f'{i} x {N} = {i*N}')
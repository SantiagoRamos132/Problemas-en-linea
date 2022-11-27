"""
Beecrowd
Problema 2232 Pascal's Triangle
Link:https://www.beecrowd.com.br/judge/es/problems/view/2232
La idea es usar la fórmula que calcula la suma de los primeros N términos de una progresión geométrica tomando "a" = 1 y "r" = 2 para cada entrada.
"""
from math import pow
T = int(input())
for _ in range(T):
    N = int(input())
    print(int(pow(2,N))-1)
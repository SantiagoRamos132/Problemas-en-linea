"""
Beecrowd
Problema 2164 Fast Fibonacci
Link:https://www.beecrowd.com.br/judge/es/problems/view/2164
Se calcula el fibonacci de N usando la fórmula dada en el problema.
"""
from math import sqrt
x = int(input())
n = ( ((1+sqrt(5))/2)**x - ((1-sqrt(5))/2)**x )/sqrt(5)
print("%.1f"%(n))
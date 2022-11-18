"""
Beecrowd
Problema 1197 Back to High School Physics
Link:https://www.beecrowd.com.br/judge/es/problems/view/1197
La idea es imprimir el doble de velocidad que tiene la partícula cuando ha pasado el tiempo V.
"""
import sys
for line in sys.stdin:
    a,b = map(int,line.split())
    print(a*b*2)
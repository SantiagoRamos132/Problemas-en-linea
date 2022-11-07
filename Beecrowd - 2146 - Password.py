"""
Beecrowd
Problema 2146 Password
Link:https://www.beecrowd.com.br/judge/es/problems/view/2146
Por cada número escrito en papel, se imprime la contraseña, que es el número escrito en papel -1.
"""
import sys

for line in sys.stdin:
    x = int(line)
    print(x-1)
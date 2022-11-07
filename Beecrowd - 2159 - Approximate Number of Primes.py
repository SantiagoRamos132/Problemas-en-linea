"""
Beecrowd
Problema 2159 Approximate Number of Primes
Link:https://www.beecrowd.com.br/judge/es/problems/view/2159
Se imprime el valor mínimo y máximo del intervalo usando las fórmulas dadas por el problema.
"""
import math
n = int(input())
menor = (n)/math.log(n)
mayor = 1.25506*n/math.log(n)
print(f"{menor:.1f} {mayor:.1f}")
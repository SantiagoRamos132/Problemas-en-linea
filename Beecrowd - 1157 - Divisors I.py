"""
Beecrowd
Problema 1157 Divisors I
Link:https://www.beecrowd.com.br/judge/es/problems/view/1157
Se lee la entrada, y se itera en el rango de los números del 1 hasta la entrada, si el número iterado divide a la entrada, se imprime.
"""
N = int(input())
for div in range(1,N+1):
    if N%div == 0: print(div)

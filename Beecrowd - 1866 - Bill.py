"""
Beecrowd
Problema 1866 Bill
Link:https://www.beecrowd.com.br/judge/es/problems/view/1866
Por cada entero leído, si este entero es impar, se imprime 1, si es par, un 0. 
"""
C = int(input())
for _ in range(C):
	N = int(input())
	if N%2:print(1)
	else:print(0)
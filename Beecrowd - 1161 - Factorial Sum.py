"""
Beecrowd
Problema 1161 Factorial Sum
Link:https://www.beecrowd.com.br/judge/es/problems/view/1161
La idea es implementar la función matemática de factorial en una función de python e imprimir la suma del factorial
de las dos entradas.
"""
import sys
def fact(n):
	if n ==0:return 1
	resp = 1
	i = 1
	while i<n+1:
		resp*=i
		i+=1
	return resp
for line in sys.stdin:
	a,b = map(int,line.split())
	print(fact(a)+fact(b))
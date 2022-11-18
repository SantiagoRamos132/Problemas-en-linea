"""
Beecrowd
Problema 1028 Tarjetas Coleccionables
Link:https://www.beecrowd.com.br/judge/es/problems/view/1028
La idea es obtener el máximo común divisor, e imprimir cuántas veces cabe este número entre las entradas a y b. 
"""
def maximocomundivisor(a,b):
	if b == 0:
		return a
	return maximocomundivisor(b,a%b)
t = int(input())
for _ in range(t):
	a,b = map(int,input().split())
	print(maximocomundivisor(a,b))
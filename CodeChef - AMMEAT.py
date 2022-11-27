"""
CodeChef
Problema AMMEAT 
Link: https://www.codechef.com/problems/AMMEAT
La idea es guardar en una lista los platos, ordenarla de mayor a menor y recorrerla para encontrar cuántos platos necesita llevar como mínimo.
"""
t = int(input())
def solucion(n,m):
	l = list(map(int,input().split()))
	l.sort(reverse=True)
	suma = 0
	for i in range(len(l)):
		suma+=l[i]
		if suma >=m:
			return i+1
	return -1

for _ in range(t):
	n,m = map(int,input().split())
	print(solucion(n,m))
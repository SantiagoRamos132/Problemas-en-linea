"""
CodeChef
Problema KINGSHIP 
Link: https://www.codechef.com/problems/KINGSHIP
La idea es conectar todas las ciudades con la más pequeña para obtener el menor costo total posible, entonces se calcula e imprime este costo.
"""
t = int(input())
for _ in range(t):
	n = int(input())
	l = list(map(int,input().split()))
	l.sort()
	maspeque = l.pop(0)
	print(maspeque*(sum(l)))

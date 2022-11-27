"""
CodeChef
Problema GFTSHP 
Link: https://www.codechef.com/problems/GFTSHP
Se guardan los precios de los items en una lista, se ordena de menor a mayor, y luego se empieza a recorrer, sumando cada item a una variable
de suma y aumentando en 1 la variable de respuesta, una vez que la variable de suma es mayor a la cantidad de dinero disponible, se determina si el último ítem agregado se puede dejar al aplicarle el descuento, si sí, se deja, sino, se resta de la variable respuesta. 
"""
def solucion(n,k):
	global l
	suma = 0
	resp = 0
	for i in range (n):
		suma+=l[i]
		if suma>k:
			suma-=l[i]
			nvasuma = suma+l[i]/2
			if nvasuma>k:
				return resp #no lo pudo meter
			else:
				return resp+1
		else:
			resp+=1
	return resp
t = int(input())
for _ in range(t):
	N,K = map(int,input().split())
	l = list(map(int,input().split()))
	l.sort()
	print(solucion(N,K))

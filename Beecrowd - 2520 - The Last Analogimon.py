"""
Beecrowd
Problema 2520 The Last Analógimôn
Link:https://www.beecrowd.com.br/judge/es/problems/view/2520
La idea es leer primeramente las dimensiones de la matriz, luego leer y guardar la matriz dada. Una vez leída esta matriz,
se llama a la función "resuelve" pasando como parámetro la matriz leída, esta función encuentra las coordenadas del analógimôn y el jugador, y retorna cuántos cuadrados se debe mover vertical y horizontalmente el jugador para alcanzar al analógimôn.
"""
import sys
def resuelve(matriz):
	pok = []
	yo = []
	for i in range(len(matriz)):
		for j in range(len(matriz[0])):
			if matriz[i][j] == 2:
				pok=[i,j]
			if matriz[i][j] == 1:
				yo = [i,j]
	return abs(pok[0]-yo[0]) + abs(pok[1]-yo[1])
cont = 0
mod = 0
matriz = []
for line in sys.stdin:
	if cont == 0:
		if matriz != []: #si ya fue llamada
			listita = list(map(int,line.split()))
			matriz.append(listita)
			print(resuelve(matriz))
			matriz = []
		else:
			x,y = map(int,line.split())
			mod = x
			matriz = []
			cont+=1
			cont%=mod
	else:
		listita = list(map(int,line.split()))
		matriz.append(listita)
		cont+=1
		cont%=mod

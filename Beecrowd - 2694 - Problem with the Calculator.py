"""
Beecrowd
Problema 2694 Problem with the Calculator
Link:https://www.beecrowd.com.br/judge/es/problems/view/2694
La idea es recorrer cada entrada guardada como string de izquierda a derecha, por cada número que se encuentre,
concatenarlo a una variable de número hasta que se encuentre un carácter que no sea un número, en ese caso, se 
pasa la variable anterior a un entero, se suma a una variable de respuesta y se reinicia la variable del número. 
Una vez recorrida toda la entrada, se imprime el valor almacenado en la variable de respuesta.
"""

l = ['0','1','2','3','4','5','6','7','8','9']

def solve(string):
	global l
	num=""
	suma = 0
	for letra in string:
		if letra in l:
			num+=letra
		else:
			if num!="":
				suma+=int(num)
				num=""
	if num!="":suma+=int(num)
	return suma

for _ in range(int(input())):
	print(solve(input()))
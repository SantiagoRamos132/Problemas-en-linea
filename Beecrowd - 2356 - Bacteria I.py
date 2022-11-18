"""
Beecrowd
Problema 2356 Bacteria I
Link:https://www.beecrowd.com.br/judge/es/problems/view/2356
La idea es que para cada caso de prueba, se busque si el string del código genético que da resistencia se encuentra
adentro del ADN de la bacteria, e imprimir si la bacteria es resistente o no basado en el resultado anterior.
"""
import sys
impar = True
a = ""
b = ""
for line in sys.stdin:
	if impar:
		a = line.split()
		impar = False
	else:
		b = line.split()
		impar = True
		if b[0] in a[0]:
			print("Resistente")
		else:
			print("Nao resistente")
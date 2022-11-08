"""
Beecrowd
Problema 2313 Which Triangle
Link:https://www.beecrowd.com.br/judge/es/problems/view/2313
Primero se ve si el triangulo es válido usando la fórmula de la desigualdad triangular, si no es valido, se imprime "Invalido",
en otro caso, si sus tres lados son iguales, se imprime que es equilátero, si dos de sus lados son iguales, se imprime
que es isósceles, y si ninguno de sus lados es igual, se imprime que es escaleno. Además, se averigua si el
triángulo es rectángulo aplicando el teorema de pitágoras, tomando en cuenta que el lado mayor del triangulo (que se toma como hipotenusa)
está almacenado en la variable "a". Luego se imprime si es rectángulo o no.
"""
def desigualdadTriangular(a,b,c):
	return a<(b+c) and b < (a+c) and c<(a+b)
from math import pow
from math import sqrt
l = list(map(int,input().split()))
l.sort(reverse=True)
a = l[0]
b = l[1]
c = l[2]
if desigualdadTriangular(a,b,c):
	if a==b and b==c:
		print("Valido-Equilatero")
	elif a==b or b==c or a==c:
		print("Valido-Isoceles")
	else:
		print("Valido-Escaleno")
	if a == sqrt(pow(b,2)+pow(c,2)):
		print("Retangulo: S")
	else:
		print("Retangulo: N")
else:
	print("Invalido")

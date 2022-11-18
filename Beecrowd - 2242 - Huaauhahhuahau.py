"""
Beecrowd
Problema 2242 Huaauhahhuahau
Link:https://www.beecrowd.com.br/judge/es/problems/view/2242
La idea es guardar en dos strings las vocales de la entrada, uno en orden de izquierda a derecha y el otro al revés, y comparar
si ambos strings son iguales, en caso de que sí lo sean, se imprime "S", sino, se imprime "N".
"""
def darvuelta(x):
	resp = ""
	for z in x:
		resp= z+resp
	return resp
vocales =['a','e','i','o','u']
letra = input()
haciaiz = ""
haciader = ""
for c in letra:
	if c in vocales:
		haciaiz+=c
for c in darvuelta(letra):
	if c in vocales:
		haciader+=c
if haciaiz == haciader:
	print("S")
else:
	print("N")
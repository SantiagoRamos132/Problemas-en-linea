"""
Beecrowd
Problema 1238 Combiner
Link:https://www.beecrowd.com.br/judge/es/problems/view/1238
La idea es ir recorriendo ambos strings desde la posición 0 hasta la última, guardando en una variable
de respuesta el carácter en la posición "i" del primer string y después el carácter en la posición "i" del segundo string,
si este "i" excede el tamaño de alguna de las dos entradas, se deja de añadir carácteres de la entrada más pequeña a la 
variable de respuesta.
"""
for _ in range(int(input())):
	a,b = input().split()
	resp = ""
	i = 0
	while i < max(len(a),len(b)):
		if i < len(a):
			resp+= a[i]
		if i < len(b):
			resp+= b[i]
		i+=1
	print(resp)
"""
Beecrowd
Problema 1120 Contract Revision
Link:https://www.beecrowd.com.br/judge/es/problems/view/1120
La idea es recorrer el número original e ir añadiendo en una lista cada digito del número leído excepto excepto por los
digitos que contienen el número malo, luego pasar los elementos de esa lista a un string y luego imprimir este string como entero, lo que evita
que se impriman ceros a la izquierda.
"""
error,numero = input().split()
while error !="0" or numero!="0":
	l = []
	for num in numero:
		l.append(num)
	i = 0
	while i<len(l):
		if l[i] == error:
			l.pop(i)
		else:
			i+=1
	if l==[]:
		print(0)
	else:
		stringnuevo = ""
		for num in l:
			stringnuevo+=num
		print(int(stringnuevo))
	error,numero = input().split()
"""
Beecrowd
Problema 1241 Fit or Dont Fit II
Link:https://www.beecrowd.com.br/judge/es/problems/view/1241
Primeramente se ve si el tamaño de B es mayor a A, en caso de que sí, se imprime que no encaja, sino, se recorre
de derecha a izquierda los carácteres de A y B, si ocurre que recorriendo estos strings a la vez hay carácteres diferentes 
se imprime que no encaja, si esto nunca ocurre, se imprime que encaja.
"""
for _ in range(int(input())):
	a,b = input().split()
	resp = ""
	x = 0
	solucion = True
	if len(a)>=len(b):
		for i in range(len(b)*-1,0):
			if b[i] != a[i]:
				solucion=False
		if solucion:
			print("encaixa")
		else:
			print("nao encaixa")
	else:
		print("nao encaixa")

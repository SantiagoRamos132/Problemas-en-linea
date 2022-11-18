"""
Beecrowd
Problema 1240 Encajar o No Encajar I
Link:https://www.beecrowd.com.br/judge/es/problems/view/1240
Se guarda los números como strings, se recorren de izquierda a derecha buscando si existe algún número diferente
en una posición de ambos números, si existe, se imprime que no encaja, sino existe, se imprime que encaja.
"""
for _ in range(int(input())):
	a,b = input().split()
	resp = ""
	x = 0
	solucion = True
	if len(a)>=len(b):
		for i in range(len(b)*-1,0):
			if b[x] != a[i]:
				solucion=False
			x+=1
		if solucion:
			print("encaixa")
		else:
			print("nao encaixa")
	else:
		print("nao encaixa")
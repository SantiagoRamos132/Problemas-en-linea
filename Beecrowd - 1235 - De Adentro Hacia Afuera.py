"""
Beecrowd
Problema 1235 De Adentro Hacia Afuera
Link:https://www.beecrowd.com.br/judge/es/problems/view/1235
La idea es recorrer la entrada hasta la mitad y guardar los carácteres en el orden contrario en una variable,
luego hacer lo mismo desde la mitad de la entrada hasta el final y luego imprimir las dos variables.
"""
for _ in range(int(input())):
	resp = ""
	a = input()
	for num in range(len(a)//2):
		resp = a[num] + resp
	segundaparte = ""
	for i in range(len(a)//2,len(a)):
		segundaparte = a[i] + segundaparte
	print(resp+segundaparte)
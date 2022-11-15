"""
Beecrowd
Problema 2963 Buffoon
Link:https://www.beecrowd.com.br/judge/es/problems/view/2963
Se guarda la cantidad de votos de Carlos en una variable y se leen el resto de votos de cada participante, si algún participante
tiene una cantidad mayor a la de Carlos, se imprime que Carlos no fue elegido, sino, se imprime que si lo fue.
"""
n = int(input())
resp = True
for i in range(n):
	if i ==0:carlos = int(input())
	else:
		x = int(input())
		if x>carlos:resp=False
if resp:print("S")
else: print("N")

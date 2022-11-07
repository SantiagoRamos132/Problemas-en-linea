"""
Beecrowd
Problema 2028 Sequence of Sequence
Link:https://www.beecrowd.com.br/judge/es/problems/view/2028
Se usa una función que genera una lista de números dado un N, en la cual por cada número X que hay desde 0 a hasta N,
se agrega el número X X veces (con la excepción que si X=0 se agrega solo una vez). Luego imprime cuantos 
números fueron agregados a la lista junto a la lista. 
"""
import sys
def generalista(n):
	i = 0
	resp = [0]
	while i !=n+1:
		for _ in range(i):
			resp.append(i)
		i+=1
	return resp
caso = 1
for line in sys.stdin:
	listita = generalista(int(line))
	if len(listita) == 1:
		print(f"Caso {caso}: 1 numero")
		print(0)
		print()
	else:
		print(f"Caso {caso}: {len(listita)} numeros")
		for num in listita[:-1]:
			print(num,end=" ")
		print(listita[-1])
		print()
	caso+=1

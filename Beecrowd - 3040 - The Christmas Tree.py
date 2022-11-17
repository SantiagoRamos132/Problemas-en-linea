"""
Beecrowd
Problema 3040 The Christmas Tree
Link:https://www.beecrowd.com.br/judge/es/problems/view/3040
Por cada entrada se determina si el árbol es elegible por Roberto usando condicionales para asegurarse de que
tenga la altura, anchura y cantidad de ramas adecuadas. 
"""
N = int(input())
for _ in range(N):
	a,b,c = map(int,input().split())
	if a>=200 and a<=300 and b>=50 and c>=150:print("Sim")
	else:print("Nao")
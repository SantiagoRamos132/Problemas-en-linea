"""
Beecrowd
Problema 2862 Insect!
Link:https://www.beecrowd.com.br/judge/es/problems/view/2862
Por cada nivel de energía leído de algún ser vivo, si el nivel es mayor de 8000 se imprime "Mais de 8000!", sino, se 
imprime "Inseto!".
"""
N = int(input())
for _ in range(N):
	C = int(input())
	if C>8000:print("Mais de 8000!")
	else:print("Inseto!")
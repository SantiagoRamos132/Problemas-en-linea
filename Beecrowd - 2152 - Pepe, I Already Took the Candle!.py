"""
Beecrowd
Problema 2152 Pepe, I Already Took the Candle!
Link:https://www.beecrowd.com.br/judge/es/problems/view/2152
Por cada caso de prueba, si el último número es un 0, se imprime que la puerta se cerro a la hora dada
por el caso de prueba, si no, se imprime que la puerta se abrió a esa hora.
"""
N = int(input())
for _ in range(N):
	H,M,O = map(int,input().split())
	if H <10:
		H =f"0{H}"
	if M <10:
		M =f"0{M}"
	if O:print(f"{H}:{M} - A porta abriu!")
	else:print(f"{H}:{M} - A porta fechou!")
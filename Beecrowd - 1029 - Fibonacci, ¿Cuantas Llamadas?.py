"""
Beecrowd
Problema 1029 Fibonacci, ¿Cuántas Llamadas?
Link:https://www.beecrowd.com.br/judge/es/problems/view/1029
La idea es crear dos listas en las que se van a ir almacenando los primeros 40 números de fibonacci y la cantidad de llamadas
recursivas de cada número, luego se crea la típica función de fibonacci con la variante de que si el resultado del número buscado se encuentra en la lista, lo devuelve y la función no se llama a sí misma de nuevo. También se crea la función "cuentallamadasrec" que usa la otra lista para almacenar cuántas llamadas recursivas  usa la función de fibonacci normal para calcular un número.
Luego por cada caso de prueba se imprime lo solicitado usando estas funciones.
"""
l = [0]*40
memo = [0] * 40
def fibo(n):
	global memo
	if n<2:return n
	if memo[n]:return memo[n]
	memo[n] = fibo(n-1)+fibo(n-2)
	return memo[n]
def cuentallamadasrec(n):
	global l
	if n <2:
		return 1
	if l[n]:
		return l[n]
	l[n] = cuentallamadasrec(n-1)+cuentallamadasrec(n-2) +1
	return l[n]

casos = int(input())
for _ in range(casos):
	x = int(input())
	print(f"fib({x}) = {cuentallamadasrec(x)-1} calls = {fibo(x)}")

"""
Beecrowd
Problema 1165 Prime Number
Link:https://www.beecrowd.com.br/judge/es/problems/view/1165

Se crea la funcion que verifica si un número X es primo, la cual verifica primero si el número es par, si no, 
recorre todos los números impares hasta la raiz de X, y si encuentra un número que divide a X, retorna Falso, si no, retorna 
verdadero.

La razón por la que se recorre hasta la raíz de X para saber si el número es primo, es por que si un número tiene 
un factor mayor que su raíz, su otro factor debe ser menor que su raíz. Esto se prueba demostrando por contradicción 
la siguiente proposición:
si n = pq entonces p<=n^1/2 o q<=n^1/2..

Por cada caso de prueba, se imprime si el número ingresado es primo o no utilizando la función anteriormente creada.
"""
import sys
sys.setrecursionlimit(1000000)
def esPrimo(n):
	if n == 2:
		return True
	if n%2 == 0:
		return False
	i = 3
	while(i*i<=n):
		if n%i== 0:
			return False
		i+=2
	return True

N = int(input())
for _ in range(N):
    x = int(input())
    if esPrimo(x):
        print(x,"eh primo")
    else: print(x,"nao eh primo")
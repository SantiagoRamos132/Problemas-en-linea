"""
Beecrowd
Problema 1164 Perfect Number
Link:https://www.beecrowd.com.br/judge/es/problems/view/1164
Se crea una función que retorna la suma de los factores propios de un número, y luego por cada caso de prueba,
se compara el número con la suma de sus factores propios. Si son iguales, se imprime que es perfecto, si no, se imprime 
que no lo es.
En la función de la suma de factores propios, se recorren únicamente hasta los números hasta la raíz del número
para encontrar su factores porque si un factor es menor a la raíz, el otro es mayor a la raíz.
Esto se prueba demostrando por contradicción la siguiente proposición
si n = pq entonces p<=n^1/2 o q<=n^1/2.
"""
def sumaFactoresPropios(n):
	suma = 1
	i = 2
	while i*i<n:
		if n%i == 0:
			suma+=i + (n//i)
		i+=1
	if i*i == n:
		suma+=i
	return suma

def esPerfecto(n):
    if n==1:
        return False
    return n == sumaFactoresPropios(n)

N = int(input())
for _ in range(N):
    x = int(input())
    if esPerfecto(x): print(x,"eh perfeito")
    else: print(x,"nao eh perfeito")

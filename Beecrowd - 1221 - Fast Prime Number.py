"""
Beecrowd
Problema 1221 Fast Prime Number
Link:https://www.beecrowd.com.br/judge/es/problems/view/1221
La idea es crear una función que recorra los números impares hasta la raíz de un número N buscando si existe
algún número que divida a N (si el factor X de un número N es mayor a la raíz, el otro factor que multiplicado por X es
igual a N debe ser menor que la raíz, por lo que no hace falta buscar después de la raíz más divisores de N), en 
caso de que exista, se imprime que N no es primo, sino, se imprime que es Primo.
"""
def esprimo(n):
	if n == 2:
		return"Prime"
	if n%2 == 0:
		return"Not Prime"
	i = 3
	while(i*i<=n):
		if n%i== 0:
			return"Not Prime"
		i+=2
	return"Prime"
n = int(input())
for _ in range(n):
    x = int(input())
    print (esprimo(x))

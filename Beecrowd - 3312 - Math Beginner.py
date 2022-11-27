"""
Beecrowd
Problema 3312 Math Beginner
Link:https://www.beecrowd.com.br/judge/es/problems/view/3312
Si un número de la entrada es primo, se imprime su factorial. Para obtener estos dos datos se emplea la función recursiva de factorial y la función
"esprimo" que busca si un número tiene factores propios desde 2 hasta su raíz y con esto determina si es primo o no.
"""
def fact(n):
    if n ==0:return 1
    return n*fact(n-1)
def esprimo(n):
	if n == 2:
		return True
	if n%2 == 0 or n==1:
		return False
	i = 3
	while(i*i<=n):
		if n%i== 0:
			return False
		i+=2
	return True
N = int(input())
lista = list(map(int,input().split()))
for i in lista:
    if esprimo(i):print(f"{i}! = {fact(i)}")


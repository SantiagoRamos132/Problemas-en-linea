"""
Beecrowd
Problema 2167 Fallo de Motor
Link:https://www.beecrowd.com.br/judge/es/problems/view/2167
Por cada caso de prueba, se guarda las mediciones en una lista, luego se recorre de izquierda a derecha esa lista,
y se termina de recorrer cuando el número en la posición i es menor al número en la posición i-1 en la lista, en este
caso, se imprime la posición i+1 donde ocurrió el cambio. Si nunca ocurre lo anterior, se imprime un 0.
"""
N = int(input())
lista = list(map(int,input().split()))
mayor = 0
pos = 0
for i in range(len(lista)):
	if lista[i] > mayor:
		mayor= lista[i]
	if lista[i] <mayor:
		pos+=i+1
		break

print(pos)
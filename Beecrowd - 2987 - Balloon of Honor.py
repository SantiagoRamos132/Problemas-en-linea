"""
Beecrowd
Problema 2987 Balloon of Honor
Link:https://www.beecrowd.com.br/judge/es/problems/view/2987
Se guarda en una lista las letras del abecedario, se recorre hasta encontrar la letra correspondiente a la entrada
y se imprime la posición de esa letra en la lista -1.
"""
lista = ["A","B","C","D","E","F","G","H","I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S","T","U","V","W","X","Y","Z"]
N = input()
for i in range(len(lista)):
	if lista[i] == N:print(i+1) 

"""
Beecrowd
Problema 1042 Clasificación Simple
Link:https://www.beecrowd.com.br/judge/es/problems/view/1042
Se guardan los números según fueron leídos en las variables a,b,c, y se ordena una lista de los mismos números
de menor a mayor,luego se imprime los elementos de la lista y las variables leídas inicialmente según indica el enunciado del problema
"""
lista = list(map(int,input().split()))
a,b,c = lista[0],lista[1],lista[2]
lista.sort()
for i in lista:
    print(i)
print(end= "\n")
print(a)
print(b)
print(c)

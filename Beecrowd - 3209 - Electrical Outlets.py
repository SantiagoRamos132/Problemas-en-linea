"""
Beecrowd
Problema 3209 Electrical Outlets
Link:https://www.beecrowd.com.br/judge/es/problems/view/3209
Por cada entrada leída, se obtiene el número de enchufes totales de todas las regletas y se le resta la cantidad
de enchufes totales -1, debido a que cada regleta excepto la última en ser conectada tiene otra regleta conectada a uno de sus enchufes.
"""
N = int(input())
for _ in range(N):
    lista = list(map(int,input().split()))
    suma = 0
    for i in range(1,len(lista)):
        suma+=lista[i]
    print(suma-(lista[0]-1))
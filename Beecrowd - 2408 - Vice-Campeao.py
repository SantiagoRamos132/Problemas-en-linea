"""
Beecrowd
Problema 2408 Vice-Campeão
Link:https://www.beecrowd.com.br/judge/es/problems/view/2408
La idea es guardar los tres números en una lista, ordenarla e imprimir el segundo elemento de la lista, que corresponde al segundo número más grande
de la lista.
"""
listaEntrada = list(map(int,input().split()))
listaEntrada.sort()
print(listaEntrada[1])
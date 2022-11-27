"""
Beecrowd
Problema 2137 The Library of Mr. Severino
Link:https://www.beecrowd.com.br/judge/es/problems/view/2137
La idea es guardar los códigos en una lista y usar la función sort de python que los ordena de menor a mayor en la lista, para luego imprimir esta lista
ordenada.
"""
import sys
for line in sys.stdin:
    n = int(line)
    listaCodigos = []
    for i in range(n):
        listaCodigos.append(input())
    listaCodigos.sort() #De menor a mayor
    for codigo in listaCodigos:
        print(codigo)
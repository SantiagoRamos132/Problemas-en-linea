"""
Beecrowd
Problema 1546 Feedback
Link:https://www.beecrowd.com.br/judge/es/problems/view/1546
La idea es guardar de manera ordenada de menor a mayor los nombres de los equipos en una lista, y luego que
por cada entrada X se imprima el nombre del equipo en la posición X-1 de la lista.
"""
l = ["Rolien","Naej","Elehcim","Odranoel"]
n = int(input())
for _ in range(n):
    x = int(input())
    for _ in range(x):
        num = int(input())
        print(l[num-1])
"""
Beecrowd
Problema 1865 Mjölnir
Link:https://www.beecrowd.com.br/judge/es/problems/view/1865
Por cada entrada leída, imprimir "Y" si el personaje que desea alzar el martillo es Thor, sino, se imprime "N".
"""
C = int(input())
for _ in range(C):
    a,b = input().split()
    if a == "Thor": print("Y")
    else: print("N")

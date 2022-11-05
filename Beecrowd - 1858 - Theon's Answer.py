"""
Beecrowd
Problema 1858 Theon's Answer
Link:https://www.beecrowd.com.br/judge/es/problems/view/1858
La idea es guardar el número de personas en una lista, y luego recorrer esta lista para encontrar la posición i en la que se encuentra 
el número más pequeño de la lista, e imprimir i+1.
"""
x = input()
y = input().split()
menor = y[0]
resp = 0
for i in range(len(y)):
    if y[i]<menor:
        menor = y[i]
        resp=i
print(resp+1)

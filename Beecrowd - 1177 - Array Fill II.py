"""
Beecrowd
Problema 1177 Array Fill II
Link:https://www.beecrowd.com.br/judge/es/problems/view/1177
Se lee una entrada N y se imprime un arreglo de mil elementos, donde el valor de cada elemento es dado por el residuo la división
de su posición en el arreglo entre N.
"""
n = int(input())
x = 0
for i in range(1000):
    print(f"N[{i}] = {x%n}")
    x+=1

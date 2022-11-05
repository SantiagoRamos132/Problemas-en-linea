"""
Beecrowd
Problema 1959 Regular Simple Polygons
Link:https://www.beecrowd.com.br/judge/es/problems/view/1959
Se imprime el perímetro (cantidad de lados * longitud de cada lado) de un polígono dado su cantidad de lados y la longitud de cada lado.
"""
N,L = map(int,input().split()) #N num de lados y L longitud
print(N*L)

"""
Beecrowd
Problema 2160 Name at Form
Link:https://www.beecrowd.com.br/judge/es/problems/view/2160
Se obtiene la cantidad de carácteres de la línea leída, si hay más de 80, se imprime que no cabe
en un espacio reservado para 80 carácteres, en caso contrario, se imprime que si cabe.
"""
x = input()
if len(x) <81: print("YES")
else: print("NO")
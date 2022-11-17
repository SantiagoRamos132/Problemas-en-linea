"""
Beecrowd
Problema 3170 Christmas Balls
Link:https://www.beecrowd.com.br/judge/es/problems/view/3170
Si la cantidad de bolas necesarias es menor o igual a las que tenía, se imprime que Amelia tiene todas las bolas, sino, se imprime cúantas 
le faltan (cantidad de bolas necesarias - cantidad de bolas que tiene actualmente).
"""
B = int(input())
G = int(input())
if G//2<=B:print("Amelia tem todas bolinhas!")
else:print(f"Faltam {(G//2)-B} bolinha(s)")

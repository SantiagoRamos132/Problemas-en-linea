"""
Beecrowd
Problema 1113 Ascendiendo y Descendiendo
Link:https://www.beecrowd.com.br/judge/es/problems/view/1113
Se leen dos números enteros, si no son iguales, se imprime si están en orden ascendiente o decresciente y el programa continua. Si son iguales, se termina el programa.
"""
va = True
while va:
    X,Y = map(int,input().split())
    if X == Y: va = False
    elif X>Y: print("Decrescente")
    else: print("Crescente")

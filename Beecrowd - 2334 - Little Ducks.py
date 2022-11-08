"""
Beecrowd
Problema 2334 Little Ducks
Link:https://www.beecrowd.com.br/judge/es/problems/view/2334
La idea de esta solución es imprimir que la cantidad de patos que regresan es igual a la cantidad de patos
inicial -1, a excepción de la cantidad de patos inicial sea 0. En ese caso, la cantidad de patos que regresan también es 0.
"""
P = int(input())
while (P!=-1):
    if (P<2):
        print(0)
    else:
        print(P-1)
    P = int(input())
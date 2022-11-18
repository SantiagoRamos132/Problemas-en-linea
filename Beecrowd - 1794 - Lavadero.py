"""
Beecrowd
Problema 1794 Lavadero
Link:https://www.beecrowd.com.br/judge/es/problems/view/1794
Si la cantidad de prendas se encuentra dentro de los rangos establecidos de la secadora y lavadora, se imprime
que es posible lavar y secar las prendas, en caso contrario, se imprime que es imposible.
"""
prendas = int(input())
LA,LB = map(int,input().split())
SA,SB = map(int,input().split())
if prendas >= LA and prendas <=LB and prendas >= SA and prendas<=SB:
    print("possivel")
else:
    print("impossivel")
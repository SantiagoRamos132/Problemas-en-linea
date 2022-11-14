"""
Beecrowd
Problema 2540 Leader's Impeachment
Link:https://www.beecrowd.com.br/judge/es/problems/view/2540
Por cada entrada, si la cantidad de votos para desistuir al líder es mayor o igual a 2/3 de los jugadores, se imprime
"impeachment", sino, se imprime "acusacao arquivada".
"""
import sys
espar = False
n = 0
s = 0
for line in sys.stdin:
    if not(espar):
        n = int(line)
        espar=True
    else:
        listita = list(map(int,line.split()))
        s = sum(listita)
        if s >= n*2/3:
            print("impeachment")
        else:
            print("acusacao arquivada")
        espar=False

"""
Beecrowd
Problema 2234 Hot Dogs
Link:https://www.beecrowd.com.br/judge/es/problems/view/2234
Se imprime el promedio de los hot dogs consumidos  por participantes en la competición dados la cantidad de hot dogs
consumidos y el número de participantes de la competición.
"""
H,P = map(int,input().split())
print ("%.2f"%(H/P))
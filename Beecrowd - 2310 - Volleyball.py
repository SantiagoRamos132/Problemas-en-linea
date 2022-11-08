"""
Beecrowd
Problema 2310 Volleyball
Link:https://www.beecrowd.com.br/judge/es/problems/view/2310
Se crean dos listas, "total" y "exitosos", que contienen 3 espacios, el primero correspondiente a saques,
el segundo corresponde a bloqueos y el tercero a ataques. Por los datos de cada jugador leído, se actualizan
los valores en estas dos listas según los datos leídos (si son el total de saques, bloqueos y ataques realizados por el jugador, se 
actualizan los valores de la lista "total", sino, se actualizan los datos de "exitosos").
Luego de leer todos los datos, se imprime el porcentaje de saques, bloqueos y ataques exitosos del equipo.
"""
n = int(input())
total = [0,0,0]
exitosos = [0,0,0]
for _ in range(n):
    nombre = input()
    t1,t2,t3 = map(int,input().split())
    total[0] += t1
    total[1] += t2
    total[2] += t3
    e1,e2,e3 = map(int,input().split())
    exitosos[0] += e1
    exitosos[1] += e2
    exitosos[2] += e3
print(F"Pontos de Saque: {(exitosos[0]/total[0])*100:.2f} %.")
print(F"Pontos de Bloqueio: {(exitosos[1]/total[1])*100:.2f} %.")
print(F"Pontos de Ataque: {(exitosos[2]/total[2])*100:.2f} %.")

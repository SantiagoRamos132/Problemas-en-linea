"""
Beecrowd
Problema 2311 Diving
Link:https://www.beecrowd.com.br/judge/es/problems/view/2311
Por cada participante, se guarda los puntuajes en una lista y se ordena de menor a mayor, de esta manera
se elimina el menor y mayor puntuaje quitando el primer y último elemento de la lista.
Luego se calcula la puntuación final multiplicando la suma de los puntuajes por la dificultad, y se imprime 
esta puntuación junto al nombre del participante.
"""
n = int(input())
for _ in range(n):
    nombre = input()
    dificultad = float(input())
    puntuajes = list(map(float,input().split()))
    puntuajes.sort()
    puntuajes.pop(0) #quitar el menor puntuaje
    puntuajes.pop() #quitar el mayor puntuaje
    resp = sum(puntuajes)*dificultad
    print(f"{nombre} {resp:.2f}")
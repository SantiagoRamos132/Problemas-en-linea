"""
Beecrowd
Problema 1131 Grenais
Link:https://www.beecrowd.com.br/judge/es/problems/view/1131
El programa lee primeramente el resultado de un partido, aumenta en 1 la variable de partidos jugados, y dependiendo
del resultado del partido, se aumenta en 1 la variable de empates si fue empate, o la variable del equipo ganador (Inter o Gremio).
Luego se pide al usuario si desea ingresar el resultado de un partido nuevo, en caso de que sí, se repite el proceso anterior, si no. Se imprime
el total de partidos jugados, las victorias del Inter, las victorias del Gremio, la cantidad de partidos empatados y cuál de los dos equipos
venció al otro (en caso de que hayan ganado la misma cantidad de partidos, se imprime que no hubo ganador).
"""
Inter = 0
Gremio = 0
goles = 0
empates =0
partidos = 0
while True:
    i,g = map(int,input().split())
    partidos +=1
    goles+= i+g
    print("Novo grenal (1-sim 2-nao)")
    goles+=i+g
    if i >g:
        Inter+=1
    elif i<g:
        Gremio+=1
    else: empates+=1
    x = int(input())
    if x == 2:
        break
print(partidos,"grenais")
print(f"Inter:{Inter}")
print(f"Gremio:{Gremio}")
print(f"Empates:{empates}")
if Inter > Gremio:
    print("Inter venceu mais")
elif Gremio > Inter:
    print("Gremio venceu mais")
else:
    print("Não houve vencedor")

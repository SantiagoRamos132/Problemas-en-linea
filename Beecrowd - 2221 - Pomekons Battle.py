"""
Beecrowd
Problema 2221 Pomekons Battle
Link:https://www.beecrowd.com.br/judge/es/problems/view/2221
Por cada entrada, se lee el bonus del Pomekon de Dadriel, se calcula valor del Pomekon con la fórmula dada, y si su nivel
es par, se le suma el bonus, se hace el mismo proceso con el Pomekon de Guarte, y se realiza una comparación con el valor
de ambos Pomekon, imprimiendo el resultado de la batalla según indica el problema.
"""
t = int(input())
for _ in range(t):
    bonus = int(input())
    ataque,defensa,nivel = map(int,input().split())
    d = ((ataque+defensa)//2)
    if nivel%2==0:
        d+=bonus
    ataque,defensa,nivel = map(int,input().split())
    g = ((ataque+defensa)//2)
    if nivel%2==0:
        g+=bonus
    if g==d:
        print("Empate")
    elif g>d:
        print("Guarte")
    else:
        print("Dabriel")
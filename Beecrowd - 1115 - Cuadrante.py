"""
Beecrowd
Problema 1115 Cuadrante
Link:https://www.beecrowd.com.br/judge/es/problems/view/1115
Se lee una coordenada en un plano cartesiano, y se utilizan los signos de los puntos X,Y para imprimir en que cuadrante se encuentra
esa coordenada. Teniendo en cuenta que:

Las coordenadas con signos (+,+) en los puntos x,y se encuentran en el primer cuadrante.
Las coordenadas con signos (-,+) en los puntos x,y se encuentran en el segundo cuadrante.
Las coordenadas con signos (-,-) en los puntos x,y se encuentran en el tercer cuadrante.
Las coordenadas con signos (+,-) en los puntos x,y se encuentran en el cuarto cuadrante.

En caso de que el punto X o el punto Y sea 0, se termina el programa.
"""
a,b = map(float,input().split())
while (a!=0 and b!=0):
    if a>0:
        if b>0:print("primeiro")
        else: print("quarto")
    else:
        if b>0:print("segundo")
        else: print("terceiro")
    a,b = map(float,input().split())

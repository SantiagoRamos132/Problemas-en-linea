"""
Beecrowd
Problema 2168 Twilight at Portland
Link:https://www.beecrowd.com.br/judge/es/problems/view/2168
Se guarda el mapa en una matriz, y se recorre cada cuadrado de 2x2 de esta matriz, viendo si en ese cuadrado
hay almenos dos camaras (unos), en caso de que sí, se imprime "S" y si no, se imprime "U". El recorrido de los cuadrados
de la matriz se hace de izquierda a derecha, empezando por los cuadrados ubicados en la parte más superior de la matriz.
"""
n = int(input())
matriz = []
for _ in range(n+1):
    l = list(map(int,input().split()))
    matriz.append(l)

def estaseguro(mapa,posx,posy):
    cantcamaras = 0
    for i in range(posx,posx+2):
        for j in range(posy,posy+2):
            if mapa[i][j] == 1:
                cantcamaras+=1
    if cantcamaras >1:
        return "S"
    else:
        return "U"

for i in range(n):
    for j in range(n):
        print(estaseguro(matriz,i,j),end="")
    print("")
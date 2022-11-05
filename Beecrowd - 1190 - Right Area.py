"""
Beecrowd
Problema 1190 Right Area
Link:https://www.beecrowd.com.br/judge/es/problems/view/1190
La idea de esta solución es guardar los números leídos en una matriz de 12x12, luego recorrer los números que se encuentran en las posiciones
i,j de la matriz que cumplen las siguientes condiciones:
i>0 y i<11
Si i>=1 y i<6,  j>=12-i y j<12
Si i>=6 y i<11, j>=i+1 y j<12

Cada número recorrido suma a una variable de suma total y aumenta en 1 la variable correspondiente a la cantidad
de números recorridos. Luego se imprime el promedio o la suma de estos números recorridos dependiendo del carácter leído inicialmente.
"""
operacion = input()
matriz = []
for i in range(12):
    l = []
    for j in range(12):
        inp = float(input())
        l.append(inp)
    matriz.append(l)
s = 0
c = 0
for i in range(1,6): #1-5
    for j in range(12-i,12):
        s+=matriz[i][j]
        c+=1
for i in range(6,11): #6-1
    for j in range(i+1,12):
        s+=matriz[i][j]
        c+=1


if operacion == "S":
    print(f"{s:.1f}")
if operacion == "M":
    print(f"{s/c:.1f}")
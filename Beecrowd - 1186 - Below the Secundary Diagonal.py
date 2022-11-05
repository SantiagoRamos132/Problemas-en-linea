"""
Beecrowd
Problema 1186 Below the Secundary Diagonal
Link:https://www.beecrowd.com.br/judge/es/problems/view/1186
La idea de esta solución es guardar los números leídos en una matriz de 12x12, luego recorrer los números que se encuentran en las posiciones
i,j de la matriz tales que  j >= 12-i y j <12, sumando cada número a una variable de suma total y guardando en otra variable la cantidad
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
for i in range(1,12):
    for j in range(12-i,12):
        s+=matriz[i][j]
        c+=1

if operacion == "S":
    print(f"{s:.1f}")
if operacion == "M":
    print(f"{s/c:.1f}")

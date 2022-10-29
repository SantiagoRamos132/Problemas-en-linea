"""
Beecrowd
Problema 1143 Squared and Cubic
Link:https://www.beecrowd.com.br/judge/es/problems/view/1143
Se lee un entero N y se imprimen N lineas, donde cada línea contiene 3 enteros, el primero es el número de línea,
el segundo es el cuadrado del número de línea, y el tercero es el cubo del número de línea.
"""
N = int(input())
for i in range(N):
    i+=1
    print(i,i*i,i*i*i)
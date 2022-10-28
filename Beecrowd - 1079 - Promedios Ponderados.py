"""
Beecrowd
Problema 1079 Promedios Ponderados
Link:https://www.beecrowd.com.br/judge/es/problems/view/1079
Por cada caso de prueba, se obtiene e imprime el promedio ponderado de 3 números flotantes, sabiendo que el primer número tiene un peso 2, el segundo peso 3 y el 
tercero peso 5. (Se suman los 3 números multiplicados por sus pesos respectivos y esa suma se divide entre la suma de pesos totales, que en este caso es 10)
"""
N = int(input())
for i in range(N):
    a,b,c = map(float,input().split())
    print( format(((a*2+b*3+c*5)/10),'.1f') )

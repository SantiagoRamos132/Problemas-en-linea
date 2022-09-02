"""
Beecrowd
Problema 1006 Promedio 2
Link:https://www.beecrowd.com.br/judge/es/problems/view/1006
El programa lee tres flotantes e imprime el promedio ponderado de los tres flotantes con 1 decimal. Este promedio se obtiene con una proporción de los valores
ganados versus el total de valores posible.
"""
A = float(input())
B = float(input())
C = float(input())
PROM = (A*2+B*3+C*5)/10
print ("MEDIA =",format(PROM,'.1f'))

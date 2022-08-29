"""
Beecrowd
Problema 1006 Promedio 2
Link:https://www.beecrowd.com.br/judge/es/problems/view/1006
El programa lee tres flotantes e imprime el promedio ponderado de los tres flotantes con 1 decimal. Este promedio se obtiene dividiendo la suma de los flotantes multiplicados por su peso entre la suma de todos los pesos
"""
A = float(input())
B = float(input())
C = float(input())
PROM = (A*2+B*3+C*5)/10
print ("MEDIA =",format(PROM,'.1f'))

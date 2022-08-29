"""
Beecrowd
Problema 1005 Promedio 1
Link:https://www.beecrowd.com.br/judge/es/problems/view/1005
El programa lee dos flotantes e imprime el promedio ponderado de los dos flotantes con 5 decimales. Este promedio se obtiene dividiendo la suma de los flotantes multiplicados por su peso entre la suma de todos los pesos
"""
A = float(input())
B = float(input())
prom = (A*3.5+B*7.5)/11
print ("MEDIA =",format(prom,'.5f'))

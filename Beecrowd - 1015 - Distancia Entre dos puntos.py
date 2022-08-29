"""
Beecrowd
Problema 1015 Distancia Entre dos puntos
Link:https://www.beecrowd.com.br/judge/es/problems/view/1015
Se leen los dos puntos y se imprime el resultado de aplicar la fórmula dada con esos puntos en el problema.
"""
a = list(map(float,input().split()))
b = list(map(float,input().split()))
x1 = a[0]
y1 = a[1]
x2 = b[0]
y2 = b[1]

d = pow(pow((x2-x1),2) + pow((y2-y1),2),1/2)
print (format(d,'.4f'))

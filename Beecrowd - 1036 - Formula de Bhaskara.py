"""
Beecrowd
Problema 1036 Fórmula de Bhaskara
Link:https://www.beecrowd.com.br/judge/es/problems/view/1036
Se leen los valores para aplicar en la fórmula, se verifica si no hay una división por cero (a=0) o una raíz negativa
en la fórmula (discriminante sea negativo), en caso de que suceda alguno de los dos casos, imprimir que no se pueden calcular las raíces de la fórmula de Bhaskara, en caso contrario, imprimirlas con 5 digitos luego del punto decimal
"""
num = list(map(float,input().split()))
a = num[0]
b = num[1]
c = num[2]
dis = b**2 - 4*a*c
if dis < 0 or a == 0:
    print('Impossivel calcular')
else:
    x = (-b + (dis)**0.50)/(2*a)
    y = (-b - (dis)**0.50)/(2*a)
    print(f'R1 = {x:.5f}')
    print(f'R2 = {y:.5f}')

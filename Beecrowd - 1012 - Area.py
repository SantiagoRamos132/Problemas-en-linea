"""
Beecrowd
Problema 1012 Área
Link:https://www.beecrowd.com.br/judge/es/problems/view/1012
El programa lee 3 flotantes e imprime el área de cada figura solicitada utilizando los tres flotantes leídos, asegurándose que cada función reciba los parámetros correctos. 
"""
A,B,C = map(float,input().split())
triangulo = (A*C)/2
circulo = 3.14159*C*C
trapecio = ((A+B)*C)/2
cuadrado = B*B
rectangulo = A*B
print('TRIANGULO:',format(triangulo,'.3f'))
print('CIRCULO:',format(circulo,'.3f'))
print('TRAPEZIO:',format(trapecio,'.3f'))
print('QUADRADO:',format(cuadrado,'.3f'))
print('RETANGULO:',format(rectangulo,'.3f'))

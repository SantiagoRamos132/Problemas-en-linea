"""
Beecrowd
Problema 1035 Prueba de Selección 1
Link:https://www.beecrowd.com.br/judge/es/problems/view/1035
Se leen cuatro enteros que se asignan a las variables a,b,c,d, luego usar una condicional que indique si se cumplen todas las condiciones dadas en el enunciado del problema para imprimir si los valores son aceptados o no.
"""
valores = list(map(int,input().split()))
a = valores[0]
b = valores[1]
c = valores[2]
d = valores[3]
if b>c and d>a and (c+d)>(a+b) and c>0 and d>0 and a%2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')

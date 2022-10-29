"""
Beecrowd
Problema 1133 Resto de la División
Link:https://www.beecrowd.com.br/judge/es/problems/view/1133
Se leen dos números de entrada "X" y "Y", se recorren todos los números entre "X" y "Y" en orden ascendente, y por
cada número recorrido si el residuo al ser dividido por 5 es 2 o 3, se imprime ese número.
"""
X = int(input())
Y = int(input())

if X>Y:
    for i in range(Y+1,X):
        if i%5 == 2 or i%5 == 3:
            print (i)
else:
    for i in range(X+1,Y):
        if i%5 == 2 or i%5 == 3:
            print (i)
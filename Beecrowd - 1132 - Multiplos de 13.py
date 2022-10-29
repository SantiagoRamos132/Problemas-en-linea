"""
Beecrowd
Problema 1132 Múltiplos de 13
Link:https://www.beecrowd.com.br/judge/es/problems/view/1132
Se leen dos números enteros, luego se itera en el intervalo del número menor al mayor, y por cada número iterado divisible entre 13,
se suma ese número a una variable que contiene la suma de todos los números de 13 en ese intervalo. Una vez recorrido
el intervalo, se imprime la variable mencionada anteriormente.
"""
X = int(input())
Y = int(input())
suma = 0
if Y > X:
    for i in range(X,Y+1):
        if not (i%13 == 0):
            suma+=i
else:
    for i in range(Y,X+1):
        if not (i%13 == 0):
            suma+=i
print (suma)

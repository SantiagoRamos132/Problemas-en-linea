"""
Beecrowd
Problema 1071 Suma de Números Consecutivos Impares
Link:https://www.beecrowd.com.br/judge/es/problems/view/1071
Se leen los dos números, luego se recorren los números del menor al mayor y se imprime la suma de cada número impar entre ellos.
"""
X = int(input())
Y = int(input())
suma = 0
if X>Y:
    for i in range(Y+1,X):
        if i%2 == 1:
            suma= suma+i
else:
    for i in range(X+1,Y):
        if i%2 == 1:
            suma= suma+i
    
print(suma)

"""
Beecrowd
Problema 1065 Pares Entre Cinco Números
Link:https://www.beecrowd.com.br/judge/es/problems/view/1065
Se recorren todos los números desde 1 hasta la entrada, y se imprimen los impares (números que al ser divididos por 2 dan residuo 1).
"""
x = int(input())
for i in range(1,x+1):
    if i%2 == 1:
        print(i)

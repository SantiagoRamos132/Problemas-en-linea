"""
Beecrowd
Problema 1067 Números Impares
Link:https://www.beecrowd.com.br/judge/es/problems/view/1067
Se lee un número y se recorren los números del 1 hasta el número leído, imprimiendo los números impares (número que al ser dividido por 2 da residuo 1).
"""
x = int(input())
for i in range(1,x+1):
    if i%2 == 1:
        print(i)

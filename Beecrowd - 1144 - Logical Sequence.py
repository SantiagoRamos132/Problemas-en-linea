"""
Beecrowd
Problema 1144 Logical Sequence
Link:https://www.beecrowd.com.br/judge/es/problems/view/1144
Se lee un entero N, Se imprime 2*N cantidad de líneas. La idea es que las líneas impares "X" contenga un valor "Y" = (X+1)/2
,"Y" al cuadrado y "Y" al cubo, y que las líneas pares tengan el primer elemento de la línea impar anterior, el segundo
elemento de la linea impar anterior aumentado en 1, y el tercer elemento de la linea impar anterior aumentado en 1.
"""
N = int(input())
for i in range(N):
    i+=1
    print(f'{i} {i*i} {i*i*i}')
    print(f'{i} {i*i+1} {i*i*i+1}')
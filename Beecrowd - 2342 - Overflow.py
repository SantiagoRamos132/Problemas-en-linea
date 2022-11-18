"""
Beecrowd
Problema 2342 Overflow
Link:https://www.beecrowd.com.br/judge/es/problems/view/2342
La idea es realizar la operación dada en la segunda línea de la entrada, y si el resultado es mayor al primer número leído, imprimir "OVERFLOW", sino, imprimir "OK".
"""
maximo = int(input())
a,b,c = input().split()
if b=="+":
    if int(a)+int(c) >maximo:
        print("OVERFLOW")
    else:
        print("OK")
else:
    if int(a)*int(c) >maximo:
        print("OVERFLOW")
    else:
        print("OK")

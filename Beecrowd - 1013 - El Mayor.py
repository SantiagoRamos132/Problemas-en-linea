"""
Beecrowd
Problema 1013 El Mayor
Link:https://www.beecrowd.com.br/judge/es/problems/view/1013
Se crea la función mayor, que utiliza la fórmula matemática utilizada para encontrar el máximo de dos números, y utiliza esa función para encontrar el número mayor de tres enteros leídos y luego imprimirlo. Para encontrar este número utiliza la función con el primer entero leído junto al resultado de la misma función aplicada con los otros dos enteros. 
"""
L = input().split()
A = int(L[0])
B = int(L[1])
C = int(L[2])

def mayor(a,b):
    return ((a+b)+abs(a-b))//2


print(mayor(A,mayor(B,C)),'eh o maior')

"""
Beecrowd
Problema 2787 Chess
Link:https://www.beecrowd.com.br/judge/es/problems/view/2787
Se imprime si la casilla es negra o blanca viendo la paridad de tanto las filas como las columnas.
"""
L = int(input())
C = int(input())
if L%2==0:
    if C%2==0:
        print(1)
    elif C%2==1: print(0)
if L%2==1: #SI LA LINEA ES IMPAR
    if C%2==0: #SI LA COLUMNA ES PAR IMPRIMIR NEGRO
        print(0)
    elif C%2==1: print(1)

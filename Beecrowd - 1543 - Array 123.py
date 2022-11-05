"""
Beecrowd
Problema 1543 Array 123
Link:https://www.beecrowd.com.br/judge/es/problems/view/1543
La idea es que dado un entero N, se va a imprimir N veces, un número de N digitos representado en un string (en este
caso, N carácteres de números) donde cada digito es un 3, excepto en dos posiciones, que tendrán un 1 o un 2.
La idea es que por cada vez que se imprima el número, se corra el 1 un lugar hacia la derecha, y el 2 un lugar hacia la izquierda,
tomando en cuenta que la primera vez el 1 estará en la posición 0 del string y el dos en la posición n-1 del string. 
"""
import sys

def imprimidor(uno,dos,entero):
    resp = ""
    for i in range(entero):
        if i == dos:
            resp+="2"
        elif i == uno:
            resp+="1"
        else:
            resp+="3"
    print(resp)
def funcion(entero):
    posiuno = 0
    posidos = entero-1
    while posiuno<entero:
        imprimidor(posiuno,posidos,entero)
        posiuno+=1
        posidos-=1

for line in sys.stdin:
    funcion(int(line))

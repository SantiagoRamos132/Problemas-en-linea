"""

Beecrowd
Problema 1871 Zero means Zero
Link: https://www.beecrowd.com.br/judge/es/problems/view/1871
Autor: Ricardo Martins
La idea de la solucion es leer dos enteros, enviar la suma de los dos enteros a la funcion quitaceros e imprimir el resultado. 
El programa se detiene cuando los dos enteros son 0.
La idea del while de la funcion quitaceros es ver si el ultimo digito del entero recibido es 0, de no serlo, agregarlo a la variable de respuesta poniendolo una cifra
a la izquierda de esta variable, luego dividir entero entre 10 para repetir el proceso con otro digito de entero.

"""


def quitaceros(entero):
    resp = 0
    cont = 1
    while entero!=0:
        if entero%10!=0:
            resp+=entero%10*cont
            cont*=10
        entero//=10   
    return resp

while True:
    a,b = map(int,input().split())
    if a ==0 and b ==0:
        quit()
    print(quitaceros(a+b))

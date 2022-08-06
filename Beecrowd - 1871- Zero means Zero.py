"""

Beecrowd
Problema 1871 Zero means Zero
Link: https://www.beecrowd.com.br/judge/es/problems/view/1871
Autor: Ricardo Martins
La idea de la solucion es leer dos enteros, enviar la suma de los dos enteros como un string a la funcion quitaceros, la cual retorna el mismo string pero sin ceros
despues imprimir este nuevo string. El programa se detiene cuando los dos enteros que lee son dos ceros.

"""


def quitaceros(string):
    resp = ""
    for i in string:
        if i !="0":
            resp+=i
    return resp
while True:
    a,b = map(int,input().split())
    if a ==0 and b ==0:
        quit()
    print(quitaceros(str(a+b)))

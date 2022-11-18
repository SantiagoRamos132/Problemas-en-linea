"""
Beecrowd
Problema 2044 Incobrable
Link:https://www.beecrowd.com.br/judge/es/problems/view/2044
La idea es recorrer la entrada como una lista de números, e ir guardando en una variable de deuda
la deuda de Ignacio, y si en algún momento esta deuda es múltiplo de 100, se aumenta en 1 una variable con la 
cantidad de veces que Irene va a ir a cobrar la deuda. Luego de recorrer esta lista, se imprime el número almacenado
en esta última variable.
"""
while True:
    n = int(input())
    if n ==-1:quit()
    deuda = 0
    cant = 0
    l = list(map(int,input().split()))
    for num in l:
        deuda+=num
        deuda%=100
        if deuda == 0:
            cant+=1
    print(cant)
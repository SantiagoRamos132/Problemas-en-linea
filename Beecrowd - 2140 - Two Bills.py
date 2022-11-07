"""
Beecrowd
Problema 2140 Two Bills
Link:https://www.beecrowd.com.br/judge/es/problems/view/2140
Se crea una lista de todos los posibles cambios que se pueden dar (todas las combinaciones de la suma dos elementos
de 2,5,10,20,50 y 100), por cada caso de prueba, se busca el cambio a dar en esta lista, si no aparece, se imprime
que es imposible dar el cambio justo, en caso contrario, se imprime que si si es posible dar el cambio justo. 
"""
cambios = [7,12,22,52,102,15,25,55,105,30,60,110,70,120,150]
while True:
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        quit()
    vuelto = b-a
    if vuelto in cambios:
        print("possible")
    else:
        print("impossible")
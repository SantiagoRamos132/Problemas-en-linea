"""
Beecrowd
Problema 1847 Welcome to the Winter!
Link:https://www.beecrowd.com.br/judge/es/problems/view/1847
Se leen las temperaturas de los tres días, y se utilizan condicionales para determinar si se debe imprimir
una cara triste o una cara feliz basándose en los 8 casos dados por el problema.
"""
d1,d2,d3 = map(int,input().split())
happy = ":)"
sad = ":("


if d1 > d2: #decrecion del dia 1 al dia d2
    if d2 <=d3: #subio del dia 2 al d3 o se mantuvo constante
        print(happy) #caso 1
    if d2>d3: #bajo del 2 al 3
        if d2-d3 < d1-d2:
            print(happy) #caso 5
        else:
            if d2-d3 >= d2-d1:
                print(sad) #caso 6

if d1==d2:
    if d2<d3:
        print(happy) #caso 7
    else:
        print(sad) #caso 8


if d1 < d2: #crecio del dia 1 al dia 2
    if d2 >= d3: #bajo del dia 2 al d3 o se mantuvo constante
        print(sad) #caso 2
    elif d2<d3: #crecio del d2 al d3
        if d3-d2 < d2-d1: 
            print(sad) #caso 3
        if d3-d2 >=d2-d1:
            print(happy) #caso 4
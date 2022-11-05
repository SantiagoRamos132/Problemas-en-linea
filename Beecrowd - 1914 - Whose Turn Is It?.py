"""
Beecrowd
Problema 1914 Whose Turn Is It?
Link:https://www.beecrowd.com.br/judge/es/problems/view/1914
Por cada caso, se calcula la suma de los dos números dados, si la suma es impar, se imprime el nombre del jugador que escogió
la palabra "IMPAR" , y si la suma de los dos números dados es par, se imprime el nombre del jugador que escogió la palabra "PAR".
"""
n = int(input())
for _ in range(n):
    n,l1,m,l2 = list(input().split())
    x,y = map(int,input().split())
    z = x+y

    if l1=="IMPAR":
        if z%2: print(n)
        else: print(m)
    if l1=="PAR":
        if z%2 == 0:
            print(n)
        else:print(m)
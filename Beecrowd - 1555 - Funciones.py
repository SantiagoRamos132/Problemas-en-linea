"""
Beecrowd
Problema 1555 Funciones
Link:https://www.beecrowd.com.br/judge/es/problems/view/1555
La idea es implementar las tres funciones, para obtener el resultado de las tres funciones dada una entrada, e imprimir cuál función retorna el mayor valor pasando como parámetro esa entrada.
"""
def rafael(x,y):
    return 3*x*3*x + y*y
def beto(x,y):
    return 2*(x*x)+5*y*5*y
def carlos(x,y):
    return -100*x+y*y*y
N = int(input())
for _ in range(N):
    x,y = map(int,input().split())
    r = rafael(x,y)
    b = beto(x,y)
    c = carlos(x,y)
    if r>b and r>c:
        print("Rafael ganhou")
    if b>r and b>c:
        print("Beto ganhou")
    if c>r and c>b:
        print("Carlos ganhou")

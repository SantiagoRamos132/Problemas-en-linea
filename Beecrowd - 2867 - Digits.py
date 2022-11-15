"""
Beecrowd
Problema 2867 Digits
Link:https://www.beecrowd.com.br/judge/es/problems/view/2867
Se obtiene el resultado de "a" elevado a "b", y se divide este resultado por 10 hasta que el resultado sea 0. Luego
de esto, se imprime las veces que el número fue divido por 10, que corresponden a la cantidad de dígitos del número.
"""
def elevar(b,p):
    if p ==1:return b
    num = elevar(b,p//2)
    resp = num*num
    if p%2:
        resp*=b
    return resp

C = int(input())
for _ in range(C):
    a,b = map(int,input().split())
    num = elevar(a,b)
    i = 0
    while num!=0:
        num//=10
        i+=1
    print(i)
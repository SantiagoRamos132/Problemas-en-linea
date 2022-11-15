"""
Beecrowd
Problema 2807 Iccanobif
Link:https://www.beecrowd.com.br/judge/es/problems/view/2807
La idea es crear una lista de los N números de la secuencia de Fibonacci, darle la vuelta a esa lista e imprimirla.
"""
def fiboaux(n,p,u):
    if n ==0:
        return p
    return fiboaux(n-1,u,p+u)
def fibocola(n):
    return fiboaux(n,0,1)

x = int(input())
l = []
for i in range(1,x+1):
    l.append(fibocola(i))
l.sort(reverse=True)
for i in range(x):
    if i ==x-1:
        print(l[i])
    else:
        print(l[i],end=" ")
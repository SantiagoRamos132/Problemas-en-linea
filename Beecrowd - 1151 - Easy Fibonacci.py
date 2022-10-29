"""
Beecrowd
Problema 1151 Easy Fibonacci
Link:https://www.beecrowd.com.br/judge/es/problems/view/1151
Se programa la función de fibonacci con recursión de cola, y se imprime los primeros N números de fibonacci
en una sola línea usando la función anterior.
"""
n = int(input())
def fiboaux(n,p,u):
    if n==0:return p
    return fiboaux(n-1,u,p+u)
def fibocola(n):
    return fiboaux(n,0,1)

for i in range(n-1):
    print (fibocola(i),end=" ")
print (fibocola(n-1))
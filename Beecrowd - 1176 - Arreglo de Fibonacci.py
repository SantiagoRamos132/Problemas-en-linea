"""
Beecrowd
Problema 1176 Arreglo de Fibonacci
Link:https://www.beecrowd.com.br/judge/es/problems/view/1176
Se crea una función recursiva de cola que calcula un número de fibonacci pedido, luego se leen las entradas y se imprime
el valor de fibonacci de cada entrada (calculado con la función creada previamente) usando el formato dado en el problema.
"""
def fiboColaAux(n, f0, f1):
    if n == 0:
        return f0
    return fiboColaAux(n-1, f1, f0+f1)

def fiboCola(n):
    return fiboColaAux(n,0,1)
    
T = int(input())
for i in range(T):
    n = int(input())
    print(f"Fib({n}) =",fiboCola(n))
"""
Beecrowd
Problema 1174 Array Selection I
Link:https://www.beecrowd.com.br/judge/es/problems/view/1174
Se iteran los números del intervalo de (0,100), por cada iteración, se lee un valor. Si el valor es 
menor a 11, se imprime el número por el que se itera en ese momento y el valor con un solo dígito después del punto
decimal.
"""
for i in range(100):
    n = float(input())
    if n <= 10:
        print(f"A[{i}] = {n:.1f}")
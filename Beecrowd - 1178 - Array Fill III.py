"""
Beecrowd
Problema 1178 Array Fill III
Link:https://www.beecrowd.com.br/judge/es/problems/view/1178
Se imprime el primer número leído como si fuera la primera posición de un arreglo, y luego se divide este número a la mitad
y se imprime como si su nuevo valor fuera el número en la segunda posición de un arreglo. El proceso se repite hasta
haber imprimido 100 números.
"""
n = float(input())
for i in range(100):
    print(f"N[{i}] = {n:.4f}")
    n/=2

"""
Beecrowd
Problema 1173 Array fill I
Link:https://www.beecrowd.com.br/judge/es/problems/view/1173
Se crea una función itera el intervalo de (0,10), por cada iteración del intervalo,
imprime el número que itera junto al valor de la entrada y después de imprimir duplica el valor de la entrada.
"""
n = int(input())
for i in range(10):
    print(f"N[{i}] = {n}")
    n*=2
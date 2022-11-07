"""
Beecrowd
Problema 2147 Galopeira
Link:https://www.beecrowd.com.br/judge/es/problems/view/2147
Por cada caso de prueba, se obtiene e imprime el tiempo usado en escribir cada mensaje multiplicando la longitud del mensaje
por 1/100.
"""
c = int(input())
for _ in range(c):
    x = input()
    print(f"{len(x)*1/100:.2f}")
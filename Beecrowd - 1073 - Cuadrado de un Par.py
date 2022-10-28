"""
Beecrowd
Problema 1073 Cuadrado de un Par
Link:https://www.beecrowd.com.br/judge/es/problems/view/1073
Se itera en cada número desde 1 hasta la entrada, y por cada número par (residuo 0 al ser divido por 2), se imprime su cuadrado
en el formato del problema.
"""
N = int(input())
N-= N%2

for i in range(N):
    i+=1
    if i%2==0:
        print(f'{i}^2 = {i*i}')
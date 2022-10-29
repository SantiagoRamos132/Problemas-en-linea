"""
Beecrowd
Problema 1142 PUM
Link:https://www.beecrowd.com.br/judge/es/problems/view/1142
Se usa un programa que imprime N cantida de lineas, donde cada linea corresponde a un entero X, X+1, X+2 y el mensaje
"PUM", y cada vez que se cambia de linea, se aumenta X en 4.
"""
N = int(input())
numero = 1
for i in range(N):
    print(f'{numero} {numero+1} {numero+2} PUM')
    numero+=4
"""
Beecrowd
Problema 1075 Resto 2
Link:https://www.beecrowd.com.br/judge/es/problems/view/1075
Se itera los números de 1 a 10000 y si el número iterado al dividirlo por la entrada da residuo 2, se imprime.
"""
N = int(input())
for i in range(1,10001):
    if i%N==2: print(i)

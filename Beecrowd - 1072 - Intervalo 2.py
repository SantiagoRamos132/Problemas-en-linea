"""
Beecrowd
Problema 1072 Intervalo 2
Link:https://www.beecrowd.com.br/judge/es/problems/view/1072
Se lee cuantos números van a ser leidos. Por cada número leído, si se encuentra dentro del intervalo
[10,20] (mayor o igual a 10 y menor o igual a 20), se aumenta 1 a la variable de números dentro del intervalo, y en 
caso contrario se aumenta 1 a la variable de números fuera del intervalo. Luego se imprimen estas dos variables.
"""
N = int(input())
IN = 0
OUT = 0
for i in range(N):
    x = int(input())
    if x >= 10 and x<=20:
        IN+=1
    else: OUT+=1
print(IN,"in")
print(OUT,"out") 
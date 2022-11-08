"""
Beecrowd
Problema 2344 Notas da Prova
Link:https://www.beecrowd.com.br/judge/es/problems/view/2344
Dada una nota numérica, se utilizan condicionales para determinar a que nota conceptual corresponde, luego se imprime
esta nota conceptual.
"""
n = int(input())
if n == 0:print("E")
elif n<=35:print("D")
elif n<=60:print("C")
elif n<=85:print("B")
elif n<=100:print("A")

"""
Beecrowd
Problema 1170 Blobs
Link:https://www.beecrowd.com.br/judge/es/problems/view/1170
La idea es despejar la siguiente ecuación para obtener el número de días dada una cantidad de comida
2^X = Comida
donde X son los días.
Una vez despejada se obtiene que X = log2(comida), por lo que para cada entrada se aplica la función anterior para
obtener el número de días buscado.
"""
from math import log2
from math import ceil
t = int(input())
for _ in range(t):
	x = float(input())
	print(ceil(log2(x)),"dias")

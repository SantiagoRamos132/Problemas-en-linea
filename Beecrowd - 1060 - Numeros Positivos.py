"""
Beecrowd
Problema 1060 Números Positivos
Link:https://www.beecrowd.com.br/judge/es/problems/view/1060
Se leen 6 números, y por cada numero positivo encontrado, se aumenta la variable "positivos" en 1. Luego se imprime
cuantos números positivos se encontraron (valor almacenado en variable "positivos")
"""
positivos = 0
for i in range(6):
    a = float(input())
    if a >0: positivos+=1
print(f"{positivos} valores positivos")
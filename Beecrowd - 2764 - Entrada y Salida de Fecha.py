"""
Beecrowd
Problema 2764 Entrada y Salida de Fecha
Link:https://www.beecrowd.com.br/judge/es/problems/view/2764
Se lee una fecha y se imprime en los tres formatos dados.
"""
d,m,a = input().split("/")
print(f"{m}/{d}/{a}")
print(f"{a}/{m}/{d}")
print(f"{d}-{m}-{a}")
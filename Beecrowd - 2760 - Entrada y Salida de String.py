"""
Beecrowd
Problema 2760 Entrada y Salida de String
Link:https://www.beecrowd.com.br/judge/es/problems/view/2760
Se leen los tres strings y se imprimen en el orden dado.
"""
a = input()
b = input()
c = input()
print(a+b+c)
print(b+c+a)
print(c+a+b)
print(a[:10]+b[:10]+c[:10])
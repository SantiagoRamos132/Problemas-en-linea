"""
Beecrowd
Problema 1020 Edad en Días
Link:https://www.beecrowd.com.br/judge/es/problems/view/1020
Se lee la edad de una persona en días y se calcula la edad en formato de años, meses y días, considerando un año como 365 días 
y un mes como 30 días. 
"""
dia = int(input())
ano = dia//365
dia %= 365
mes = dia//30
dia%= 30

print(ano,'ano(s)')
print(mes,'mes(es)')
print(dia,'dia(s)')

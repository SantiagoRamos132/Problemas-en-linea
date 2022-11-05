"""
Beecrowd
Problema 1759 Ho Ho Ho
Link:https://www.beecrowd.com.br/judge/es/problems/view/1759
Se imprime "Ho" N veces, y al último "Ho" se le agrega el carácter "!".
"""
t = "Ho"
n = int(input())
for i in range(n-1):
    t+=" Ho"
print(t+"!")

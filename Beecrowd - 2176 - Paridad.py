"""
Beecrowd
Problema 2176 Paridad
Link:https://www.beecrowd.com.br/judge/es/problems/view/2176
Se guarda la entrada como un string, y se cuentan cuántos unos tiene el string, en caso de que esta cantidad sea par, se agrega
un 1 al final del string y se imprime, sino, se agrega un 0 al final del string y también se imprime.
"""
cantuno = 0
entrada = input()
for i in entrada:
    if int(i):
        cantuno+=1
if cantuno%2:
    entrada+= "1"
else:
    entrada+= "0"
print(entrada)
"""
Beecrowd
Problema 2753 Salida 7
Link:https://www.beecrowd.com.br/judge/es/problems/view/2753
Se imprimen los números desde 97 a 122, junto al carácter ASCII representado por cada número.
"""
x = 97
for _ in range(26):
    print(f"{x} e {chr(x)}")
    x+=1
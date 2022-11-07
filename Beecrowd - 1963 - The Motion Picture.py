"""
Beecrowd
Problema 1963 The Motion Picture
Link:https://www.beecrowd.com.br/judge/es/problems/view/1963
La idea es imprimir el procentaje incrementado reemplazando el primer precio (i1) y el segundo (i2) en la siguiente formula
((i2-i1)*100)/i1 
"""
i1,i2 = map(float,input().split())
incremento = ((i2-i1)*100)/i1
print(f"{incremento:.2f}%")
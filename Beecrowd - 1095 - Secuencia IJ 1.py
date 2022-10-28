"""
Beecrowd
Problema 1095 Secuencia IJ 1
Link:https://www.beecrowd.com.br/judge/es/problems/view/1095
Se crea un programa que imprime una secuencia en la que se le resta 5 a una variable J iniciada en 60, 
y suma a la vez 3 a una variable I que empieza en 1, hasta que J sea 0.
"""
I = 1
J = 60
while J>0:
    print(f'I={I} J={J}')
    I+=3
    J-=5
if J==0:
    print("I=37 J=0")

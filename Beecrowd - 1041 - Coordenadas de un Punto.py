"""
Beecrowd
Problema 1041 Coordenadas de un Punto
Link:https://www.beecrowd.com.br/judge/es/problems/view/1041
Se leen dos flotantes de entrada que representan las coordenadas de un punto en un plano
y se utilizan varias condicionales para encontrar en que parte del plano se encuentra ese punto  
"""
x,y = map(float,input().split())
if (x,y) == (0,0):
    print("Origem")
elif x==0 or y == 0:
    print('Eixo X') if y==0 else print("Eixo Y")
elif x>0:
    print("Q1") if y>0 else print("Q4")
elif x<0:
    print("Q2") if y>0 else print("Q3")
"""
Beecrowd
Problema 1134 Type of Fuel
Link:https://www.beecrowd.com.br/judge/es/problems/view/1134
Se leen diferentes códigos de tipos de combustible, y por cada código leído se aumenta en 1 una variable
que contiene el total de veces que se usó ese combustible. Cuando el código leído es 4, el programa se detiene
e imprime cuantos clientes usaron Alcohol, Gasolina y Diesel.
"""
entrada = 0
A = 0
G = 0
D = 0
while (entrada!=4):
    entrada = int(input())
    if entrada ==1:
        A+=1
    elif entrada ==2:
        G+=1
    elif entrada ==3:
        D+=1
print("MUITO OBRIGADO")
print("Alcool:",A)
print("Gasolina:",G)
print("Diesel:",D)
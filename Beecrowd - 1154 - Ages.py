"""
Beecrowd
Problema 1154 Ages
Link:https://www.beecrowd.com.br/judge/es/problems/view/1154
Se crean dos variables, una conteniendo la suma de todas las edades leídas, y otra de la cantidad de edades leídas,
luego se empiezan a leer edades hasta que se lea una edad negativa. Por cada edad leída, se agrega la variable de 
la suma y se aumenta la variable de la cantidad de edades en 1. Después de leer las edades, se imprime el promedio de estas.
"""
suma = 0
edades = 0
while True:
    edad = int(input())
    if edad <0: break
    suma+=edad
    edades+=1

print(format((suma/edades),'.2f'))
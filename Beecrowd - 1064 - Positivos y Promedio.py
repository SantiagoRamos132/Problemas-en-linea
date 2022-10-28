"""
Beecrowd
Problema 1064 Positivos y Promedio
Link:https://www.beecrowd.com.br/judge/es/problems/view/1064
Se leen 6 números, por cada número positivo, se aumenta 1 al contador de números positivos, y se suma este número
a la variable que contiene la suma de los valores positivos.
Luego se imprime cuantos números positivos se leyeron, y el promedio de estos 
((suma de todos los números positivos)/cantidad de numeros positivos)
"""
positivos = 0
suma= 0
for i in range(6):
    num = float(input())
    if num >0: 
        positivos +=1
        suma+=num

print(positivos,"valores positivos")
print(format((suma/positivos),'.1f'))
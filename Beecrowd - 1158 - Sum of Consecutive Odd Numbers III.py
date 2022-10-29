"""
Beecrowd
Problema 1158 Sum of Consecutive Odd Numbers III
Link:https://www.beecrowd.com.br/judge/es/problems/view/1158
Por cada caso de prueba, se leen dos números a,b, se calcula la suma de los b siguientes números impares consecutivos de 
"a" (empezando por "a" si es impar) usando un for que vaya aumentando a "a" en dos unidades, y sumando "a" 
a una variable de respuesta, luego se imprime esta respuesta.
"""
n = int(input()) #Casos pruebas que van a ser input
for _ in range(n):
    a,b = map(int,input().split())
    suma = 0
    if a%2:
        for x in range(b):
            suma+=a
            a+=2
    else:
        a+=1
        for x in range(b):
            suma+=a
            a+=2
    print (suma)
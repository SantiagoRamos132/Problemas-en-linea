"""
Beecrowd
Problema 1099 Suma de Números Consecutivos Impares II
Link:https://www.beecrowd.com.br/judge/es/problems/view/1099
Se lee cuantos casos de prueba van a haber. Por cada caso de prueba, se leen dos numeros, se itera del número menor
al mayor, y por cada número impar encontrado, se suma a una variable "suma". Luego de iterar estos números, se imprime 
"suma".
"""
n = int(input()) #Casos pruebas que van a ser input
for i in range(n):
    a,b = map(int,input().split())
    if a > b:
        suma = 0
        for z in range(b+1,a):
            if z%2: suma+=z
        print(suma)  
    else:
        suma = 0
        for z in range(a+1,b):
            if z%2: suma+=z
        print(suma) 
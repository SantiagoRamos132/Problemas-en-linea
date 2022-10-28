"""
Beecrowd
Problema 1080 El Más Alto y Su Posición
Link:https://www.beecrowd.com.br/judge/es/problems/view/1080
Se crean dos variables para el valor del número más alto("mayor") y su posición("posicion"), y se leen 100 números. Por cada número leído, si su valor es mayor
al valor guardado en la variable "mayor", se actualizan las dos variables. Una vez leídos los 100 números, se imprimen las variables.
"""
mayor = 0
posicion = 0
for i in range(1,101):
    x = int(input())
    if x > mayor:
        mayor = x
        posicion = i
print(mayor)
print(posicion)

"""
Beecrowd
Problema 1181 Line in Array
Link:https://www.beecrowd.com.br/judge/es/problems/view/1181
La idea de esta solución es primero guardar en una variable N el número de línea del de interés,
luego la operación a realizar con los elementos de esa línea y crear una variable que va guardando la suma de los elementos de esa línea.
Siguientemente se leen los 144 números de la matriz y se determina si el número pertenece a la línea de interés 
(Esto se determina si en el turno que se lee este número, este turno se encuentra dentro del rango
[12*N,12*N+11]), si pertenece, se suma a la variable de la suma de los elementos de esa línea, luego de leer los números
del arreglo, se imprime el resultado de la operación leída aplicada a los números de esa línea.
"""
linea = int(input())
operacion = input()
suma = 0
for turno in range(144):
    flotante = float(input())
    if turno >= 12*linea and turno <=12*linea+11:
        suma+=flotante
                
if operacion == "S":
    print(f"{suma:.1f}")
else:
    print(f"{suma/12:.1f}")

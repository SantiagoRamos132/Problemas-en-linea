"""
Beecrowd
Problema 1182 Column in Array
Link:https://www.beecrowd.com.br/judge/es/problems/view/1182
Primero se guarda en una variable C el número de columna de interés del arreglo, luego la operación a realizar con los elementos
de esa línea y se crea una variable que va guardando la suma de los elementos de esa línea.
Por cada número leído, se determina si pertenece a la columna C cuando el turno en el que se lee este número es múltiplo de C. Si pertenece,
se suma a la variable de suma. Después de leer todos los números, se imprime esa variable si la operación leída es una S,
si no, el promedio de los números de la columna de interés.
"""
c = int(input())
operacion = input()
suma = 0
for i in range(144):
    x = float(input())
    if i%12==c:
        suma+=x
if operacion == "S":
    print(f"{suma:.1f}")
else:
    print(f"{(suma/12):.1f}")

"""
Beecrowd
Problema 1429 Factorial Again!
Link:https://www.beecrowd.com.br/judge/es/problems/view/1429
La idea detrás de la solución es guardar cada entrada como un string, iterarlo carácter por carácter, donde el número de cada carácter se multiplica
por el factorial de su posición en el string (por ejemplo en "154", se multiplica el 5 por 2!) y sumar el resultado a la variable de respuesta.
Debido a que los números de entrada no tienen más de 5 dígitos, se guarda en una lista los factoriales de 1 hasta 5 para no tener que calcularlos
varias veces.
"""
factoriales = [1,1,2,6,24,120]
entrada = input()
while (entrada != '0'):
    acm = 0
    digitos = len(entrada)
    i = 0
    while (i<digitos):
        acm+= int(entrada[digitos-i-1])*factoriales[i+1]
        i+=1
    print(acm)
    entrada=input()

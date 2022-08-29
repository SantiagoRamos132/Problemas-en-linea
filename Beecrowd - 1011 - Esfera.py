"""
Beecrowd
Problema 1011 Esfera
Link:https://www.beecrowd.com.br/judge/es/problems/view/1011
Se crea la función volumen que recibe el radio de una esfera y retorna su volumen, luego se lee el radio una esfera y después se imprime el volumen de esa esfera utilizando la función previamente creada.
"""
pi = 3.14159
r = int(input())
def volumen(r):
    return (4/3) * pi * r*r*r

print("VOLUME =",format(volumen(r),'.3f'))

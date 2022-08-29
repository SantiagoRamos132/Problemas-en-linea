"""
Beecrowd
Problema 1003 Suma Simple
Link:https://www.beecrowd.com.br/judge/es/problems/view/1003
El programa crea la variable n que tiene el numero de pi, crea la función ¨Area¨ que recibe el radio de un círculo y retorna su área, luego lee un flotante que es el radio de un círculo e imprime el valor del área con 4 decimales.
"""
n = 3.14159
def Area(r):
    return r*r*n
r = float(input())
print(f"A={Area(r):.4f}")

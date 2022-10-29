"""
Beecrowd
Problema 1150 Excediendo Z
Link:https://www.beecrowd.com.br/judge/es/problems/view/1150
Se lee un número inicial X, y se continua leyendo hasta encontrar un número Z mayor a X.

Sabiendo que la fórmula para encontrar la suma entre dos numeros a y b, b>=a, es 
(b(b+1)-a(a-1))/2

para cada caso de prueba se necesita encontrar un B tal que
(b(b+1)-X(X-1))/2 > Z

despejando la expresión anterior, se obtiene la expresión

B^2 + b - (x(x-1)-2z) > 0.

reemplazando el > por = se obtiene una expresión cuadratica, con la cuál podemos despejar B

B^2 + b - (x(x-1)-2z) = 0.

Con esta función cuadrática, por cada caso de prueba, se reemplaza X y Z y se obtiene la solución positiva (el valor de B positivo
que satisfaga la función cuadrática) usando la fórmula de Bhaskara.

Tomando en cuenta que este B obtenido anteriormente es uno tal que al ser reemplazado en   
B^2 + b - (x(x-1)-2z)
da 0.

Se le aumenta una unidad, pues necesitamos el B más pequeño que satisfaga la siguiente expresión 
B^2 + b - (x(x-1)-2z) > 0.

Y si el B obtenido en la función cuadrática era racional pero no natural, se le aplica la función de piso. Ya que B debe ser un número natural.

Una vez encontrado B, se imprime cuántos números hay entre X y B, incluyendo a X. (B-X+1) 
"""
from math import sqrt
from math import floor
X = int(input())
Z= int(input())
while (X>=Z):
    Z = int(input())

dis = 1+4*(2*Z+X*(X-1))
B = 1+floor((-1+sqrt(dis))/2)
print(B-X+1)

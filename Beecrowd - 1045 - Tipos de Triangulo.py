"""
Beecrowd
Problema 1045 Tipos de Triángulos
Link:https://www.beecrowd.com.br/judge/es/problems/view/1045
Se guardan los lados del triangulo en una lista, para ordenarla de mayor a menor y asignar las variables a,b,c de la misma manera. Luego se usan varias condicionales para encontrar que tipo de triángulo se tiene e imprimirlo. Estas condicionales usan las propiedades dadas en el enunciado del problema.
"""
Lista = list(map(float,input().split()))
Lista.sort(reverse=True)
A = Lista[0]
B = Lista[1]
C = Lista[2]

if A>= (B+C):
    print("NAO FORMA TRIANGULO")
    quit()
if A*A == (B*B+C*C):
    print("TRIANGULO RETANGULO")
if A*A> (B*B + C*C):
    print("TRIANGULO OBTUSANGULO")
if A*A< (B*B+C*C):
    print("TRIANGULO ACUTANGULO")
if A == B and B == C:
    print("TRIANGULO EQUILATERO")
elif (A == B or B==C):
    print("TRIANGULO ISOSCELES")

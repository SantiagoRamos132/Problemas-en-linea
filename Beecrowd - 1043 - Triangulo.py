"""
Beecrowd
Problema 1043 Triángulo
Link:https://www.beecrowd.com.br/judge/es/problems/view/1043
Se almacenan la entrada en tres variables, si se aplica la desigualdad triángular usando las variables
almacenadas como los lados de un triángulo se imprime el perímetro de dicho triangulo. En caso contrario
se imprime el área de un trapecio usando las variables de entrada según indica el problema.
"""
a,b,c = map(float,input().split())
if (a+b>c) and (b+c>a) and (c+a>b):
    print("Perimetro =", (a+b+c))
else:
    print("Area =",((a+b)/2)*c)

"""
Beecrowd
Problema 1159 Sum of Consecutive Even Numbers
Link:https://www.beecrowd.com.br/judge/es/problems/view/1159
Se lee un entero X y se imprime la suma de los siguientes 5 números pares a partir de X (incluyendo X si es par).
Se factoriza la siguiente expresión que calcula la suma de 5 números pares consecutivos:
    x+x+2+x+4+x+6+x+8
Resultando en
    5x+20
Luego en
    5(x+4)
Y se imprime el resultado de la expresión de arriba remplazando X en caso de que X sea par.
Si X es impar, se aumenta en 1, cambiando la expresión anterior a 5(x+5), y se imprime el resultado de reemplazar
X en la expresión anterior.
"""
while True:
    x = int(input())
    if x%2:
        print(5*(x+5))
    else:
        if x==0:
            break
        print(5*(x+4))
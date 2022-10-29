"""
Beecrowd
Problema 1146 Growing Sequences
Link:https://www.beecrowd.com.br/judge/es/problems/view/1146
Se lee un número X, y se imprime en una sola línea todos los números desde 1 hasta X. Esto se repite hasta que 
X sea 0.
Debido a que en python el valor booleano de Falso es cero, el programa se ejecuta dentro de un while que tiene
como condición el número X, ya que permite repetir el bucle mientras X no sea 0, y cuando sea X sea 0, se termina
el bucle, lo que resulta en el fin del programa.
"""
x = int(input())
while x:
    texto = "1"
    for i in range(2,x+1):
        texto= texto+f" {i}"
    print (texto)
    x = int(input())

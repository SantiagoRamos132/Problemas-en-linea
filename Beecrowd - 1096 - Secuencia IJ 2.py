"""
Beecrowd
Problema 1096 Secuencia IJ 2
Link:https://www.beecrowd.com.br/judge/es/problems/view/1096
Se crea un programa que imprime una secuencia que utiliza una variable I iniciada que recorre los números impares de 1 hasta 9.
Por cada valor que toma I, se imprime I tres veces, la primera junta el string "J=7", la segunda con "J=6" y la tercera con "J=5".
"""
I =1
while I<10:
    print(f'I={I} J=7')
    print(f'I={I} J=6')
    print(f'I={I} J=5')
    I+=2

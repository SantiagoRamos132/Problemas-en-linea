"""
Beecrowd
Problema 1097 Secuencia IJ 3
https://www.beecrowd.com.br/judge/es/problems/view/1097
Se crea un programa que imprime una secuencia que utiliza una dos variables "I" y "J". La variable J inicia en 7 y la variable I en 1. La variable
I recorre los números impares de 1 hasta 9 y por cada valor que toma I, se imprime I tres veces, la primera junto al valor de J, la segunda con J-1 y la tercera con J-2, y cuando I pasa al siguiente número, J se incrementa en 2.
XX
"""
I =1
J = 7
while I<10:
    print(f'I={I} J={J}')
    print(f'I={I} J={J-1}')
    print(f'I={I} J={J-2}')
    I+=2
    J+=2

